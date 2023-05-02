
from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

    cursor.execute('''
        drop table if exists exercises;
        ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text,
            created timestamp
        );
    ''')
    connection.commit()

    cursor.execute('''
        create table exercises (
            name text primary key
        );
    ''')

    connection.commit()

    cursor.execute('''
        create table routines (
            id integer primary key,
            date date,
            exercise text,
            sets integer,
            reps integer,
            kilos integer

        );
    ''')
    connection.commit()


def initialize_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        insert into exercises
            (name) values ('deadlift')
        
        ''')
    connection.commit()

    cursor.execute('''
        insert into exercises
            (name) values ('bench press')
        ;
    ''')
    connection.commit()

    cursor.execute('''
        insert into exercises 
            (name) values ('squat')
        ;
    ''')
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    initialize_tables(connection)

if __name__ == "__main__":
    initialize_database()
