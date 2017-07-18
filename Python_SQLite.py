import sqlite3

from Python_SQLite_Employee_Class import Employee

"With this variable we create a connection object to store/work with our database"
"Our database can be either a file or in memory database"
"For in memory database we use -> :memory: as our argumant as bellow"
# con = sqlite3.connect(":memory:")

"For storing/working with a file we use the name of that file:"
con = sqlite3.connect("employee.db")

"For executing SQL commands we need a cursor as below:"
c = con.cursor()


"Dock string: writing a string in many lines"


"Creating a table"
"""SQL command:
CREATE TABLE table-name (
column-name-1 data-type-1,
column-name-2 data-type-2,
)
"""
"We cannot create another table with this name again, it will create error: sqlite3.OperationalError: table employee already exists"
"Because of this I commented out this part"
# c.execute("""CREATE TABLE employee (
# 	first text,
# 	last text,
# 	pay integer
# 	)""")

"Adding data to our database"
"""SQL command:
INSERT INTO table-name VALUES ('Corey', 'Schafer', 50000)
"""
# c.execute("INSERT INTO employee VALUES ('Corey', 'Schafer', 50000)")


"Query data"
"""SQL command
SELECT * FROM table-name WHERE last='Schafer'
"""
"Select commands doesnt need to be committed"
c.execute("SELECT * FROM employee WHERE last='Schafer'")

"Based on the query that we need we should use one these fetch commands"
# c.fetchone()
# c.fetchmany(s)
# c.fetcall()

print(c.fetchone())

"Difference between fetchone and fetchall"
"It returns a list"
c.execute("SELECT * FROM employee WHERE last='Schafer'")
print(c.fetchall())

"query for a non existing record"
c.execute("SELECT * FROM employee WHERE last='varfan'")
print(c.fetchone())



""
"Working with classes and objects"
""

emp1 = Employee('John','Doe',80000)
emp2 = Employee('Sara', 'Doe', 90000)

"First way to insert information into database"
"the question marks are place holders for the objects properties"
c.execute("INSERT INTO employee VALUES (?,?,?)", (emp1.first, emp1.last, emp1.pay))
c.execute("SELECT * FROM employee WHERE first=?",('John',))
print (c.fetchone())

"Second way to insert information into database"
c.execute("INSERT INTO employee VALUES (:first, :last, :pay)",
	{'first':emp2.first, 'last' :emp2.last, 'pay' :emp2.pay})
c.execute("SELECT * FROM employee WHERE first=:first",{'first': 'Sara'})

print (c.fetchone())

"Because I iserted the data many times to the database now we have many records with the same data"
print (c.fetchall())




"Committing the changes to database"
con.commit()

"Closing the database"
con.close()