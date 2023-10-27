import sqlite3

def create_connection(db_file):
    """Создает соединение с БД"""
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

def print_cities(connection):
    sql ='''SELECT c.id, c.title FROM cities AS c'''
    cursor = connection.cursor()
    cursor.execute(sql, ())
    connection.commit()
    rows = cursor.fetchall()
    ids = []
    for key, value in rows:
        print(f'{key}. {value}')
        ids.append(key)
    return ids

def employees_in_city(connection, id_city):
    sql = '''SELECT e.first_name,
       e.last_name,
       co.title,
       c.title,
       c.area
  FROM employees AS e
       LEFT JOIN
       cities AS c ON e.city_id = c.id
       LEFT JOIN 
       countries as co ON co.id = c.country_id
       WHERE c.id = ?;'''
    cursor = connection.cursor()
    cursor.execute(sql, (id_city,))
    connection.commit()
    rows = cursor.fetchall()
    for a, b, c, d, e in rows:
        print(f'{a} {b} \033[1m\033[32mСтрана:\033[0m {c} \033[1m\033[32mГород проживания:\033[0m {d} \033[1m\033[32mПлощадь города: \033[0m{e}')
    return

connection = create_connection("hw-8.db")

while True:
    print('\033[1m\033[36mВы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:\033[0m')
    count = print_cities(connection)
    id_city = int(input('\033[1m\033[36mВведите id города:\033[0m'))
    # print(count)
    if id_city == 0:
        print('\033[1m\033[33mЗавершение работы...')
        break
    elif id_city in count:
        employees_in_city(connection, id_city)
        print('\n')
    else:
        print('\033[1m\033[31mТы выбрал несуществующий id!!!\033[0m\n')