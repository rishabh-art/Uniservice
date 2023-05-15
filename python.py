from flask import Flask

import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    # Establish a connection
    connection = mysql.connector.connect(
        host="dumbo.db.elephantsql.com",
        user="imddrpva",
        password="Fjwbme_N7rGG2Nf0zXu4PXVSwJT1kWVW",
        database="imddrpva"
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute a SELECT query
    cursor.execute("SELECT * FROM your_table")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Process the retrieved data and generate HTML
    html = "<ul>"
    for row in rows:
        html += f"<li>{row[0]} - {row[1]}</li>"
    html += "</ul>"

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()

    return html

if __name__ == "__main__":
    app.run()
