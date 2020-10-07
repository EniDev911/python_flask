from flask import Flask

app = Flask(__name__)

@route('/')
def home():
    return 'test response'