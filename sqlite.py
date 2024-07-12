import sqlite3

db=sqlite3.connect('Db.sql')
cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
            id INT PRIMARY KEY,
            name TEXT,
            car TEXT
)""")

print(' Choose only one: READ | DELETE | INSERT | SORT | CHOOSE ')
respond=input("What do you want to do?:")


def choice():
    id=int(input('id:'))

    cursor.execute("SELECT * FROM cars WHERE id=?",(id,))

    row=cursor.fetchone()

    if row:
        print(row)
    else:
        print('Not found 404')

def read():
    cursor.execute("SELECT * FROM cars ORDER BY id")
    rows=cursor.fetchall()

    for row in rows:
        print(row)

def sort():
    sort_by = input("Sort by (id, name, car): ")
    cursor.execute(f"SELECT * FROM cars ORDER BY {sort_by}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    db.commit()


def reg():
    id=int(input("Введите id:"))
    name=input("Name:")
    car_name=input('Car name:')
    cursor.execute(f"INSERT INTO cars (id,name,car) VALUES (?,?,?)",(id,name,car_name))
    db.commit()

    cursor.execute("SELECT * FROM cars ORDER BY id")
    rows=cursor.fetchall()

    for row in rows:
        print(row)


def delete():
    id = int(input('id:'))

    cursor.execute("SELECT * FROM cars ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    cursor.execute("DELETE FROM cars WHERE id=?", (id,))
    print('Entry deleted.')
    db.commit()

def update():
    id = int(input('ID:'))
    new_car_name = input("New car name:")

    cursor.execute("UPDATE cars SET car=? WHERE id=?", (new_car_name, id))
    db.commit()

    cursor.execute("SELECT * FROM cars ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

if __name__=='__main__':
    if respond == 'INSERT':
        reg()
    elif respond == 'DELETE':
        delete()
    elif respond == 'UPDATE':
        update()
    elif respond == 'SORT':
        sort()
    elif respond == 'READ':
        read()
    elif respond == 'CHOOSE':
        choice()
        

db.close()