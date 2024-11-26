
# File: data_tools.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from sqlalchemy import create_engine


class DataVisualization:
    def __init__(self):
        """Initialize the visualization class."""
        sns.set(style="whitegrid")

    def plot_correlation_heatmap(self, data: pd.DataFrame, title: str = "Correlation Heatmap"):
        """Generate a heatmap for correlation matrix."""
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        plt.figure(figsize=(12, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title(title)
        plt.show()

    def plot_histogram(self, data: pd.DataFrame, column: str, bins: int = 30):
        """Generate a histogram for a specified column."""
        if column not in data.columns:
            raise ValueError(f"Column '{column}' not found in the dataset.")
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True, bins=bins)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def plot_scatter(self, data: pd.DataFrame, x: str, y: str, hue: str = None):
        """Generate a scatter plot between two variables."""
        if x not in data.columns or y not in data.columns:
            raise ValueError(f"Columns '{x}' and/or '{y}' not found in the dataset.")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=x, y=y, hue=hue, palette="viridis")
        plt.title(f"Scatter Plot of {x} vs {y}")
        plt.show()

    def plot_boxplot(self, data: pd.DataFrame, column: str):
        """Generate a boxplot for a specified column."""
        if column not in data.columns:
            raise ValueError(f"Column '{column}' not found in the dataset.")
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=data[column])
        plt.title(f"Boxplot of {column}")
        plt.show()

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
