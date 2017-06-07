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

    def getPlayingQuiz(self, quizid):
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