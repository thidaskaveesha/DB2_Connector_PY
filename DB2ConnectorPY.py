import pyodbc
import getpass 

def kapiti_db_connection(user, password, ip, sql_query):
    """
    Connect to an IBM i (DB2) database and return the connection status.

    Parameters:
        user (str): Username for the database.
        password (str): Password for the database.
        library (str): Default library to use.
        ip (str): IP address of the IBM i server.
        sql_query (str): query.
    Returns:
        str: Result of the query.
    """
    try:
        # Connection string
        connection_string = (
            f"DRIVER={{iSeries Access ODBC Driver}};"
            f"SYSTEM={ip};"
            f"UID={user};"
            f"PWD={password};"
            f"FORCE_TRANSLATE=0;"
        )
        # Create the connection
        conn = pyodbc.connect(connection_string)
   
        # Test the connection by querying the server
        cursor = conn.cursor()
        cursor.execute(f"""
            {sql_query}
            """)

        result = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        return result
    except Exception as ex:
        result = f"Error: {ex}"
        return result

print("--------------------------------------------------------")
print("Welcome to the DB2 connection module!")
print("This module allows you to connect to the DB2.")
print("This module developed by Thidas Senavirathna.")
print("--------------------------------------------------------")
print("Please enter the following information to connect to the DB2:")
username = input("Enter your DB2 username: ")
password = getpass.getpass("Enter your DB2 password: ")
ip = input("Enter the IP address of the DB2 server: ")
sql_query = input("Enter the SQL query: ")
print("--------------------------------------------------------")
# Call the function
data = kapiti_db_connection(username, password, ip, sql_query)
# Display the result
print(data)
