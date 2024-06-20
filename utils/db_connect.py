

import random
import sqlalchemy
from sqlalchemy import null


class Database:
    def __init__(self, driver, username, password, host, dbname):
        self.driver= driver
        self.username= username
        self.password= password
        self.host= host
        self.dbname= dbname
        self.conn = self.dbConnect()
        self.questions = self.conn.exec_driver_sql(f"select idPergunta from {self.dbname}.pergunta order by RANDOM_BYTES(idPergunta)")._allrows()

    def dbConnect(self):
        import sqlalchemy
        driver = self.driver
        user = self.username
        password = self.password
        host = self.host
        db = self.dbname

        #   driver  :// user    :   password   @   host    /   db
        
        engine = sqlalchemy.create_engine(url=f"{driver}://{user}:{password}@{host}:3306/{db}")

        return engine.connect()
    
    def getQuestion(self,):

        query = self.conn.exec_driver_sql(f"select *  from {self.dbname}.pergunta where idPergunta = {self.questions.pop()[0]}")._allrows()
                  
        response    = { "idPergunta":query[0][0],
                                    "texto" : query[0][1],
                                    "acertos":query[0][2],
                                    "repetições":query[0][3],
                                    "reposta":query[0][4]}

        self.conn.exec_driver_sql(f"UPDATE mydb.pergunta SET repetições=repetições+1 where idPergunta={response['idPergunta']}")

        return response