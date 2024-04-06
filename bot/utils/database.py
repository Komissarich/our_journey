import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


class Database:
    def __init__(self, db_name, user, password) -> None:
        self.connection = psycopg2.connect(
            database=db_name, user=user, password=password, port="5432", host="db"
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """ CREATE TABLE IF NOT EXISTS users (
        id serial primary key,
        nickname TEXT UNIQUE,
        age INTEGER,
        town TEXT,
        country TEXT,
        description TEXT,
        photo_id TEXT,
        chat_id TEXT);"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS friends(
        id serial primary key,
        nickname TEXT,
        friend_nickname TEXT);"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS journeys(
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE,
            description TEXT,
            locations TEXT[],
            time_arrive TEXT[],
            time_leave TEXT[]
            )
            """
        )
        self.cursor.close()

    def create_user(self, nickname, age, town, country, descr, photo_id, chat_id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f"INSERT INTO users (nickname, age, town, country, description, photo_id, chat_id) VALUES ('{nickname}', '{age}','{town}','{country}','{descr}','{photo_id}','{chat_id}')"
        )
        self.cursor.close()

    def check_registered(self, chat_id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE chat_id = '{chat_id}'")
        result = self.cursor.fetchall()
        self.cursor.close()
        if len(result) > 0:
            return True
        else:
            return False

    def check_nickname(self, nickname):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE nickname = '{nickname}'")
        result = self.cursor.fetchall()
        self.cursor.close()
        if len(result) > 0:
            return True
        else:
            return False

    def update_nickname(self, oldnick_id, newnick):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f"SELECT nickname FROM users WHERE chat_id = '{oldnick_id}'"
        )
        old_nickname = self.cursor.fetchall()[0][0]
        self.cursor.execute(
            f"UPDATE users SET nickname = '{newnick}' WHERE nickname = '{old_nickname}'"
        )
        self.cursor.execute(
            f"UPDATE friends SET nickname = '{newnick}' WHERE nickname = '{old_nickname}'"
        )
        self.cursor.close()

    def search_by_nickname(self, nickname):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE nickname = '{nickname}'")
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def search_by_city(self, city):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE town = '{city}'")
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def search_by_country(self, country):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE country = '{country}'")
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def show_profile(self, chat_id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE chat_id = '{chat_id}'")
        result = self.cursor.fetchall()[0]

        self.cursor.close()
        return result

    def add_friend(self, chat_id, friend_nickname):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT nickname FROM users WHERE chat_id = '{chat_id}'")
        nickname = self.cursor.fetchall()[0][0]
        print(nickname)
        if nickname != friend_nickname:
            self.cursor.execute(
                f"SELECT * FROM friends WHERE nickname = '{nickname}' AND friend_nickname = '{friend_nickname}'"
            )
            result = self.cursor.fetchall()
            if len(result) > 0:
                pass
            else:
                self.cursor.execute(
                    f"INSERT INTO friends (nickname, friend_nickname) VALUES ('{nickname}', '{friend_nickname}')"
                )
        self.cursor.close()

    def show_friends(self, chat_id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT nickname FROM users WHERE chat_id = '{chat_id}'")
        nickname = self.cursor.fetchall()[0][0]
        self.cursor.execute(
            f"SELECT friend_nickname FROM friends WHERE nickname = '{nickname}'"
        )
        result = self.cursor.fetchall()
        s = ""
        for i in result:
            s += str(i)[1 : len(str(i)) - 2]
            s += ", "

        self.cursor.execute(f"SELECT * FROM users WHERE nickname in ({s[:-2]})")
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def remove_friend(self, chat_id, friend_nickname):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users WHERE chat_id = '{chat_id}'")
        nickname = self.cursor.fetchall()[0][1]
        self.cursor.execute(
            f"DELETE FROM friends  WHERE nickname = '{nickname}' AND friend_nickname = '{friend_nickname}'"
        )

        self.cursor.close()
