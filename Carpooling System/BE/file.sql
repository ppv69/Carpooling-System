CREATE DATABASE carpool;
use carpool;

SET SQL_LOG_BIN = 0;
-- Table: drivers
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_name VARCHAR(255),
    driver_license VARCHAR(255)  NOT NULL,
    driver_email VARCHAR(255),
    driver_password VARCHAR(255),
    car_id INT,
    trip_id INT
);

-- Table: users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255),
    user_email VARCHAR(255),
    user_password VARCHAR(255),
    trip_id INT,
    feedback_id INT
);

-- Table: trips
CREATE TABLE trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(255) DEFAULT 'my trip',
    source VARCHAR(255),
    destination VARCHAR(255),
    trip_status ENUM ('available','full','completed') NOT NULL DEFAULT 'available',
    schedule VARCHAR(40),
    seating_capacity INT CHECK (seating_capacity > -1),
    car_id INT
);

-- Table: cars
CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    car_name VARCHAR(255),
    car_documents VARCHAR(255),
    car_type VARCHAR(255),
    car_colour VARCHAR(255)
);

-- Table: feedbacks
CREATE TABLE feedbacks (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    rating INT CHECK (rating >= 0 AND Rating <= 5)
);

-- Adding relations:
ALTER TABLE drivers
ADD CONSTRAINT carid 
FOREIGN KEY (car_id) REFERENCES cars(car_id) on delete cascade on update cascade;

ALTER TABLE drivers
ADD CONSTRAINT tripid1 
FOREIGN KEY (trip_id) REFERENCES trips(trip_id) on delete cascade on update cascade;

ALTER TABLE users
ADD CONSTRAINT tripid2 
FOREIGN KEY (trip_id) REFERENCES trips(trip_id) on delete cascade on update cascade;

ALTER TABLE users
ADD CONSTRAINT feedback
FOREIGN KEY (feedback_id) REFERENCES feedbacks(feedback_id) on delete cascade on update cascade;

ALTER TABLE trips
ADD CONSTRAINT car
FOREIGN KEY (car_id) REFERENCES cars(car_id) on delete cascade on update cascade;




delimiter //
CREATE TRIGGER decrement_seating_capacity_1
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    UPDATE trips
    SET seating_capacity = seating_capacity - 1
    WHERE trip_id = NEW.trip_id;
END;
//

CREATE TRIGGER update_trip_status
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    UPDATE trips
    SET trip_status = 'full'
    WHERE trip_id = NEW.trip_id AND seating_capacity = 0;
END;
//

CREATE PROCEDURE rm_user_trip(
    IN p_user_id INT,
    IN p_trip_id INT
)
BEGIN
    DECLARE user_exists INT;

    SELECT COUNT(*) INTO user_exists FROM users WHERE user_id = p_user_id AND trip_id = p_trip_id;

    IF user_exists > 0 THEN
        
        UPDATE users
        SET trip_id = NULL
        WHERE user_id = p_user_id AND trip_id = p_trip_id;

        UPDATE trips
        SET trip_status = 'available',
            seating_capacity = seating_capacity + 1
        WHERE trip_id = p_trip_id;
    END IF;
END //

CREATE PROCEDURE add_user_trip(
    IN p_user_id INT,
    IN p_trip_id INT
)
BEGIN
    DECLARE capacity INT;
    DECLARE intable INT;

    SELECT COUNT(*) INTO intable FROM USERS WHERE trip_id IS NOT NULL;

    IF intable =0 THEN

            UPDATE users
            SET trip_id = p_trip_id
            WHERE user_id = p_user_id;

            UPDATE trips
            SET seating_capacity = seating_capacity - 1
            WHERE trip_id = p_trip_id;

            SELECT seating_capacity INTO capacity FROM trips WHERE trip_id = p_trip_id;
            IF capacity = 0 THEN
                update trips set trip_status='full' where trip_id = p_trip_id;
            END IF;
    END IF;
END //

CREATE PROCEDURE add_user_feedback(
    IN p_trip_id INT,
    IN p_user_id INT,
    IN p_feedback_id INT
)
BEGIN
    DECLARE v_is_complete INT;
    DECLARE intable INT;

    SELECT COUNT(*) INTO intable FROM USERS WHERE feedback_id IS NOT NULL;
    
    IF intable=0 THEN 

        SELECT COUNT(*) INTO v_is_complete FROM trips WHERE trip_id = p_trip_id AND trip_status = 'completed';
        IF v_is_complete > 0 THEN
            UPDATE users
            SET feedback_id = p_feedback_id
            WHERE user_id = p_user_id;
        END IF;
    END IF;
