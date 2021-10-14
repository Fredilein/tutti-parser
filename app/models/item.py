import mysql.connector
from connection import db

# Color codes for pretty print in terminal
BOLD = '\033[1m'
END = '\033[0m'


class Item:
    def __init__(self, json_item, q_id):
        self.id = json_item['id']
        self.query_id = q_id
        self.title = json_item['subject']
        self.description = json_item['body']
        self.price = json_item['price'].split(' ')[-1]  # There's a space in the price for whatever reason

    def pretty_print(self):
        # Output to terminal (for debugging)
        print(f'\n{BOLD}{self.title}{END}')
        print(f'{self.description}')
        print(f'{self.price}\n')

    def to_telegram_msg(self):
        pretty_description = self.description
        pretty_description.replace('\n', ',')
        return f'<a href="https://www.tutti.ch/go/vi/{self.id}"><b>{self.title}</b></a>\n<i>{pretty_description}</i>\n🏷 <b>{self.price} CHF</b>'

    def insert_into_db(self):
        """
        Inserts Item into database if not already there.
        :return: True if item is not stored yet, False otherwise
        """
        if self.exists_in_db():
            return False

        cursor = db.cursor()
        sql = 'INSERT INTO items (TuttiId, QueryId, Title, Description, Price) VALUES (%s, %s, %s, %s, %s)'
        val = (self.id, self.query_id, self.title, self.description, self.price)
        try:
            cursor.execute(sql, val)
            db.commit()
        except mysql.connector.Error as err:
            print(f'Err: {err}')
            db.rollback()
            return False

        return True

    def exists_in_db(self):
        cursor = db.cursor()
        sql = 'SELECT * FROM items WHERE TuttiId = %s'
        val = (self.id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        if len(result) > 0:
            return True

        return False
