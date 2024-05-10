import streamlit as st
import pandas as pd
import sqlite3

# Configuration
DB_NAME = "image_color_choices.db"
ADMIN_USERNAME = "admin"  # Replace with your desired username
ADMIN_PASSWORD = "admin"  # Replace with a strong password (warning: not secure)

# Function to create a database connection
def create_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

# Function to create the user_choices table if it doesn't exist
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_choices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            color1 TEXT,
            color2 TEXT,
            color3 TEXT,
            color4 TEXT,
            color5 TEXT,
            submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

# Function to save data to the database
def save_to_db(conn, data):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_choices (image_name, color1, color2, color3, color4, color5)
        VALUES (?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()

# Function to write data to a CSV file
def write_to_csv(data, filename="image_color_choices.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    st.title("JxC App Data Collection")

    # Database connection
    conn = create_db_connection()
    create_table(conn)

    # User input section
    st.subheader("User Input")

    # Upload image
    uploaded_file = st.file_uploader("Upload Image (JPG or PNG)", type=["jpg", "png"])

    # Set width for color pickers to match file uploader
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        color1 = st.color_picker("Color 1")
    with col2:
        color2 = st.color_picker("Color 2")
    with col3:
        color3 = st.color_picker("Color 3")
    with col4:
        color4 = st.color_picker("Color 4")
    with col5:
        color5 = st.color_picker("Color 5")
    
    # Set width for buttons
    button_container = st.container()
    with button_container:
        submit_button, reset_button = st.columns(2)
        with submit_button:
            if st.button("Submit", use_container_width=True, type="primary"):
                if uploaded_file is not None:
                    image_name = uploaded_file.name
                    data = (image_name, color1, color2, color3, color4, color5)
                    try:
                        save_to_db(conn, data)
                        write_to_csv([data])  # Write to CSV as well
                        st.success("Submission successful!")
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                else:
                    st.warning("Please upload an image file.")
        with reset_button:
            if st.button("Reset Form", use_container_width=True):
                st.session_state.clear()


if __name__ == "__main__":
    main()
