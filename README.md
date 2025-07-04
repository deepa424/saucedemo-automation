
# Saucedemo Automation Project

This repository contains an automation testing project for the [Saucedemo](https://www.saucedemo.com) e-commerce demo website. The project is implemented using **Python**, **Selenium WebDriver**, and **PyTest**.

---

## Objective

To perform automated testing on key user functionalities of the Saucedemo web application, such as login, cart operations, and logout, ensuring they work as expected.

---

## Test Cases Covered

| Test Case         | Description                                      |
|------------------|--------------------------------------------------|
| Valid Login      | Login with valid credentials                     |
| Invalid Login    | Login attempt using incorrect credentials        |
| Add to Cart      | Add an item to the cart and verify the cart page |
| Logout           | Logout from the application                      |

---

## Technologies Used

- Python 3.11
- Selenium WebDriver
- PyTest
- ChromeDriver

---

## Project Structure

```

saucedemo\_automation\_project/
│
├── drivers/                     # ChromeDriver executable
├── screenshots/                 # Captured screenshots of failed test cases
├── tests/
│   ├── test\_login.py            # Valid login test
│   ├── test\_invalid\_login.py    # Invalid login test
│   ├── test\_cart.py             # Add to cart test
│   └── test\_logout.py           # Logout test
├── conftest.py                  # Common PyTest fixtures (browser setup/teardown)
└── README.md                    # Project documentation

```

---

## How to Run the Tests

1. Install the required packages:

```

pip install selenium pytest

```

2. Ensure the ChromeDriver executable is placed inside the `drivers/` folder and matches your Chrome browser version.

3. Run all test cases:

```

pytest tests/

```

To run a specific test file:

```

pytest tests/test\_cart.py

```

---

## Screenshots

Any test failure will trigger a screenshot to be captured and saved inside the `screenshots/` directory with a timestamp.

---

## Author

**Name:** Deepa S  
**Location:** Bangalore, India  
**Email:** deepachitra407@gmail.com  
**GitHub:** [github.com/deepa424](https://github.com/deepa424)

---

## License

This project is provided under the MIT License. You are free to use, modify, and distribute it with proper attribution.
