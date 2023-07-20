import sqlite3

def conn():
    return sqlite3.connect('malumot.db')

def add_data(data: dict, table: str):
    con = conn()
    cur = con.cursor()
    cur.execute(f"""
        insert into {table}(first_name, last_name, username, password, email, is_active, like, dislike, history)
        values
        ('{data['first_name']}', '{data['last_name']}', '{data['username']}', '{data['password']}', '{data['email']}', {data['is_active']}, '{data['like']}', '{data['dislike']}', '{data['history']}')
    """)
    con.commit()

def update(table, part, new_data, username):
    con = conn()
    cur = con.cursor()
    cur.execute(f"""
        update {table}
        set {part}={new_data}
        where `username`='{username}'
    """)
    con.commit()

def delete(table, first_name):
    con = conn()
    cur = con.cursor()
    cur.execute(f"""
        delete from {table} where `first_name`='{first_name}'
    """)
    con.commit()

delete('user', 'Abdulaziz')