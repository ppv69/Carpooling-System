INSERT INTO cars (Car_name, Car_documents, Car_type, Car_colour) VALUES
('Car1', 'Doc1', 'Sedan', 'Blue'),
('Car2', 'Doc2', 'SUV', 'Black'),
('Car3', 'Doc3', 'Hatchback', 'Red');



INSERT INTO trips (trip_name, source, destination, trip_status, schedule, seating_capacity, car_id) VALUES
('My Trip to the Beach', 'San Francisco, CA', 'Los Angeles, CA', 'available', '2023-11-25 10:00:00', 4, 1),
('My Weekend Getaway', 'New York, NY', 'Boston, MA', 'available', '2023-11-25 15:00:00', 2, 2),
('My Business Trip', 'Chicago, IL', 'Dallas, TX', 'available', '2023-11-25 20:00:00', 3, 3);




INSERT INTO feedbacks (rating) VALUES
(1),
(2),
(3),
(4),
(5);






INSERT INTO drivers (Driver_name, Driver_license, Driver_email, Driver_Password, car_id, trip_id) VALUES
('Driver1', 'DL111', 'driver1@example.com',  'password1', 1, 1),
('Driver2', 'DL222', 'driver2@example.com',  'password2', 2, 2),
('Driver3', 'DL333', 'driver3@example.com', 'password3', 3, 3);





INSERT INTO users (user_name, user_email, user_password, trip_id, feedback_id) VALUES
('John Doe', 'johndoe@example.com', 'password123', 1, 1),
('Jane Doe', 'janedoe@example.com', 'password456', 2, 2),
('Peter Jones', 'peterjones@example.com', 'password789', 3, 3);

