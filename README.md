# CSV Analysis Django Web Application

## Overview

This project is a Django-based web application that allows users to upload CSV files, perform data analysis using `pandas` and `numpy`, and display the results along with visualizations on a web interface.

## Features

1. **File Upload**:

   - Users can upload CSV files via the web interface.
   - Files are stored temporarily for processing.

2. **Data Analysis**:

   - Displays the first few rows of the uploaded CSV file.
   - Calculates basic summary statistics (mean, median, standard deviation) for numerical columns.
   - Identifies and handles missing values.

3. **Data Visualization**:

   - Generates basic plots (e.g., histograms for numerical columns) using `matplotlib` or `seaborn`.
   - Displays the visualizations on the web page.

4. **User-Friendly Interface**:

   - Simple and clean interface for uploading files and viewing results.

## Technologies Used

- **Backend**: Django 4.2
- **Frontend**: HTML, CSS (via Django templates)
- **Data Processing**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`

---

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Steps to Set Up the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/csv_analysis_project.git
   cd csv_analysis_project
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

---

## Project Structure

```
csv_analysis_project/
|-- analyzer/              # Django app for CSV analysis
|   |-- templates/         # HTML templates
|   |-- views.py           # Application logic
|   |-- urls.py            # App-specific URLs
|-- csv_analysis_project/  # Main project folder
|   |-- settings.py        # Project settings
|   |-- urls.py            # Project URLs
|-- media/                 # Temporary storage for uploaded files
|-- requirements.txt       # Python dependencies
|-- manage.py              # Django management script
```

---

## How It Works

1. **Uploading a CSV File**:

   - Users upload a CSV file via the homepage.

2. **Data Analysis**:

   - The file is processed using `pandas` to extract useful insights.
   - Basic statistics and missing values are calculated.

3. **Visualization**:

   - The application generates histograms for numerical columns using `matplotlib` or `seaborn`.
   - The plots and data summaries are displayed on the results page.

---

## Sample CSV File

A sample CSV file is included in the repository as `sample.csv`. This file can be used to test the application.

---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push the branch to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Author

Developed by Raghavendra

