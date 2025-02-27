
# File: data_tools.py

import pandas as pd
import seaborn as sns
import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.graphics.texture import Texture
import matplotlib.pyplot as plt
import numpy as np



class EnhancedVisualizationApp(App):
    def build(self):
        self.data = None  # DataFrame for loaded data
        self.selected_column = None  # Column for single-column visualizations
        self.selected_x_column = None  # X-axis column for scatter plots
        self.selected_y_column = None  # Y-axis column for scatter plots
        self.selected_chart_type = "Bar Chart"  # Default chart type

        # Root layout
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # File loading section
        file_label = Label(text="Load Dataset:", size_hint=(1, 0.1))
        file_button = Button(text="Browse File", size_hint=(1, 0.1))
        file_button.bind(on_press=self.open_file_chooser)

        # Column selection for single-column visualizations
        column_label = Label(text="Select Column:", size_hint=(1, 0.1))
        self.column_dropdown = DropDown()
        self.column_button = Button(text="Select Column", size_hint=(1, 0.1))
        self.column_button.bind(on_release=self.column_dropdown.open)
        self.column_dropdown.bind(on_select=lambda instance, x: self.select_column(x))

        # Column selection for scatter plot (X and Y axes)
        scatter_label = Label(text="Select Columns for Scatter Plot:", size_hint=(1, 0.1))
        self.x_column_dropdown = DropDown()
        self.x_column_button = Button(text="Select X Column", size_hint=(1, 0.1))
        self.x_column_button.bind(on_release=self.x_column_dropdown.open)
        self.x_column_dropdown.bind(on_select=lambda instance, x: self.select_x_column(x))

        self.y_column_dropdown = DropDown()
        self.y_column_button = Button(text="Select Y Column", size_hint=(1, 0.1))
        self.y_column_button.bind(on_release=self.y_column_dropdown.open)
        self.y_column_dropdown.bind(on_select=lambda instance, x: self.select_y_column(x))

        # Chart type selection
        chart_type_label = Label(text="Select Chart Type:", size_hint=(1, 0.1))
        self.chart_type_dropdown = DropDown()
        self.chart_type_button = Button(text="Bar Chart", size_hint=(1, 0.1))
        self.chart_type_button.bind(on_release=self.chart_type_dropdown.open)
        self.chart_type_dropdown.bind(on_select=lambda instance, x: self.select_chart_type(x))
        for chart_type in ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Pie Chart", "Heatmap"]:
            btn = Button(text=chart_type, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.chart_type_dropdown.select(btn.text))
            self.chart_type_dropdown.add_widget(btn)

        # Chart customization
        customization_label = Label(text="Chart Customization:", size_hint=(1, 0.1))
        self.chart_title_input = TextInput(hint_text="Enter Chart Title", size_hint=(1, 0.1))
        self.chart_color_input = TextInput(hint_text="Enter Color (e.g., blue)", size_hint=(1, 0.1))
        self.histogram_bins_input = TextInput(hint_text="Bins (for Histogram)", size_hint=(1, 0.1))

        # Save chart button
        save_button = Button(text="Save Chart as Image", size_hint=(1, 0.2))
        save_button.bind(on_press=self.save_chart)

        # Render chart button
        render_button = Button(text="Render Chart", size_hint=(1, 0.2))
        render_button.bind(on_press=self.render_chart)

        # Chart display
        self.chart_image = Image(size_hint=(1, 1))

        # Add widgets to the root layout
        self.root.add_widget(file_label)
        self.root.add_widget(file_button)
        self.root.add_widget(column_label)
        self.root.add_widget(self.column_button)
        self.root.add_widget(scatter_label)
        self.root.add_widget(self.x_column_button)
        self.root.add_widget(self.y_column_button)
        self.root.add_widget(chart_type_label)
        self.root.add_widget(self.chart_type_button)
        self.root.add_widget(customization_label)
        self.root.add_widget(self.chart_title_input)
        self.root.add_widget(self.chart_color_input)
        self.root.add_widget(self.histogram_bins_input)
        self.root.add_widget(save_button)
        self.root.add_widget(render_button)
        self.root.add_widget(self.chart_image)

        return self.root

    def open_file_chooser(self, instance):
        """
        Opens a FileChooser popup for selecting a file.
        """
        file_chooser = FileChooserListView()
        popup = Popup(title="Choose a File", content=file_chooser, size_hint=(0.9, 0.9))
        file_chooser.bind(on_submit=lambda file_chooser, selected, touch: self.load_file(selected[0], popup))
        popup.open()

    def load_file(self, file_path, popup):
        """
        Loads the selected file into a Pandas DataFrame.
        """
        try:
            if file_path.endswith(".csv"):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                self.data = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file type! Please use CSV or Excel files.")
            self.populate_column_dropdowns()
            popup.dismiss()
        except Exception as e:
            popup.title = f"Error: {e}"

    def populate_column_dropdowns(self):
        """
        Populates dropdowns with column names for selection.
        """
        if self.data is not None:
            self.column_dropdown.clear_widgets()
            self.x_column_dropdown.clear_widgets()
            self.y_column_dropdown.clear_widgets()
            for column in self.data.columns:
                btn = Button(text=column, size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: self.column_dropdown.select(btn.text))
                self.column_dropdown.add_widget(btn)

                btn_x = Button(text=column, size_hint_y=None, height=44)
                btn_x.bind(on_release=lambda btn: self.x_column_dropdown.select(btn.text))
                self.x_column_dropdown.add_widget(btn_x)

                btn_y = Button(text=column, size_hint_y=None, height=44)
                btn_y.bind(on_release=lambda btn: self.y_column_dropdown.select(btn.text))
                self.y_column_dropdown.add_widget(btn_y)

    def select_column(self, column):
        """
        Sets the selected column for single-column visualizations.
        """
        self.selected_column = column
        self.column_button.text = column

    def select_x_column(self, column):
        """
        Sets the selected X-axis column for scatter plots.
        """
        self.selected_x_column = column
        self.x_column_button.text = column

    def select_y_column(self, column):
        """
        Sets the selected Y-axis column for scatter plots.
        """
        self.selected_y_column = column
        self.y_column_button.text = column

    def select_chart_type(self, chart_type):
        """
        Sets the selected chart type.
        """
        self.selected_chart_type = chart_type
        self.chart_type_button.text = chart_type

    def render_chart(self, instance):
        """
        Renders the selected chart with customization.
        """
        if self.data is None:
            return

        plt.clf()
        color = self.chart_color_input.text or 'blue'
        title = self.chart_title_input.text or f"{self.selected_chart_type} Visualization"

        try:
            if self.selected_chart_type == "Bar Chart":
                self.data[self.selected_column].value_counts().plot(kind='bar', color=color)
            elif self.selected_chart_type == "Line Chart":
                self.data[self.selected_column].plot(kind='line', marker='o', color=color)
            elif self.selected_chart_type == "Scatter Plot":
                self.data.plot.scatter(x=self.selected_x_column, y=self.selected_y_column, color=color)
            elif self.selected_chart_type == "Histogram":
                bins = int(self.histogram_bins_input.text) if self.histogram_bins_input.text.isdigit() else 10
                self.data[self.selected_column].plot(kind='hist', bins=bins, color=color)
            elif self.selected_chart_type == "Pie Chart":
                self.data[self.selected_column].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette())
            elif self.selected_chart_type == "Heatmap":
                sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')

            plt.title(title)
            self.display_chart_as_texture()
        except Exception as e:
            print(f"Error rendering chart: {e}")

    def display_chart_as_texture(self):
        """
        Converts the Matplotlib chart to a Kivy-compatible texture.
        """
        plt.savefig('chart.png', bbox_inches='tight')
        texture = Texture.create()
        texture.mag_filter = 'nearest'
        img = plt.imread('chart.png')
        height, width, _ = img.shape
        texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()
        self.chart_image.texture = texture

    def save_chart(self, instance):
        """
        Saves the current chart as an image.
        """
        plt.savefig('saved_chart.png', bbox_inches='tight')
        print("Chart saved as 'saved_chart.png'")

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