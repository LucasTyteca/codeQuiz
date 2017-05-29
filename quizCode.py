from flask import Flask
from flask import render_template
from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quizzen')
def quizzenPage():
    return render_template("quizzen.html")


@app.route('/statistieken')
def statistiekenPage():
    return render_template("statistieken.html")


if __name__ == '__main__':
    app.run(debug=True)
