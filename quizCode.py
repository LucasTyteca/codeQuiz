#imports
# from time import sleep
# sleep(20)
import json as json

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

import game as game
from DbClass import DbClass

#from piScripts import game as game

#db class aanmaken
db = DbClass()

#globals
global amoutQuestionsNewQuiz
global quizid
global player1
global player2
global player3
global player4
global chosenQuizId
global whatQuestion
whatQuestion = 0
global amountOfQuestions
global sessionid
global done
done = True
def modify(value, whatGlobal):
    if whatGlobal == "amoutQuestionsNewQuiz":
        global amoutQuestionsNewQuiz
        amoutQuestionsNewQuiz = value
    elif whatGlobal == "quizid":
        global quizid
        quizid = value[0]
    elif whatGlobal == "player1":
        global player1
        player1 = value
    elif whatGlobal == "player2":
        global player2
        player2 = value
    elif whatGlobal == "player3":
        global player3
        player3 = value
    elif whatGlobal == "player4":
        global player4
        player4 = value
    elif whatGlobal == "chosenQuizId":
        global chosenQuizId
        chosenQuizId = value
    elif whatGlobal == "whatQuestion":
        global whatQuestion
        whatQuestion = value
    elif whatGlobal == "amountOfQuestions":
        global amountOfQuestions
        amountOfQuestions = value
    elif whatGlobal == "sessionid":
        global sessionid
        sessionid = value
    elif whatGlobal == "done":
        global done
        done = value
def use(whatGlobal):
    if whatGlobal == "amoutQuestionsNewQuiz":
        return amoutQuestionsNewQuiz
    elif whatGlobal == "quizid":
        return quizid
    elif whatGlobal == "player1":
        return player1
    elif whatGlobal == "player2":
        return player2
    elif whatGlobal == "player3":
        return player3
    elif whatGlobal == "player4":
        return player4
    elif whatGlobal == "chosenQuizId":
        return chosenQuizId
    elif whatGlobal == "whatQuestion":
        return whatQuestion
    elif whatGlobal == "amountOfQuestions":
        return amountOfQuestions
    elif whatGlobal == "sessionid":
        return sessionid
    elif whatGlobal == "done":
        global done
        return done

#definities
def testthreading(quiz, question, scores, answers):
    return render_template("quizVraag.html", quiz=quiz, question=question, answers=answers, player1=use("player1"), player2=use("player2"), player3=use("player3"), player4=use("player4"), scores=scores)

def testthredding2():
    return redirect('/quizvraag')

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
        modify(request.form['displayname1'], "player1")
        modify(request.form['displayname2'], "player2")
        modify(request.form['displayname3'], "player3")
        modify(request.form['displayname4'], "player4")
        modify(request.form['choosequizdrop'], "chosenQuizId")
        createsessionid = db.getLastIdSession("spelerspeeltquiz", "sessionid")
        playerslist = [use("player1"), use("player2"), use("player3"), use("player4")]
        for player in playerslist:
            test = db.getStatistiekPlayer(player)
            if len(test) == 0:
                db.statistiekenCreateAndSetAantalGespeeld(player)
            else:
                db.statistiekenUpdateAantalGespeeld(player)
        if createsessionid == []:
            modify(1, "sessionid")
        else:
            modify(createsessionid[0][0]+1, "sessionid")
        db.createPlayerSession(use("player1"), use("chosenQuizId"), use("sessionid"))
        db.createPlayerSession(use("player2"), use("chosenQuizId"), use("sessionid"))
        db.createPlayerSession(use("player3"), use("chosenQuizId"), use("sessionid"))
        db.createPlayerSession(use("player4"), use("chosenQuizId"), use("sessionid"))
        return redirect('/quizvraag')

    players = db.getAllPlayers()
    playersjs = json.dumps(players)
    quizzes = db.getQuizzes()
    quizzesjs = json.dumps(quizzes)
    return render_template("quizzen.html", players=players, quizzes=quizzes, playersjs=playersjs, quizzesjs=quizzesjs)


@app.route('/quizvraag',  methods=['GET', 'POST'])
def quizVraag():
    trydone = use("done")
    if trydone == False:
        if request.method == "POST":
            print(use("done"))
            try:
                button = request.form["btn"]
                return redirect('/quiz_beindigt')
            except:
                quizid = use("chosenQuizId")
                quiz = db.getQuiz(quizid)
                quivragen = db.getQuizQuestions(quiz[0])
                modify(len(quivragen), "amountOfQuestions")
                question = quivragen[use("whatQuestion")]
                answers = db.getAnswers(question[0])
                answerids = []
                for answer in answers:
                    answerids.append(answer[0])
                    if answer[2] == 1:
                        rightAnswer = answers.index(answer)
                playerslist = [use("player1"), use("player2"), use("player3"), use("player4")]
                data = game.firstButtonPush(rightAnswer, [], len(playerslist), len(answers), playerslist, answerids, use("sessionid"))
                print(data)
                for smallList in data:
                    for tupple in smallList:
                        if len(tupple) == 2:
                            gemAntwoordSnelheid = db.statistiekenGetAntwoordSnelheid(tupple[0])
                            aantalAntwoorden = db.aantalAntwoordenGegeven(tupple[0])
                            newGemAntwoordSnelheid = gemAntwoordSnelheid[0][0] * aantalAntwoorden[0][0]
                            newGemAntwoordSnelheid += tupple[1]
                            newGemAntwoordSnelheid = newGemAntwoordSnelheid / (aantalAntwoorden[0][0] + 1)
                            db.statistiekenUpdateGemAntw(tupple[0], newGemAntwoordSnelheid)
                        else:
                            db.setPlayerAnswer(tupple[0], tupple[1], sessionid)
                            if tupple[2] == 1:
                                oldscore = db.getScores(sessionid, tupple[0])
                                newscore = oldscore[0][3] + 1
                                db.updateSession(tupple[0], sessionid, newscore)
                modify(True, "done")
                modify(use("whatQuestion")+1,"whatQuestion")
                if(use("whatQuestion")==use("amountOfQuestions")):
                    modify(0, "whatQuestion")
                    return redirect('/quiz_beindigt')
                else:
                    return redirect('/quizvraag')
    modify(False, "done")
    quizid = use("chosenQuizId")
    quiz = db.getQuiz(quizid) #
    quivragen = db.getQuizQuestions(quiz[0])
    modify(len(quivragen), "amountOfQuestions")
    question = quivragen[use("whatQuestion")]
    answers = db.getAnswers(question[0])
    scores = [db.getScores(use("sessionid"), use("player1")), db.getScores(use("sessionid"), use("player2")), db.getScores(use("sessionid"), use("player3")), db.getScores(use("sessionid"), use("player4")) ]
    print(scores)
    return render_template("quizVraag.html", quiz=quiz, question=question, answers=answers, player1=use("player1"), player2=use("player2"), player3=use("player3"), player4=use("player4"), scores=scores)

