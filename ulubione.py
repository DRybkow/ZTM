import sqlite3

class DB():
    TABLE_NAME = 'ulubione'

    @classmethod
    def wstaw(self,t):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS ulubione (B_ID INTEGER PRIMARY KEY, C text, D text, E text, F text)"
        cursor.execute(create_table)
        query = "INSERT OR IGNORE INTO {table} VALUES(?,?,?,?,?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (t[1],t[2],t[3],t[4],t[5]))
        print('Dodano')
        connection.commit()
        connection.close()

    @classmethod
    def ulubione(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS ulubione (B_ID INTEGER PRIMARY KEY, C text, D text, E text, F text)"
        cursor.execute(create_table)
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append(row)
        connection.commit()
        connection.close()
        return items

    def usun(self, B_ID):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE B_ID=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (B_ID,))
        connection.commit()
        connection.close()
        return print (f'usunięto przystanek z ID: {B_ID}')