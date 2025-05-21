from utlis.db import curr, conn
from tabulate import tabulate

while True:
    category = input("Qaysi kategoriya?: ")
    with conn:
        sql_quary = f""" SELECT c.name, p.name, p.description, p.price, p.discount_precent, p.stock, p.unit, p.weight, p.dimensions, p.size, p.manufactured_date, p.expiry_date  FROM category c JOIN products p ON c.id = p.category_id WHERE c.name like '{category}%' """
        datas = curr.execute(sql_quary).fetchall()

    headers = ['Category', 'Product', 'Description', 'Price', 'Discount_precent', 'Stock', 'Unit', 'Weight', 'Dimenstion', 'Size',  'Manufactured Date', 'Expiry Date']
    print(tabulate(datas, headers, 'grid'))


    