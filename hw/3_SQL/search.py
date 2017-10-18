import mysql.connector
import sys

def search(key):
    cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='sakila')  
    cursor = cnx.cursor()
    catename = key.capitalize()
    query = "select count(f.film_id) from film f, film_category f_c, category c where c.name ='%s' AND c.category_id = f_c.category_id AND f_c.film_id = f.film_id" %(catename)
    cursor.execute(query)
    for number in cursor:
        print number[0]
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    search(sys.argv[1])