
# File: data_tools.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from sqlalchemy import create_engine
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooser
from kivy.graphics.texture import Texture
import matplotlib.pyplot as plt
import numpy as np


class PandasVisualizationApp(App):
    def build(self):
        # Root layout
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # File input to load datasets
        file_input_label = Label(text="Load CSV File:", size_hint=(1, 0.1))
        self.file_input = TextInput(hint_text="Enter file path or click Browse", size_hint=(1, 0.1))
        browse_button = Button(text="Browse", size_hint=(1, 0.1))
        browse_button.bind(on_press=self.browse_file)

        # Dropdown for column selection
        column_label = Label(text="Select Column:", size_hint=(1, 0.1))
        self.column_dropdown = DropDown()
        self.column_button = Button(text="Select Column", size_hint=(1, 0.1))
        self.column_button.bind(on_release=self.column_dropdown.open)
        self.column_dropdown.bind(on_select=lambda instance, x: self.select_column(x))

        # Dropdown for chart type selection
        chart_type_label = Label(text="Select Chart Type:", size_hint=(1, 0.1))
        self.chart_type_dropdown = DropDown()
        self.chart_type_button = Button(text="Bar Chart", size_hint=(1, 0.1))
        self.chart_type_button.bind(on_release=self.chart_type_dropdown.open)
        self.chart_type_dropdown.bind(on_select=lambda instance, x: self.select_chart_type(x))
        for chart_type in ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"]:
            btn = Button(text=chart_type, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.chart_type_dropdown.select(btn.text))
            self.chart_type_dropdown.add_widget(btn)

        # Render Button
        render_button = Button(text="Render Chart", size_hint=(1, 0.2))
        render_button.bind(on_press=self.render_chart)

        # Chart display
        self.chart_image = Image(size_hint=(1, 1))

        # Add widgets to the root layout
        self.root.add_widget(file_input_label)
        self.root.add_widget(self.file_input)
        self.root.add_widget(browse_button)
        self.root.add_widget(column_label)
        self.root.add_widget(self.column_button)
        self.root.add_widget(chart_type_label)
        self.root.add_widget(self.chart_type_button)
        self.root.add_widget(render_button)
        self.root.add_widget(self.chart_image)

        # Data attributes
        self.data = None
        self.selected_column = None
        self.selected_chart_type = "Bar Chart"

        return self.root

    def browse_file(self, instance):
        """
        Mock browse function to simulate file loading. In a real app, integrate FileChooser.
        """
        try:
            # Load the file
            file_path = self.file_input.text
            if file_path.endswith(".csv"):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                self.data = pd.read_excel(file_path)
            else:
                self.file_input.hint_text = "Unsupported file type! Use .csv or .xlsx"
                return

            # Populate column dropdown
            self.populate_column_dropdown()
        except Exception as e:
            self.file_input.hint_text = f"Error: {e}"

    def populate_column_dropdown(self):
        """
        Populate the column dropdown with columns from the loaded dataset.
        """
        self.column_dropdown.clear_widgets()
        for column in self.data.columns:
            btn = Button(text=column, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.column_dropdown.select(btn.text))
            self.column_dropdown.add_widget(btn)

    def select_column(self, column):
        self.selected_column = column
        self.column_button.text = column

    def select_chart_type(self, chart_type):
        self.selected_chart_type = chart_type
        self.chart_type_button.text = chart_type

    def render_chart(self, instance):
        if self.data is None or self.selected_column is None:
            self.file_input.hint_text = "Load data and select a column first!"
            return

        # Fetch the selected column
        column_data = self.data[self.selected_column]

        # Generate chart based on selected type
        plt.clf()
        if self.selected_chart_type == "Bar Chart":
            column_data.value_counts().plot(kind='bar', color='blue')
        elif self.selected_chart_type == "Line Chart":
            column_data.plot(kind='line', marker='o', color='green')
        elif self.selected_chart_type == "Scatter Plot":
            x = range(len(column_data))
            plt.scatter(x, column_data, color='red')
        elif self.selected_chart_type == "Histogram":
            column_data.plot(kind='hist', bins=10, color='purple')

        plt.title(f"{self.selected_chart_type} of {self.selected_column}")
        plt.xlabel(self.selected_column)
        plt.ylabel("Frequency" if self.selected_chart_type in ["Bar Chart", "Histogram"] else "Value")

        # Display chart as a Kivy texture
        self.display_chart_as_texture()

    def display_chart_as_texture(self):
        plt.savefig('chart.png', bbox_inches='tight')
        texture = Texture.create()
        texture.mag_filter = 'nearest'
        img = plt.imread('chart.png')
        height, width, _ = img.shape
        texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()
        self.chart_image.texture = texture



class DatabaseConnection:
    def __init__(self, db_path: str):
        """
        Initialize the DatabaseConnection class.
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"Connected to the database at {self.db_path}.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        else:
            print("No active connection to close.")

    def execute_query(self, query: str, params: tuple = None):
        """
        Execute a query on the database.
        :param query: SQL query string.
        :param params: Tuple of parameters for the query.
        :return: Result of the query.
        """
        if not self.connection:
            raise ValueError("No active database connection.")
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
            return cursor
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

class DatabaseDataHandler:
    def __init__(self, db_connection: DatabaseConnection, table_name: str):
        """
        Initialize the DatabaseDataHandler class.
        :param db_connection: An instance of the DatabaseConnection class.
        :param table_name: Name of the table to work with.
        """
        self.db_connection = db_connection
        self.table_name = table_name

    def fetch_data(self) -> pd.DataFrame:
        """Fetch all data from the table as a pandas DataFrame."""
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.db_connection.execute_query(query)
        if cursor:
            data = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return pd.DataFrame(data, columns=columns)
        else:
            print(f"Failed to fetch data from {self.table_name}.")
            return pd.DataFrame()

    def insert_data(self, data: pd.DataFrame):
        """
        Insert data from a pandas DataFrame into the table.
        :param data: Pandas DataFrame with data to insert.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        engine = create_engine(f'sqlite:///{self.db_connection.db_path}')
        try:
            data.to_sql(self.table_name, con=engine, if_exists='append', index=False)
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def delete_data(self, condition: str):
        """
        Delete data from the table based on a condition.
        :param condition: SQL WHERE clause to define which rows to delete.
        """
        query = f"DELETE FROM {self.table_name} WHERE {condition}"
        self.db_connection.execute_query(query)
        print(f"Deleted data where {condition}.")

    def update_data(self, set_clause: str, condition: str):
        """
        Update data in the table based on a condition.
        :param set_clause: SQL SET clause to define new values.
        :param condition: SQL WHERE clause to define which rows to update.
        """
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        self.db_connection.execute_query(query)
        print(f"Updated data where {condition}.")

    def execute_custom_query(self, query: str, params: tuple = None) -> pd.DataFrame:
        """
        Execute a custom SQL query.
        :param query: The SQL query string.
        :param params: Optional parameters to substitute into the query.
        :return: Result of the query as a pandas DataFrame (if applicable).
        """
        cursor = self.db_connection.execute_query(query, params)
        if cursor:
            try:
                data = cursor.fetchall()
                if cursor.description:  # Check if there are column descriptions
                    columns = [description[0] for description in cursor.description]
                    return pd.DataFrame(data, columns=columns)
                else:
                    print("Query executed successfully. No data to fetch.")
                    return pd.DataFrame()
            except Exception as e:
                print(f"Error fetching data from query: {e}")
                return pd.DataFrame()
        else:
            print("Failed to execute custom query.")
            return pd.DataFrame()

#3 classes