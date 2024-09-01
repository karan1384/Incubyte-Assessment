# Library Management System (Assessment)

A command-line interface tool designed for managing a library's collection of books. Users can add new books, borrow books, return borrowed books, and view available books. The application is implemented using Python.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Running the tests](#running-the-tests)
- [Built With](#built-with)
- [Authors](#authors)

## Getting Started

Follow the instructions to get the project running on your local machine for development and testing.

## Prerequisites

- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/karan1384/Incubyte-Assessment.git
   ```

2. Navigate to the project directory:

   ```
   cd Incubyte-Assessment
   ```

3. (Optional) Create a virtual environment to manage dependencies (For Windows):

   ```
   virtualenv env
   cd scripts\
   activate
   cd..
   cd..
   ```

4. Install the required packages:
   ```
   pip install pytest
   ```


## Usage

1. Run the program:

   ```
   python src\library.py
   ```

2. Follow the on-screen instructions to add books, borrow books, return books, and view available books.

3. The program will handle all interactions through the command line, and display the results accordingly.

## Running the tests

To ensure the reliability of the navigation system, unit tests are provided. To run these tests:

`  pytest
 `

For detailed information about each test:

`  pytest -v -rP
 `


## Built With

- [Python](https://www.python.org/) - The programming language used for application development
- [pytest](https://docs.pytest.org/en/stable/) - Testing framework used for unit tests

## Authors

- [Karan Gandhi](https://github.com/karan1384) - L.D. College Of Engineering
