import os

from flask import Flask
app = Flask(__name__)

@app.route('/<name>/')
def hello_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/')
def hello_world():
    return 'Hello, world!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8523))
    app.run(host='localhost', port=port)