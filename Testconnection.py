import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-2TJD0P0\SQLLAD;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('Select * from Test.dbo.Customer;')
for row in cursor:
    print(row)
