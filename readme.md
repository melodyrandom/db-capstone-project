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

The entity-relationship (ER) diagram visually represents the database structure, showing the relationships between these entities:
<p>
  <img src="https://github.com/melodyrandom/db-capstone-project/blob/bc82472394eee187d6615ab5cccb70c06b88e93e/ERD.png">
</p>

Forward Engineer tool is used to creates a SQL script that sets up the database structure, including tables, columns, and rules.
Here is the SQL code generated by the Forward Engineer tool:

```sql
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema little_lemon_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema little_lemon_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `little_lemon_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `little_lemon_db` ;

-- -----------------------------------------------------
-- Table `little_lemon_db`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`customers` (
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(100) NOT NULL,
  `ContactNumber` VARCHAR(20) NULL DEFAULT NULL,
  `Email` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`CustomerID`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  UNIQUE INDEX `ContactNumber_UNIQUE` (`ContactNumber` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`staffs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`staffs` (
  `StaffID` INT NOT NULL,
  `FullName` VARCHAR(100) NOT NULL,
  `Role` VARCHAR(100) NOT NULL,
  `Salary` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`StaffID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`bookings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`bookings` (
  `BookingID` INT NOT NULL AUTO_INCREMENT,
  `BookingDate` DATE NOT NULL,
  `CustomerID` INT NOT NULL,
  `TableNumber` INT NULL DEFAULT NULL,
  `StaffID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`BookingID`, `BookingDate`),
  INDEX `staff_id_fk_idx` (`StaffID` ASC) VISIBLE,
  INDEX `booking_customer_id_fk_idx` (`CustomerID` ASC) VISIBLE,
  CONSTRAINT `booking_customer_id_fk`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `little_lemon_db`.`customers` (`CustomerID`),
  CONSTRAINT `staff_id_fk`
    FOREIGN KEY (`StaffID`)
    REFERENCES `little_lemon_db`.`staffs` (`StaffID`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`menuitems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`menuitems` (
  `MenuItemID` INT NOT NULL AUTO_INCREMENT,
  `CourseName` VARCHAR(100) NULL DEFAULT NULL,
  `StarterName` VARCHAR(100) NULL DEFAULT NULL,
  `DessertName` VARCHAR(100) NULL DEFAULT NULL,
  `Drinks` VARCHAR(100) NULL DEFAULT NULL,
  `Sides` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`MenuItemID`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`menus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`menus` (
  `MenuID` INT NOT NULL AUTO_INCREMENT,
  `MenuItemID` INT NOT NULL,
  `MenuName` VARCHAR(100) NOT NULL,
  `Cuisine` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`MenuID`),
  INDEX `menu_item_id_fk_idx` (`MenuItemID` ASC) VISIBLE,
  CONSTRAINT `menu_item_id_fk`
    FOREIGN KEY (`MenuItemID`)
    REFERENCES `little_lemon_db`.`menuitems` (`MenuItemID`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`orders` (
  `OrderID` INT NOT NULL AUTO_INCREMENT,
  `OrderDate` DATE NOT NULL,
  `MenuID` INT NOT NULL,
  `CustomerID` INT NOT NULL,
  `Quantity` INT NOT NULL,
  `TotalCost` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`OrderID`),
  INDEX `menu_id_fk_idx` (`MenuID` ASC) VISIBLE,
  INDEX `order_customer_id_fk_idx` (`CustomerID` ASC) VISIBLE,
  CONSTRAINT `menu_id_fk`
    FOREIGN KEY (`MenuID`)
    REFERENCES `little_lemon_db`.`menus` (`MenuID`),
  CONSTRAINT `order_customer_id_fk`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `little_lemon_db`.`customers` (`CustomerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `little_lemon_db`.`orderdeliverystatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`orderdeliverystatus` (
  `OrderID` INT NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `DevlieryDate` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`OrderID`),
  CONSTRAINT `delivery_order_id_fk`
    FOREIGN KEY (`OrderID`)
    REFERENCES `little_lemon_db`.`orders` (`OrderID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

USE `little_lemon_db` ;

-- -----------------------------------------------------
-- Placeholder table for view `little_lemon_db`.`ordersview`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_db`.`ordersview` (`OrderID` INT, `Quantity` INT, `TotalCost` INT);

-- -----------------------------------------------------
-- procedure GetMaxQuantity
-- -----------------------------------------------------

DELIMITER $$
USE `little_lemon_db`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetMaxQuantity`()
SELECT MAX(Quantity) AS "Max Quantity in Order" FROM ORDERS$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure UpdateBooking
-- -----------------------------------------------------

DELIMITER $$
USE `little_lemon_db`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateBooking`(
IN in_BookingID INT,
IN in_newBookingDate DATE)
BEGIN
	-- Update the booking date for the given booking ID
	UPDATE Bookings
    SET BookingDate = in_NewBookingDate
    WHERE BookingID = in_BookingID;
    
    -- Output message
    SELECT CONCAT("Booking ", in_BookingID, " updated ") AS Confirmation;
    
    END$$

DELIMITER ;

-- -----------------------------------------------------
-- View `little_lemon_db`.`ordersview`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `little_lemon_db`.`ordersview`;
USE `little_lemon_db`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `little_lemon_db`.`ordersview` AS select `little_lemon_db`.`orders`.`OrderID` AS `OrderID`,`little_lemon_db`.`orders`.`Quantity` AS `Quantity`,`little_lemon_db`.`orders`.`TotalCost` AS `TotalCost` from `little_lemon_db`.`orders` where (`little_lemon_db`.`orders`.`Quantity` > 2);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


```


## Booking system ##
A booking system for Little Lemon Restaurant is designed to implement the following functionalities:
- GetMaxQuantity: Displays the maximum ordered quantity in the Orders table
- ManageBooking: Check booking details by Booking Date and Table Number
- UpdateBooking: Update an existing booking date using the Booking ID
- AddBooking: Add new table booking records
- CancelBooking: Cancel or remove existing bookings



## Data Analysis and Dashboard ##
After importing the data into Tableau, further analysis is conducted to gain insights, and an interactive dashboard is developed for easy visualization and exploration of key metrics.
<p>
	<img src=https://github.com/melodyrandom/db-capstone-project/blob/main/little-lemon-dashboard-customers.png.
</p>
<p>
	<img src = https://github.com/melodyrandom/db-capstone-project/blob/main/tableau-dashboard.png>
</p>