END //

CREATE PROCEDURE rm_user_feedback(
    IN p_user_id INT,
    IN p_feedback_id INT
)
BEGIN
    DECLARE feedback_exists INT;

    SELECT COUNT(*) INTO feedback_exists FROM users WHERE user_id = p_user_id AND feedback_id = p_feedback_id;

    IF feedback_exists > 0 THEN
        
        UPDATE users
        SET feedback_id = NULL
        WHERE user_id = p_user_id AND feedback_id = p_feedback_id;
    END IF;
END //


CREATE PROCEDURE add_driver_trip(
    IN p_driver_id INT,
    IN p_trip_id INT
)
BEGIN
    DECLARE intable INT;
    SELECT COUNT(*) INTO intable FROM DRIVERS WHERE trip_id IS NOT NULL;
    IF intable=0 THEN
        UPDATE drivers
        SET trip_id = p_trip_id
        WHERE driver_id = p_driver_id;
    END IF;    
END //

CREATE PROCEDURE add_driver_car(
    IN p_driver_id INT,
    IN p_car_id INT
)
BEGIN
    DECLARE intable INT;

    SELECT COUNT(*) INTO intable FROM DRIVERS WHERE car_id IS NOT NULL;
    IF intable=0 THEN
        UPDATE drivers
        SET car_id = p_car_id
        WHERE driver_id = p_driver_id;
    END IF;
END //

CREATE PROCEDURE trip_complete(
    IN p_trip_id INT
)
BEGIN
    DECLARE intable INT;

    SELECT COUNT(*) INTO intable FROM TRIPS WHERE trip_id IS NOT NULL;

    IF intable=0 THEN

        UPDATE trips
        SET trip_status = 'completed'
        WHERE trip_id = p_trip_id;
    END IF;
END //

CREATE PROCEDURE rm_driver_trip(
    IN p_driver_id INT,
    IN p_trip_id INT
)
BEGIN
    DECLARE driver_exists INT;

    SELECT COUNT(*) INTO driver_exists FROM drivers WHERE driver_id = p_driver_id AND trip_id = p_trip_id;

    IF driver_exists > 0 THEN
        
        UPDATE drivers
        SET trip_id = NULL
        WHERE driver_id = p_driver_id AND trip_id = p_trip_id;
    END IF;
END //

CREATE PROCEDURE rm_driver_car(
    IN p_driver_id INT,
    IN p_car_id INT
)
BEGIN
    DECLARE driver_exists INT;

    SELECT COUNT(*) INTO driver_exists FROM drivers WHERE driver_id = p_driver_id AND car_id = p_car_id;

    IF driver_exists > 0 THEN
        
        UPDATE drivers
        SET car_id = NULL
        WHERE driver_id = p_driver_id AND car_id = p_car_id;
    END IF;
END //

CREATE PROCEDURE add_trip_car(
    IN p_trip_id INT,
    IN p_car_id INT
)
BEGIN
    DECLARE intable INT;

    SELECT COUNT(*) INTO intable FROM TRIPS WHERE car_id IS NOT NULL;
    IF intable=0 THEN

        UPDATE trips
        SET car_id = p_car_id
        WHERE trip_id = p_trip_id;
    END IF;
END //

CREATE PROCEDURE rm_trip_car(
    IN p_trip_id INT,
    IN p_car_id INT
)
BEGIN
    DECLARE trip_exists INT;

    SELECT COUNT(*) INTO trip_exists FROM trips WHERE trip_id = p_trip_id AND car_id = p_car_id;

    IF trip_exists > 0 THEN
        
        UPDATE trips
        SET car_id = NULL
        WHERE trip_id = p_trip_id AND car_id = p_car_id;
    END IF;
END //


CREATE FUNCTION get_average_trip_rating(p_trip_id INT)
    RETURNS DECIMAL(3,2)
    DETERMINISTIC
    BEGIN
        DECLARE avg_rating DECIMAL(3,2);
        
        SELECT AVG(f.rating) INTO avg_rating
        FROM feedbacks f
        INNER JOIN users u ON f.feedback_id = u.feedback_id
        WHERE u.trip_id = p_trip_id;
        
        RETURN COALESCE(avg_rating, 0);
    END;
//
delimiter ;


