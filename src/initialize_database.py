from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    #connection.commit()
    cursor.execute('''
        drop table if exists exercises;
        ''')
    #connection.commit()
    cursor.execute('''
        drop table if exists routines;
        ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id integer primary key,
            username text,
            password text,
            created timestamp
        )
    ''')
    #connection.commit()

    cursor.execute('''
        create table exercises (
            id integer primary key,
            name text,
            username text
        )
    ''')

    #connection.commit()

    cursor.execute('''
        create table routines (
            id integer primary key,
            username,
            date date,
            exercise text,
            sets integer,
            reps integer,
            kilos integer
        )
    ''')
    connection.commit()


def initialize_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        insert into users
            (username, password) values ('qwerty', '1234')
        ''')
    cursor.execute('''
        insert into exercises
            (name, username) values ('deadlift', 'qwerty')
        ''')
    cursor.execute('''
        insert into exercises
            (name, username) values ('bench press', 'qwerty')
    ''')
    cursor.execute('''
        insert into exercises 
            (name, username) values ('squat', 'qwerty')
    ''')
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    initialize_tables(connection)

if __name__ == "__main__":
    initialize_database()
