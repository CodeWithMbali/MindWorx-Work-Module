import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS04;"
    "Database=master;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

while True:

    print("\n STANDARD BANK CUSTOMER SYSTEM")
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":

        customer_id = input("Enter Customer ID: ")
        customer_name = input("Enter Customer Name: ")

        cursor.execute("""
            INSERT INTO CUSTOMER
            (CustomerID, CustomerName)
            VALUES (?, ?)
        """, (customer_id, customer_name))

        conn.commit()

        print("Customer added successfully!")

    elif choice == "2":

        customer_id = input("Enter Customer ID: ")

        cursor.execute("""
            SELECT CustomerID, CustomerName
            FROM CUSTOMER
            WHERE CustomerID = ?
        """, (customer_id))

        result = cursor.fetchone()

        if result:
            print("\nCustomer Found")
            print("ID:", result.CustomerID)
            print("Name:", result.CustomerName)
        else:
            print("Customer not found.")

    elif choice == "3":
        print("Application Closed")
        break

    else:
        print("Invalid option")

conn.close()