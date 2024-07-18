import sqlite3


conn = sqlite3.connect('perguntas_respostas.db')


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS perguntas_respostas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta VARCHAR(255),
    resposta VARCHAR(255)
)
''')


conn.commit()

def close_database():
    global conn
    conn.close()

def insert_question(question, answer):
    cursor.execute('''
    INSERT INTO perguntas_respostas (pergunta, resposta)
    VALUES (?, ?)
    ''', (question, answer))
    conn.commit()


def search_all_questions():
    cursor.execute('SELECT * FROM perguntas_respostas')
    return cursor.fetchall()


insert_question('Quanto é 8 + 5?', '13')
insert_question('Quanto é 15 - 7?', '8')
insert_question('Quanto é 12 + 9?', '21')
insert_question('Quanto é 20 - 10?', '10')
insert_question('Quanto é 14 + 6?', '20')
insert_question('Quanto é 18 - 5?', '13')
insert_question('Quanto é 7 + 8?', '15')
insert_question('Quanto é 13 - 4?', '9')
insert_question('Quanto é 6 + 9?', '15')
insert_question('Quanto é 17 - 8?', '9')
insert_question('Quanto é 5 + 11?', '16')
insert_question('Quanto é 19 - 3?', '16')
insert_question('Quanto é 9 + 7?', '16')
insert_question('Quanto é 16 - 6?', '10')
insert_question('Quanto é 10 + 10?', '20')
insert_question('Quanto é 11 - 5?', '6')
insert_question('Quanto é 4 + 14?', '18')
insert_question('Quanto é 15 - 9?', '6')
insert_question('Quanto é 3 + 12?', '15')
insert_question('Quanto é 20 - 12?', '8')



