﻿# Jewellery Data Collection

This repository facilitates the collection of data for image-based object color recommendation. It includes Streamlit web applications for both data collection and administration, utilizing SQLite for database management.

## How to Use

1. **Fork this Repository**: Click the "Fork" button at the top-right corner of this page to create a copy of this repository in your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/m-sharique/JewelleryDataCollection.git
   ```

3. **Install Dependencies**: Navigate to the cloned directory and install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Applications**:
   - To start the data collection application, run `app.py`.
   - To access the admin interface for data management, navigate to the `pages/` directory and run `admin.py`.

5. **Contribute**: Make necessary changes, improvements, or bug fixes to the codebase, and submit pull requests to contribute back to the original repository.

## Files and Directories

- `app.py`: Streamlit web application for data collection.
- `pages/admin.py`: Streamlit web application for administration and data management.
- `requirements.txt`: List of Python dependencies required for the project.
- `image_color_choices.db`: SQLite database file to store user choices.
- `README.md`: This file providing information about the repository.

## Repository Structure

```
JewelleryDataCollection/
│
├── app.py
├── requirements.txt
├── image_color_choices.db
├── README.md
└── pages/
    └── admin.py
```
