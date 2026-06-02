import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
#VARCHAR → Variable-length string (text)
#(25) → Maximum 25 characters allowed

cursor.execute(table_info)

# Insert records
cursor.execute(
    '''INSERT INTO STUDENT VALUES('Akshay','Data Science','A',90)'''
)

cursor.execute(
    '''INSERT INTO STUDENT VALUES('Aryan','Data Science','B',100)'''
)

cursor.execute(
    '''INSERT INTO STUDENT VALUES('Priya','Data Science','A',86)'''
)

cursor.execute(
    '''INSERT INTO STUDENT VALUES('Anam','DEVOPS','A',50)'''
)

cursor.execute(
    '''INSERT INTO STUDENT VALUES('Shreyas','DEVOPS','A',35)'''
)

# Display all records
print("The inserted records are")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# Commit changes
connection.commit()

# Close connection
connection.close()