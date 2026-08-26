import pyodbc


def connect_to_database():
    """
    Establish connection to SQL Server database.
    """
    return pyodbc.connect(
        "Driver={SQL Server};"
        "Server=localhost\\SQLEXPRESS04;"
        "Database=master;"
        "Trusted_Connection=yes;"
    )


def add_customer(cursor, conn):
    """
    Add a new customer to the CUSTOMER table.
    """
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")

    cursor.execute("""
        INSERT INTO CUSTOMER
        (CustomerID, CustomerName)
        VALUES (?, ?)
    """, (customer_id, customer_name))

    conn.commit()
    print("Customer added successfully!")


def view_customer(cursor):
    """
    Retrieve a customer using their Customer ID.
    """
    customer_id = input("Enter Customer ID: ")

    cursor.execute("""
        SELECT CustomerID, CustomerName
        FROM CUSTOMER
        WHERE CustomerID = ?
    """, (customer_id,))

    result = cursor.fetchone()

    if result:
        print("\nCustomer Found")
        print(f"ID: {result.CustomerID}")
        print(f"Name: {result.CustomerName}")
    else:
        print("Customer not found.")


def view_all_customers(cursor):
    """
    Display all customers in the database.
    """
    cursor.execute("""
        SELECT CustomerID, CustomerName
        FROM CUSTOMER
    """)

    results = cursor.fetchall()

    if results:
        print("\nCUSTOMER LIST")
        print("-" * 30)

        for customer in results:
            print(f"ID: {customer.CustomerID} | Name: {customer.CustomerName}")
    else:
        print("No customers found.")


def display_menu():
    """
    Display application menu.
    """
    print("\nSTANDARD BANK CUSTOMER SYSTEM")
    print("1. Add Customer")
    print("2. View Customer")
    print("3. View All Customers")
    print("4. Exit")


def main():
    """
    Main application entry point.
    """
    conn = connect_to_database()
    cursor = conn.cursor()

    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_customer(cursor, conn)

        elif choice == "2":
            view_customer(cursor)

        elif choice == "3":
            view_all_customers(cursor)

        elif choice == "4":
            print("Application Closed")
            break

        else:
            print("Invalid option. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