@app.route('/quizRule', methods=['GET', 'POST'])
def quizRules():
    if request.method=='POST':
        playerslist = [use("player1"), use("player2"), use("player3"), use("player4")]
        game.readRules(len(playerslist), playerslist)
        return redirect('/quizvraag')
    return render_template("quizRules.html")

@app.route('/create_quiz',  methods=['GET', 'POST'])
def createQuizPage():
    if request.method=='POST':
        try:
            if request.form['btn'] =="Bewerken":
                quizid = request.form['chooseditquiz']
                quiz = db.getQuiz(quizid)
                quizvragen = db.getQuizQuestions(quiz[0])
                answers = db.getQuizAnswers(quizid)
                return editQuiz(quiz, quizvragen, answers)
        except:
            quizname = request.form['quizname']
            quizdescription = request.form['description']
            db.createQuiz(quizname, quizdescription)
            quizid = db.getLastId("quiz","quizid")
            modify(quizid, "quizid")
            modify(int(request.form['amountquestions']), "amoutQuestionsNewQuiz")
            return redirect('/newQuiz')

    quizzes = db.getQuizzes()
    quizzesjs = json.dumps(quizzes)
    return render_template("createQuiz.html", quizzes=quizzes, quizzesjs=quizzesjs)


@app.route('/statistieken')
def statistiekenPage():
    statistieken = db.getStatistieken()
    players = []
    aantalGespeeld = []
    aantalGewonnen = []
    gemAntwoordSnelheid = []
    listJuisteAntwoorden = []
    for tupple in statistieken:
        players.append(tupple[1])
        aantalGespeeld.append(tupple[2])
        aantalGewonnen.append(tupple[3])
        gemAntwoordSnelheid.append(tupple[4])
    for player in players:
        juisteAntwoorden = db.getAmountRightAnswers(player)
        listJuisteAntwoorden.append(juisteAntwoorden[0][0])
    print(listJuisteAntwoorden)
    return render_template("statistieken.html", players=players, aantalGespeeld=aantalGespeeld, aantalGewonnen=aantalGewonnen, gemAntwoordSnelheid=gemAntwoordSnelheid, juisteAntwoorden=listJuisteAntwoorden)


@app.route('/quiz_beindigt')
def quizBeindigt():
    scores = [db.getScores(use("sessionid"), use("player1")), db.getScores(use("sessionid"), use("player2")), db.getScores(use("sessionid"), use("player3")), db.getScores(use("sessionid"), use("player4"))]
    omzettenScores = []
    for score in scores:
        omzettenScores.append(score[0][3])
    scores = omzettenScores
    playerAndScores = [(player1, scores[0]), (player2, scores[1]), (player3, scores[2]), (player4, scores[3])]
    sortedPlayerAndScores = sorted(playerAndScores, key=lambda player:player[1], reverse=True)
    db.statistiekenUpdateAantalGewonnen(sortedPlayerAndScores[0][0])

    return render_template("quizBeindigt.html", playerAndScores=sortedPlayerAndScores)


@app.route('/editQuiz')
def editQuiz(quiz, vragen, antwoorden):
    return render_template("editQuiz.html", quiz=quiz, questions=vragen, answers=antwoorden)


@app.route('/newQuiz',  methods=['GET', 'POST'])
def newQuiz():
    if request.method == 'POST':
        amountOfQuestions = use("amoutQuestionsNewQuiz") + 1
        quizid = use("quizid")
        for x in range(1, amountOfQuestions):
            question = request.form[str(x)]
            db.createQuestion(question, quizid)
            questionid = db.getLastId("quizvragen","vraagid")[0]
            for y in range(1,5):
                answer = request.form[str(x) + str(y)]
                if answer != "":
                    print(str(x) + str(x) + str(y))
                    try:
                        correct = request.form[str(x) + str(x) + str(y)]
                        corbool = 1
                    except:
                        corbool = 0
                    db.createAnswer(answer,corbool,questionid)
        return redirect('/')
    amountOfQuestions = use("amoutQuestionsNewQuiz")+1
    return render_template("newQuiz.html", amountOfQuestions=amountOfQuestions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
