import sqlite3


DATABASE_NAME = "applications.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_application(company, role, date_applied, status):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO applications
        (company, role, date_applied, status)
        VALUES (?, ?, ?, ?)
    """, (company, role, date_applied, status))

    connection.commit()
    connection.close()


def delete_application(application_id):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()

def update_application(application_id, company, role, date_applied, status):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE applications
        SET company = ?,
            role = ?,
            date_applied = ?,
            status = ?
        WHERE id = ?
    """, (company, role, date_applied, status, application_id))

    connection.commit()
    connection.close()
    

def get_applications():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company, role, date_applied, status
        FROM applications
        ORDER BY date_applied DESC
    """)

    applications = cursor.fetchall()

    connection.close()

    return applications