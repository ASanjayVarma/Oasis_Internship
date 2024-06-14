# BMI Calculator

Welcome to the BMI Calculator project, a Python-based tool designed to help users calculate their Body Mass Index (BMI) and track their BMI history. This project is one of the three submissions for the Oasis internship certificate.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Contact](#contact)

## Features

- **BMI Calculation:** Calculate BMI based on weight and height.
- **BMI Categorization:** Categorize BMI into underweight, normal weight, overweight, and obesity.
- **History Tracking:** Save and view the history of BMI calculations.
- **Trend Plotting:** Visualize BMI trends over time using matplotlib.
- **User-Friendly Interface:** Simple and intuitive GUI built with Tkinter.

## Installation

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
- MySQL server
- `mysql-connector-python` library for MySQL connection
- `matplotlib` library for plotting trends

### Steps

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/ASanjayVarma/bmi-calculator.git
    cd bmi-calculator
    ```

2. **Install Required Libraries:**

    ```sh
    pip install mysql-connector-python matplotlib
    ```

## Usage

1. **Run the Application:**

    ```sh
    python main.py
    ```

2. **Calculate BMI:**

    - Open the application.
    - Enter your name, weight, and height (in feet and inches).
    - Click the "Calculate BMI" button.
    - The calculated BMI and its category will be displayed.

3. **View History:**

    - Click the "View History" button to see past BMI records.

4. **Plot Trends:**

    - Click the "Plot Trends" button to visualize BMI trends over time.

5. **Clear History:**

    - Click the "Clear History" button to delete all BMI records from the database.

## Database Setup

1. **Set Up MySQL Database:**

    - Start your MySQL server and create a database named `bmi_calculator`.

    ```sql
    CREATE DATABASE bmi_calculator;
    ```

2. **Create the Table:**

    - Use the provided `BMIDB.sql` file to create the necessary table.

    ```sh
    mysql -u username -p bmi_calculator < BMIDB.sql
    ```

    - Replace `username` with your MySQL username.

## Contact

- **Name:** Sanjay Varma
- **Email:** [asanjayvarma18@gmail.com](mailto:asanjayvarma18@gmail.com)
- **GitHub:** [ASanjayVarma](https://github.com/asanjayvarma)
