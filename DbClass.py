class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "root",
            "db": "db_quizzen"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = None

    def getAllPlayers(self):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM spelers ORDER BY spelersid ASC "

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getQuizzes(self):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM quiz"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def createNewPlayer(self, fname, lname, dname):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "INSERT INTO spelers (displaynaam,spelersvnaam,spelersnaam) VALUES ('{param1}', '{param2}', '{param3}')"
        sqlCommand = sqlQuery.format(param1=dname, param2=fname, param3=lname)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def updatePlayer(self, id, fname, lname, dname):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE spelers SET displaynaam='{param1}', spelersvnaam='{param2}', spelersnaam='{param3}' where spelersid = {param4}"
        sqlCommand = sqlQuery.format(param1=dname, param2=fname, param3=lname, param4=id)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getQuiz(self, quizid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM quiz WHERE quizid = {param1}"
        sqlCommand = sqlQuery.format(param1=quizid)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getQuizQuestions(self, quizid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM quizvragen WHERE quizid = {param1} order by vraagid ASC "
        sqlCommand = sqlQuery.format(param1=quizid)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getQuizAnswers(self, vraagid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select * from quizantwoorden inner join quizvragen on quizantwoorden.vraagid = quizvragen.vraagid where quizvragen.quizid = {param1};"
        sqlCommand = sqlQuery.format(param1=vraagid)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def createQuiz(self, quizname, quizdescription):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into quiz(quiznaam,beschrijving) values('{param1}', '{param2}')"
        sqlCommand = sqlQuery.format(param1=quizname, param2=quizdescription)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def createQuestion(self, question, quizid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into quizvragen(vraag,quizid) values ('{param1}',{param2})"
        sqlCommand = sqlQuery.format(param1=question, param2=quizid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getLastId(self, table, tableid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select {param1} from {param2} where {param3}=(select max({param4}) from {param5})"
        sqlCommand = sqlQuery.format(param1=tableid, param2=table, param3=tableid, param4=tableid, param5=table)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getLastIdSession(self, table, tableid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select {param1} from {param2} where {param3}=(select max({param4}) from {param5})"
        sqlCommand = sqlQuery.format(param1=tableid, param2=table, param3=tableid, param4=tableid, param5=table)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def createAnswer(self, answer, correct, questionid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into quizantwoorden(antwoord,juist_antwoord,vraagid) values('{param1}', {param2}, {param3})"
        sqlCommand = sqlQuery.format(param1=answer, param2=correct, param3=questionid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getAnswers(self, questionid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select * from quizantwoorden where vraagid = {param1}"
        sqlCommand = sqlQuery.format(param1=questionid)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def createPlayerSessionOne(self, displayname, quizid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into spelerspeeltquiz(displaynaam, quizid, score) values('{param1}', {param2}, 0)"
        sqlCommand = sqlQuery.format(param1=displayname, param2=quizid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def createPlayerSession(self, displaynaam, quizid, sessionid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into spelerspeeltquiz(sessionid, displaynaam, quizid, score) values({param1},'{param2}', {param3}, 0)"
        sqlCommand = sqlQuery.format(param1=sessionid, param2=displaynaam, param3=quizid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def setPlayerAnswer(self, displaynaam, answerid, sessionid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into spelerantwoorden(displaynaam, antwoordid, sessionid) values('{param1}',{param2}, {param3})"
        sqlCommand = sqlQuery.format(param1=displaynaam, param2=answerid, param3=sessionid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def updateSession(self, displaynaam, sessionid, newscore):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE spelerspeeltquiz SET score = {param1} WHERE displaynaam = '{param2}' and sessionid = {param3}"
        sqlCommand = sqlQuery.format(param1=newscore, param2=displaynaam, param3=sessionid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def testscores(self, displaynaam, sessionid, value):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE spelerspeeltquiz SET score = {param1} WHERE displaynaam = '{param2}' and sessionid = {param3}"
        sqlCommand = sqlQuery.format(param1=value, param2=displaynaam, param3=sessionid)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getScores(self, sessionid, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select * from spelerspeeltquiz where displaynaam = '{param1}' and sessionid = {param2}"
        sqlCommand = sqlQuery.format(param1=displaynaam, param2=sessionid)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def statistiekenGetAntwoordSnelheid(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select gemantwoordsnelheid from statistieken where displaynaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def aantalAntwoordenGegeven(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select count(antwoordid) from spelerantwoorden where displaynaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result



    def statistiekenUpdateGemAntw(self, displaynaam, newAntwoordsnelheid):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE statistieken SET gemantwoordsnelheid = '{param1}' WHERE displaynaam = '{param2}'"
        sqlCommand = sqlQuery.format(param1=newAntwoordsnelheid, param2=displaynaam)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def statistiekenUpdateAantalGespeeld(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE statistieken SET aantalgespeeld = aantalgespeeld+1 WHERE displaynaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def statistiekenCreateAndSetAantalGespeeld(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "insert into statistieken(displaynaam, aantalgespeeld, aantalgewonnen, gemantwoordsnelheid, gemacceleratie) VALUES ('{param1}', 1, 0, 0, 0)"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def statistiekenUpdateAantalGewonnen(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "UPDATE statistieken SET aantalgewonnen = aantalgewonnen+1 WHERE displaynaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getStatistiekPlayer(self, displayname):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select * from statistieken where displaynaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=displayname)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getStatistieken(self):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select * from statistieken"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getAmountRightAnswers(self, displaynaam):
        self.__cursor = self.__connection.cursor()
        sqlQuery = "select count(spelerantwoorden.antwoordid) from spelerantwoorden inner join quizantwoorden on spelerantwoorden.antwoordid = quizantwoorden.antwoordid where displaynaam = '{param1}' and quizantwoorden.juist_antwoord = 1"
        sqlCommand = sqlQuery.format(param1=displaynaam)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result