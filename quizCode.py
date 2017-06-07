from flask import Flask
from flask import render_template
from DbClass import DbClass
from flask import request
import json as json
db = DbClass()

def quizzenSubmitted():
    # player1
    valueplayer = request.form['chooseplayer1']
    fnameplayer = request.form['firstname1']
    lnameplayer = request.form['lastname1']
    displayplayer = request.form['displayname1']
    if valueplayer == "newPlayer":
        db.createNewPlayer(fnameplayer, lnameplayer, displayplayer)
    else:
        db.updatePlayer(valueplayer, fnameplayer, lnameplayer, displayplayer)

    # player2
    valueplayer = request.form['chooseplayer2']
    fnameplayer = request.form['firstname2']
    lnameplayer = request.form['lastname2']
    displayplayer = request.form['displayname2']
    if valueplayer == "newPlayer":
        db.createNewPlayer(fnameplayer, lnameplayer, displayplayer)
    else:
        db.updatePlayer(valueplayer, fnameplayer, lnameplayer, displayplayer)

    # player3
    valueplayer = request.form['chooseplayer3']
    fnameplayer = request.form['firstname3']
    lnameplayer = request.form['lastname3']
    displayplayer = request.form['displayname3']
    if valueplayer == "newPlayer":
        db.createNewPlayer(fnameplayer, lnameplayer, displayplayer)
    else:
        db.updatePlayer(valueplayer, fnameplayer, lnameplayer, displayplayer)

    # player4
    valueplayer = request.form['chooseplayer4']
    fnameplayer = request.form['firstname4']
    lnameplayer = request.form['lastname4']
    displayplayer = request.form['displayname4']
    if valueplayer == "newPlayer":
        db.createNewPlayer(fnameplayer, lnameplayer, displayplayer)
    else:
        db.updatePlayer(valueplayer, fnameplayer, lnameplayer, displayplayer)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/quiz_spelen',  methods=['GET', 'POST'])
def quizzenPage():
    if request.method == 'POST':
        quizzenSubmitted()
        player1 = request.form['displayname1']
        player2 = request.form['displayname2']
        player3 = request.form['displayname3']
        player4 = request.form['displayname4']
        quiz = request.form['choosequizdrop']
        return quizVraag(quiz, player1, player2, player3, player4)

    players = db.getAllPlayers()
    playersjs = json.dumps(players)
    quizzes = db.getQuizzes()
    quizzesjs = json.dumps(quizzes)
    return render_template("quizzen.html", players=players, quizzes=quizzes, playersjs=playersjs, quizzesjs=quizzesjs)

@app.route('/create_quiz')
def createQuizPage():
    return render_template("createQuiz.html")


@app.route('/statistieken')
def statistiekenPage():
    return render_template("statistieken.html")

@app.route('/quizvraag')
def quizVraag(quizid, player1, player2, player3, player4):
    quiz = db.getPlayingQuiz(quizid)
    quivragen = db.getQuizQuestions(quiz[0])
    answers = db.getQuizAnswers(quizid)
    return render_template("quizVraag.html", quiz=quiz, questions=quivragen, answers = answers, player1=player1, player2=player2, player3=player3, player4=player4)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
