from flask import Flask
from flask import render_template
from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/quiz_spelen')
def quizzenPage():
    db = DbClass()
    players = db.getAllPlayers()
    db2 = DbClass()
    quizzes = db2.getQuizzes()
    return render_template("quizzen.html", players=players, quizzes=quizzes)

@app.route('/create_quiz')
def createQuizPage():
    return render_template("createQuiz.html")


@app.route('/statistieken')
def statistiekenPage():
    return render_template("statistieken.html")


if __name__ == '__main__':
    app.run(debug=True)
