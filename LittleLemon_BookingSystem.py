# Import MySQL Connector/Python
import mysql.connector as connector
from mysql.connector import errorcode


# Establish connection
def create_connection():
    try:
        connection = connector.connect(user="root", password="yasminrandom", database="little_lemon_db")
        return connection  # Return the connection object

    except connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Connection user or password are incorrect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


# Get maximum quantity from Order table
def get_max_quantity():
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.callproc('GetMaxQuantity')

        for result in cursor.stored_results():
            print(result.fetchone())

    finally:
        cursor.close()
        connection.close()


# Manage booking
def manage_booking(booking_date, table_number):
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.callproc("ManageBooking",(booking_date, table_number))

        for result in cursor.stored_results():
            print(result.fetchall())

    finally:
        cursor.close()
        connection.close()
        

#Update booking
def update_booking(booking_id, booking_date):
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.callproc("UpdateBooking", (booking_id, booking_date))
        for result in cursor.stored_results():
            print(result.fetchall())
   
    finally:
        cursor.close()
        connection.close()

def add_booking(booking_id, customer_id, booking_date, table_number):
    connection = create_connection()
    if connection is None:
        return

    try:
        with connection.cursor() as cursor:
            cursor.callproc("AddBooking", (booking_id, customer_id, booking_date, table_number))
            
            connection.commit()

            for result in cursor.stored_results():
                print(result.fetchall())

    except connector.Error as err:
            print("Error adding booking: ", err)
   
    finally:
        connection.close()       


# Cancel booking
def cancel_booking(booking_id):
    connection = create_connection()  
    if connection is None:
        return

    try:

        with connection.cursor() as cursor:
            cursor.callproc("CancelBooking", (booking_id,))
        
        connection.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except connector.Error as err:
        print("Error cancelling booking:", err)

    finally:
        connection.close()


# Create the connection
connection = create_connection()

# If the connection was successful, add a booking
if connection:
    #get_max_quantity()
    #manage_booking("2022-10-11",5)
    #update_booking(12,"2022-10-16")
    #add_booking(13, 10, "2022-10-31", 5)
    cancel_booking(12)

