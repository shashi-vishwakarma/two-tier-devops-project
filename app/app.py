from flask import Flask
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="employee",
        password="employee123",
        database="employee_db"
    )

@app.route("/")
def home():
    try:
        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()

        conn.close()


        html_rows = ""

        for employee in employees:
            html_rows += f"""
            <tr>
                <td>{employee[0]}</td>
                <td>{employee[1]}</td>
                <td>{employee[2]}</td>
                <td>₹ {employee[3]}</td>
            </tr>
            """

        return f"""
        <html>
        <head>
            <title>Employee Management System</title>
        </head>

        <body>

            <h1>Employee Management System</h1>
            <h3>Welcome to TechNova Solutions</h3>

            <table border="1" cellpadding="10" cellspacing="0">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Department</th>
                    <th>Salary</th>
                </tr>

                {html_rows}

            </table>

        </body>
        </html>
        """

    except Exception as e:
        return f"""
        <h1>Employee Management System</h1>
        <h3>❌ Database Connection Failed</h3>
        <p>{e}</p>
        """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
