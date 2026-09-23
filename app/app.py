from flask import Flask
import mysql.connector
import os

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
    host=os.getenv("DB_HOST", "customer-db-dev"),
    user=os.getenv("DB_USER", "customeruser"),
    password=os.getenv("DB_PASSWORD", "customer123"),
    database=os.getenv("DB_NAME", "customerdb")
)
        connection.close()
        return "Database connection successful"

    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)