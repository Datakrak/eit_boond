import os
import sys
from flask import Flask

app = Flask(__name__)

sys.path.insert(0, os.path.dirname(__file__))

@app.route('/')
def index():
    return 'Hellow World!'

if __name__ == '__main__':
    app.run()

