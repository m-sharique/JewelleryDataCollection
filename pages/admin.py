import streamlit as st
import pandas as pd
import sqlite3
import os

# Configuration
DB_NAME = "image_color_choices.db"
ADMIN_USERNAME = "admin"  # Replace with your desired username
ADMIN_PASSWORD = "admin"  # Replace with a strong password (warning: not secure)

# Function to create a database connection
def create_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

# Function to fetch all records from the database
def fetch_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_choices")
    records = cursor.fetchall()
    return records

# Function to display records in tabular format
def display_records(records):
    if len(records) > 0:
        df = pd.DataFrame(records, columns=["ID", "Image Name", "Color 1", "Color 2", "Color 3", "Color 4", "Color 5", "Submitted At"])
        st.dataframe(df)
    else:
        st.write("No records found.")

# Function to download the CSV file of the records
def download_csv(records):
    df = pd.DataFrame(records, columns=["ID", "Image Name", "Color 1", "Color 2", "Color 3", "Color 4", "Color 5", "Submitted At"])
    csv_data = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv_data, file_name="image_color_choices.csv", mime="text/csv")

# Function to clear/delete records from database and CSV file
def clear_records():
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_choices")
    conn.commit()
    conn.close()

    # Delete CSV file if exists
    if os.path.exists("image_color_choices.csv"):
        os.remove("image_color_choices.csv")
        st.success("Deleted")

def main():
    st.title("Admin Page")

    # Admin login section
    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password")

    if st.button("Login"):
        if admin_username == ADMIN_USERNAME and admin_password == ADMIN_PASSWORD:
            st.success("Admin login successful!")

            # Fetch records from the database
            conn = create_db_connection()
            records = fetch_records(conn)

            # Display records in tabular format
            display_records(records)

            # Download CSV button
            download_csv(records)

            # Button to clear/delete records
            st.button("Clear Records", on_click=clear_records)
        else:
            st.error("Invalid admin credentials.")

if __name__ == "__main__":
    main()
