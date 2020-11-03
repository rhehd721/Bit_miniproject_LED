import sqlite3

conn =sqlite3.connect('/home/park/Downloads/chadwick.db')
print("Opened database successfully")

cursor = conn.execute("SELECT yearID FROM Salaries LIMIT 10")

for row in cursor:
    print("yearID=", row[0])


#cursor = conn.execute("SELECT * FROM Salaries LIMIT 10")
#for row in cursor:
#    print("yearID=", row[0])
#    print("teamID=", row[1])
#    print("lgID=", row[2])
#    print("playerID=", row[3])
#    print("salary=",row[4])

print("Operation done successfully")
conn.close()

