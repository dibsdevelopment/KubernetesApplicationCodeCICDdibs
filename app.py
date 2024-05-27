from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Dibs completed IIT Computer Science MTech degree'
