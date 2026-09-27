# Job Application Tracker

A simple job application tracker built with Python, Streamlit, SQLite and Pandas.

## Features

* Add job applications
* View all applications
* Filter applications by status
* Sort applications by date or company
* Update existing applications
* Delete applications
* Dashboard with application statistics
* Applications by Status chart
* Local data storage using SQLite

## Technologies

* Python
* Streamlit
* Pandas
* SQLite

## Project Structure

```text
job-application-tracker/
├── app.py
├── database.py
├── applications.db
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

The application will open in the browser.

## Database

The application uses SQLite to store job applications locally in:

```text
applications.db
```

The database is created automatically when the application starts.

## Application Statuses

The application supports the following statuses:

* Applied
* Interview
* Offer
* Rejected

## Usage Walkthrough

### 1. Start the application

Open PowerShell in the project folder and run:

```powershell
streamlit run app.py
```

The application will open in your browser.

### 2. Add an application

Go to **Add Application**.

Enter:

* Company
* Role
* Date Applied
* Status

Click **Add Application**.

The new application will appear under **Your Applications**.

### 3. View and filter applications

Under **Your Applications**, you can:

* View all saved applications
* Filter applications by status
* Sort applications by date
* Sort applications by company

### 4. Update an application

Go to **Update Application**.

Select the application using the company and role shown in the dropdown.

Change the information you want and click **Update Application**.

### 5. Delete an application

Go to **Delete Application**.

Select the application you want to remove.

Confirm the deletion and click **Delete Selected Application**.

### 6. View statistics

The dashboard displays:

* Total applications
* Interviews
* Offers
* Conversion rate

The **Applications by Status** chart provides a visual overview of application statuses.

### 7. Data storage

Applications are stored locally in the SQLite database:

```text
applications.db
```

The data remains available when the application is stopped and started again.
