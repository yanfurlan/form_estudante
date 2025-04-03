from flask import Flask
from routes import app
import database

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)
