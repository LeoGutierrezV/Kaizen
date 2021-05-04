import os
import sqlite3

DB_PATH = str(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db','kaizen.sqlite'))

def get_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_contact():
    try:
        create_tables()
        conn = get_conn(DB_PATH)
        CREATE_TABLE_CONTACT = ''' 
        SELECT * FROM contactos;
        '''
        cur = conn.cursor()
        cur.execute(CREATE_TABLE_CONTACT)
        data = cur.fetchall()
        return data
    except:
        return None



def create_contact(contact):

    create_tables()
    try:
        sql = ''' INSERT INTO contactos (nombre,email,mensaje)
                VALUES(?,?,?); '''
        conn = get_conn(DB_PATH)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, contact)
            conn.commit()
    except:
        print('error')



def create_tables():
    conn = get_conn(DB_PATH)
    with conn:
        CREATE_TABLE_CONTACT = ''' 
        CREATE TABLE IF NOT EXISTS contactos (
            id integer PRIMARY KEY AUTOINCREMENT,
            nombre text NOT NULL,
            email text NOT NULL,
            mensaje text NOT NULL
        );
        '''
        cur = conn.cursor()
        cur.execute(CREATE_TABLE_CONTACT)
        conn.commit()
        


