from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Customer App - Task 2"

@app.route("/health")
def health():
    return "OK"

@app.route("/db-test")
def db_test():
    try:
        connection = mysql.connector.connect(
            host="customer-db-dev",
            user="customeruser",
            password="customer123",
            database="customerdb"
        )

        connection.close()
        return "Database connection successful"

    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)