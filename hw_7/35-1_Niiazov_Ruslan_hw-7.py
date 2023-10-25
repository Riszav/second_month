# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3 +
# 2. В БД создать таблицу products +
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию. +
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL) +
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL)
# значением по-умолчанию поля должно быть 0.0 +
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0 +
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров +
# 8. Добавить функцию, которая меняет количество товара по id +
# 9. Добавить функцию, которая меняет цену товара по id +
# 10. Добавить функцию, которая удаляет товар по id +
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
# 12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле 100 сомов и количество которых больше чем 5 и распечатывала бы их в консоли
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием -
# “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
# 14. Протестировать каждую написанную функцию
import sqlite3

def create_connection(db_file):
    """Создает соединение с БД"""
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

def create_table(connection, sql):
    """Создает таблицу"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_employee(connection):
    values = [('Acer Nitro 5', 80000, 20), ('Lenovo Ideapad', 75000, 16), ('Lenovo Ideapad gaming', 79000, 21), ('TUF Gaming', 85000, 18),
              ('Lenovo LV-1233', 38000, 22), ('Acer Aspire 7', 70000, 15), ('DELL WW-124h', 30000, 18), ('ASUS Y1511CDA', 35000, 25),
              ('Maibenben M543', 38000, 12), ('ASUS ZenBook 14', 108000, 22), ('Acer Aspire 5', 60000, 13), ('Acer Aspire 3', 35000, 11),
              ('ASUS Vivobook Go 15', 40000, 11), ('Machenike Machcreator 15', 110000, 19), ('MSI Modern 14', 98000, 25), ]
    for employees in values:
        sql = '''
        INSERT INTO employees 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        try:
            cursor = connection.cursor()
            cursor.execute(sql, employees)
            connection.commit()
        except sqlite3.Error as e:
            print(e)

def update_employee_price(connection, employee_id, new_price):
    sql = '''UPDATE employees SET price = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, employee_id))
    connection.commit()

def update_employee_quantity(connection, employee_id, new_quantity):
    sql = '''UPDATE employees SET quantity = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_quantity, employee_id))
    connection.commit()

def delete_employee(connection, employee_id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (employee_id,))
    connection.commit()

def select_all_employees(connection):
    sql = '''SELECT * FROM employees'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('\nСписок всех товаров:')
    for row in rows:
        print(row)

def select_employer_by_price_and_quntity(connection, price, quantity):
    sql = '''SELECT * FROM employees WHERE price > ? AND  quantity > ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (price, quantity))
    rows = cursor.fetchall()
    print(f'\nСписок товаров у которых цена больше {price}, а количество больше чем {quantity}:')
    for row in rows:
        print(row)

def select_employer_by_product_title(connection, name):
    # value = f'%{name}%'
    sql = '''SELECT * FROM employees WHERE product_title LIKE ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (name,))
    rows = cursor.fetchall()
    print(f'\nСписок товаров в найденных по поиску {name}')
    for row in rows:
        print(row)

connection = create_connection("hw.db")

sql_create_employees_table = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
);
'''

if connection:
    print("Соединение с БД установлено")
    create_table(connection, sql_create_employees_table)
    # select_all_employees(connection)
    # select_employer_by_price_and_quntity(connection, 50000, 16)
    # select_employer_by_product_title(connection, '%Acer%')
    # update_employee_price(connection,31,75000)
    # update_employee_quantity(connection,31, 25)
    # delete_employee(connection,32)

    # create_employee(connection)