import sqlite3

class Database:

    def create_database():
        conn = sqlite3.connect('high_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def saveData(score):
        try:
            conn = sqlite3.connect('high_scores.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO scores (score) VALUES (?)', (score,))
            conn.commit()
        except Exception as e:
            print(f"Error saving data: {e}")
        finally:
            conn.close()


    def read_high_scores():
        try:
            conn = sqlite3.connect('high_scores.db')
            cursor = conn.cursor()
            cursor.execute('SELECT score FROM scores ORDER BY score DESC LIMIT 5')
            scores = [row[0] for row in cursor.fetchall()]  # Получаем все записи
            return scores
        except Exception as e:
            print(f"Error reading data: {e}")
            return []
        finally:
            conn.close()