from flask import Flask
from werkzeug.urls import url_quote

app = Flask(__name__)

@app.route('/')
    print("Hello World")

if __name__ == '__main__':
    app.run(debug=True)
