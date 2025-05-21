import sqlite3
url=r'D:\MadinaBackEnd\Library.DB'
conn = sqlite3.connect(url)
curr = conn.cursor()

# sql_quary = 'SELECT * FROM Library'
# datas = curr.execute(sql_quary).fetchall()
# for data in datas:
#     print(data)


#who = input("Kitob qidiruv: ")
#sql_quary = f"SELECT id, title, author FROM BOOKS WHERE title='{who}';"
#data = curr.execute(sql_quary).fetchall()
#for dt in data:
    #print(f"id: {dt[0]}, title: {dt[1]}, author: {dt[2]}")


#who = input("Kitob qidiruv harf boyicha: ")
#sql_quarys = f"SELECT * FROM BOOKS WHERE title like '{who}%';"
#data = curr.execute(sql_quarys).fetchall()
#for dt in data:
    #print(f"id: {dt[0]}, title: {dt[1]}, author: {dt[2]}")



#title= input("title?: ")
#author = input("author?: ")
#year = input("year?: ")
#genre = input("genre?: ")
#sql_quary="""INSERT INTO BOOKS (title, author, year, genre)
#VALUES ('%s', '%s', '%s', '%s');""" %(title, author, year, genre)

#curr.execute(sql_quary)
#conn.commit()
#curr.close()
#print("Ma'lumot saqlandi!")

#
# def insert_books(title, author, year, genre):
#     sql_quary = f"""INSERT INTO BOOKS (title, author, year, genre)
# VALUES ('{title}', '{author}', '{year}', '{genre}');
# """
# curr.execute(sql_quary)
# conn.commit()
# curr.close()
# print('Malumot saqlandi')
#
# def update_books(id):
#     sql_quary=id
#


