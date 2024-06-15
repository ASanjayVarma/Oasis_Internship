CREATE DATABASE bmi_calculator;
CREATE USER 'bmicalcuser'@'localhost' IDENTIFIED BY 'drowsydreamy';
GRANT ALL PRIVILEGES ON bmi_calculator.* TO 'bmicalcuser'@'localhost';
FLUSH PRIVILEGES;
USE bmi_calculator;
CREATE TABLE bmi_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    weight FLOAT,
    height FLOAT,
    bmi FLOAT,
    category VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);