import sqlite3

# Создание базы данных и таблицы
def create_table():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_title TEXT NOT NULL,
                        price DECIMAL(10,2) NOT NULL DEFAULT 0.0,
                        quantity INTEGER NOT NULL DEFAULT 0
                    )''')
    conn.commit()
    conn.close()

# Добавление 15 товаров в БД
def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    products = [
        ('Шишки еловые', 150.50, 10),
        ('Шоколад молочный', 75.99, 20),
        ('Молоко 2.5%', 45.25, 30),
        ('Картофель свежий', 30.00, 50),
        ('Сок апельсиновый', 90.75, 15),
        ('Печенье овсяное', 65.30, 25),
        ('Сыр Чеддер', 120.80, 12),
        ('Мыло детское', 25.99, 40),
        ('Масло оливковое', 200.00, 8),
        ('Чай черный', 35.60, 60),
        ('Кофе растворимый', 80.15, 18),
        ('Шампунь для волос', 55.75, 22),
        ('Зубная паста', 40.50, 35),
        ('Маска для лица', 90.00, 14),
        ('Пакеты для мусора', 10.70, 100)
    ]
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

# Изменение количества товара по id
def update_quantity(id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, id))
    conn.commit()
    conn.close()

# Изменение цены товара по id
def update_price(id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, id))
    conn.commit()
    conn.close()

# Удаление товара по id
def delete_product(id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Вывод всех товаров из БД
def print_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Вывод товаров, дешевле 100 сом и количеством больше 5 штук
def print_filtered_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Поиск товаров по названию
def search_products_by_name(name):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%'+name+'%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Тестирование функций
create_table()
add_products()
update_quantity(2, 25)
update_price(5, 95.50)
delete_product(13)
print_all_products()
print_filtered_products()
search_products_by_name('мыло')
