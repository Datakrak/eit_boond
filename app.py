import os
import sys
from flask import Flask
from dotenv import load_dotenv
import boondmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector as MC

from index import main_index

app = Flask(__name__)

sys.path.insert(0, os.path.dirname(__file__))

load_dotenv()
DB_IP=os.getenv('DB_IP')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
DB_NAME=os.getenv('DB_NAME')

db_url = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_IP}:3306/{DB_NAME}"

engine = create_engine(db_url)


@app.route('/')
def index():
    main_index()
    return "Hello world"

if __name__ == '__main__':
    app.run()

