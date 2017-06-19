from RPi import GPIO as GPIO
from DbClass import DbClass
import time
GPIO.setmode(GPIO.BCM)
#knoppen declareren
#player buttons
playerButtons = [17, 24, 16, 22] #oranje, groen, blauw, rood
buttonOrange = 17
buttonGreen = 24
buttonBlue = 16
buttonRed = 22
#answer buttons
answerA = 21
answerB = 26
answerC = 19
answerD = 13
answerButtons = [21, 26 , 19, 13]


#leds declareren
leds = [27, 25, 18, 6] #oranje, groen, blauw, rood
ledOrange = 27
ledGreen = 25
ledBlue = 18
ledRed = 6

#andere variabalen
bannedPlayers = []
db = DbClass()

#buttons setup
#player buttons
for x in range(0,4):
    GPIO.setup(playerButtons[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)
#answer buttons
for x in range(0,4):
    GPIO.setup(answerButtons[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#leds setup
for x in range(0,4):
    GPIO.setup(leds[x], GPIO.OUT)
    GPIO.output(leds[x], GPIO.LOW)

def readPlayerButtons(amountPlayers):
    for x in range(0,amountPlayers):
        if GPIO.input(playerButtons[x]) == 0:
            return x
    return 9

def readAnswerButtons(amountAnswers):
    for x in range(0,amountAnswers):
        if GPIO.input(answerButtons[x]) == 0:
            return x
    return 9
answers = []
antwoordSnelheidList = []
returndata = []
def firstButtonPush(rightAnswer, bannedPlayers, amountPlayers, amountAnswers, players, answerids, sessionid):
    pushed = False
    which = 9
    pushedPlayer = None
    pushedAnswer = None
    pushed = False
    for x in range(0,amountPlayers):
        if x not in bannedPlayers:
            GPIO.output(leds[x], GPIO.HIGH)
        else:
            GPIO.output(leds[x], GPIO.LOW)

    start = time.time()
    while pushed == False:
        which = readPlayerButtons(amountPlayers)
        if which != 9:
            end = time.time()
            if which not in bannedPlayers:
                pushed = True
                pushedPlayer = which
    pushed = False
    reactionTime = end - start
    for x in range(0, amountPlayers):
        if x != which:
            GPIO.output(leds[x], GPIO.LOW)

    while pushed == False:
        which = readAnswerButtons(amountAnswers)
        if which != 9:
            pushed = True
            pushedAnswer = which
            which = 9

    tuppleReactionTime = (players[pushedPlayer], reactionTime)
    antwoordSnelheidList.append(tuppleReactionTime)
    if pushedAnswer == rightAnswer:
        bannedPlayers.clear()
        # db.setPlayerAnswer(players[pushedPlayer], answerids[pushedAnswer], sessionid)
        # oldscore = db.getScores(sessionid, players[pushedPlayer])
        # newscore = oldscore[0][3] + 1
        # db.updateSession(players[pushedPlayer], sessionid, newscore)
        answerstupple = (players[pushedPlayer], answerids[pushedAnswer], 1)
        answers.append(answerstupple)
        returndata.clear()
        returndata.append(antwoordSnelheidList)
        returndata.append(answers)
        print(returndata)
        antwoordSnelheidList.clear()
        answers.clear()
        return returndata
    else:
        bannedPlayers.append(pushedPlayer)
        answerstupple = (players[pushedPlayer], answerids[pushedAnswer], 0)
        answers.append(answerstupple)
        if len(bannedPlayers)==amountPlayers:
            bannedPlayers.clear()
            print("all players are banned")
            returndata.clear()
            returndata.append(antwoordSnelheidList)
            returndata.append(answers)
            antwoordSnelheidList.clear()
            answers.clear()
            return returndata
        return firstButtonPush(rightAnswer, bannedPlayers, amountPlayers, amountAnswers, players, answerids, sessionid)

def readRules(amountPlayers, playersList):
    playersPushed = False
    players = amountPlayers
    playerlist = playersList
    while playersPushed == False:
        pushed = readPlayerButtons(amountPlayers)
        if pushed != 9:
            GPIO.output(leds[pushed], GPIO.HIGH)
            playerlist.remove(playerlist[pushed])
            pushed = 9
        if len(playerlist)==0:
            playersPushed = True