import MySQLdb

class MysqlDB:
    def con(self):
# Open database connection
        db = MySQLdb.connect("localhost","root","","gowtham" )

# prepare a cursor object using cursor() method
        cursor = db.cursor()

# execute SQL query using execute() method.
        cursor.execute("SELECT * from test")

# Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        for row in data:
#d = row[1]
            ID = row[0]
            name = row[1]
            place = row[2]
            stat = row[3]
            #row = (x for x in row)
            print ID, name, place, stat
#print "Database version : %s " % data
# disconnect from server
        db.close()

db = MysqlDB()
db.con()
