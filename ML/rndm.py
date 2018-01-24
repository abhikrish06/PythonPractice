# from mnist import MNIST
# import random
#
# # mndata = MNIST(C:/Users/KRISHNA/Downloads/train-images-idx3-ubyte)
# mndata = MNIST('ML_data_csv/')
# # images, labels = mndata.load_training()
# images, labels = mndata.load_testing()
#
# index = random.randrange(0, len(images))  # choose an index ;-)
# print(mndata.display(images[index]))

# https://docs.python.org/2/library/sqlite3.html#module-sqlite3

import sqlite3
murcon = sqlite3.connect(':memory')
import csv
import pandas as pd

murdersdf = pd.read_csv('https://raw.githubusercontent.com/colaberry/538data/master/murder_2016/murder_2015_final.csv')
murdersdf.head(5)
# renaming columns as SQL columns cannot start with a number
murdersdf.columns = ['city','state','murders_2014','murders_2015','change']
murdersdf.to_sql(name='murderstable',con=murcon,if_exists='replace',index=False)

murcur = murcon.cursor()
murcur.execute('select * from murderstable LIMIT 5') # LIMIT to select only certian no. of rows
queryone = murcur.fetchall() # instead of LIMIT we can use murcur.fetchall()[0:5] to print 5 rows
print(queryone)

print(pd.read_sql_query('select * from murderstable LIMIT 5'))

try:
    murcur.execute("""CREATE TABLE murderstabletwo (
                      city TEXT,
                      state TEXT,
                      murders_2014 INTEGER,
                      murders_2015 INTEGER,
                      change INTEGER)""")
except Exception as e:
    print(e)

# read table using for
for i in murcur.execute('select * from murderstable order by murders_2015 desc limit 5'):
    print(i)
# alternate way to execute above for loop query
murcur.execute("SELECT * FROM murderstable ORDER BY murders_2015 DESC LIMIT 5")
topfive = murcur.fetchall()
print(topfive)

# insert into a table
murcur.executemany('INSERT INTO murderstabletwo VALUES (?,?,?,?,?)', topfive)
murcur.execute("SELECT * FROM murderstabletwo")
querytwo = murcur.fetchall()
print(querytwo)