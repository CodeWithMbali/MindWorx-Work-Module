import pyodbc

try:
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=localhost\SQLEXPRESS03;"
        "Database=master;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    print("Database connection successful!")

    # WRITE Operation
    cursor.execute("""
        INSERT INTO CUSTOMER (CustomerID, CustomerName)
        VALUES ('C100', 'Mbali Banda')
    """)

    conn.commit()

    print("Customer inserted successfully!")

    # READ Operation
    cursor.execute("""
        SELECT CustomerID, CustomerName
        FROM CUSTOMER
        WHERE CustomerID = 'C100'
    """)

    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()

except Exception as e:
    print("Error:", e)