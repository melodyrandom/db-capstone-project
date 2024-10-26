# Capstone Project: Little Lemon Restaurant

## About the project ##
This is the capstone project for the Meta Database Engineer Professional Certificate on Coursera. This project involves creating a data model for Little Lemon Restaurant in MySQL and building a booking system. It also includes analyzing data and generating reports using Tableau.

## Database model design ##
The database model for Little Lemon Restuarant includes the following entities:
1. Bookings
2. Customers
3. Menus
4. MenuItems
5. Orders
6. OrderDeliveryStatus
7. Staffs

Entity Relationship Diagram
<p>
  <src="">
</p>

## Booking system ##
A booking system is designed for Little Lemon Restaurant to manage their bookings with the following procedures:

<p>
1. GetMaxQuantity
</p>

```sql

-- Displays the maximum ordered quantity in the Orders table
CREATE PROCEDURE GetMaxQuantity()
SELECT MAX(Quantity) AS "Max Quantity in Order" FROM ORDERS;

```

<p>
2. ManageBooking
</p>

```sql

-- Check booking details
DELIMITER //
CREATE PROCEDURE ManageBooking(
IN inputBookingDate DATE, 
IN inputTableNumber INT
)
BEGIN
	DECLARE booking_status INT;
  SELECT COUNT(*) INTO booking_status
  FROM Bookings
  WHERE BookingDate = inputBookingDate AND TableNumber = inputTableNumber;

  IF booking_status > 0 THEN
		SELECT CONCAT("Table ", inputTableNumber,  " is already booked") AS "Booking status";
	ELSE
		SELECT CONCAT("Table ", inputTableNumber,  " is available") AS "Booking status";
	END IF;
END //
DELIMITER ;

```

<p>
3. UpdateBooking 
</p>

```sql

-- Displays the maximum ordered quantity in the Orders table
DELIMITER //
CREATE PROCEDURE UpdateBooking(
IN in_BookingID INT,
IN in_newBookingDate DATE
)
BEGIN
  -- Update the booking date for the given booking ID
  UPDATE Bookings
  SET BookingDate = in_NewBookingDate
  WHERE BookingID = in_BookingID;

  -- Output message
  SELECT CONCAT("Booking ", in_BookingID, " updated ") AS Confirmation;
END //
DELIMITER ;

```

<p>
4. AddBooking
</p>

```sql

-- Add a new table booking record
DELIMITER //

CREATE PROCEDURE AddBooking(
IN in_BookingID INT,
IN in_CustomerID INT,
IN in_BookingDate DATE,
IN in_TableNumber INT
)
BEGIN
  -- insert a new booking into the Bookings table
  INSERT INTO Bookings (BookingID, CustomerID, BookingDate, TableNumber)
  VALUES (in_BookingID, in_CustomerID, in_BookingDate, in_TableNumber);

  -- Output message
  SELECT "New booking added" AS Confirmation;
END //

DELIMITER ;


```

<p>
5. CancelBooking
</p>

```sql

-- Cancel or remove a booking
DELIMITER //
CREATE PROCEDURE CancelBooking(
IN in_BookingID INT
)
BEGIN
  -- Delete booking with the specified booking ID
  DELETE FROM Bookings WHERE BookingID = in_BookingID;

  -- Output message
  SELECT CONCAT("Booking ", in_BookingID, " deleted ") AS Confirmation;
END //
DELIMITER ;


```
