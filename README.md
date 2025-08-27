**Python Playwright Automation Framework** integrated with **Pytest**, **Allure Reporting**, and **GitHub Actions CI/CD**.

---

# 🚀 Playwright Python Automation Framework

This automation framework is built with **Python**, **Playwright**, and **Pytest**, with **Allure** for reporting and **GitHub Actions** for CI/CD integration.

---

## 📁 Framework Structure

```
playwright-python-framework/
│
├── tests/                 # Test cases
│   ├── test_example.py
│   └── ...
│
├── pages/                 # Page Object Model (POM)
│   ├── login_page.py
│   └── ...
│
├── utils/                 # Utility modules
│   ├── constants.py
│   └── test_data.py
│
├── allure-report/               # Allure reports output
│
├── requirements.txt       # Python dependencies
├── pytest.ini             # Pytest configuration
├── conftest.py            # Fixtures
├── .github/workflows/     # GitHub Actions workflows
│   └── ci.yml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Install Python and Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
# Core testing
pytest==7.4.2
pytest-playwright==0.6.0
playwright==1.39.2

# Reporting
allure-pytest==2.10.0

# Optional: for data handling and utilities
pytest-xdist==3.3.1           # Parallel test execution
pytest-rerunfailures==11.1    # Retry failed tests
pytest-html==4.1.1            # HTML reports (optional alongside Allure)

# Environment & Config management
python-dotenv==1.0.1          # Load environment variables
pyyaml==7.0.1                  # YAML config support

# Logging and debugging
loguru==0.7.0                  # Enhanced logging

```

### 3. Install Playwright Browsers

```bash
playwright install
```

### 4. Run Tests Locally

```bash
# Run all tests
pytest tests/

# Run with Allure reporting
pytest tests/ --alluredir=reports/

# Serve Allure report
allure serve reports/
```

---

## 🧩 Pytest Configuration (`pytest.ini`)

```ini
[pytest]
addopts = -v --maxfail=1 --disable-warnings
testpaths = tests
```

---

## 🧑‍💻 Fixtures (`conftest.py`)

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
```

---

## 📊 Reporting with Allure

1. Add the `--alluredir` option when running tests:

```bash
pytest --alluredir=reports/
```

2. Serve the report:

```bash
allure serve reports/
```

---

## 📦 Page Object Model Example

**pages/login_page.py**

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "input#username"
        self.password = "input#password"
        self.login_btn = "button#login"

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
```

**tests/test_login.py**

```python
from pages.login_page import LoginPage

def test_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    page.goto("https://example.com/login")
    login_page.login("user", "password")
    assert page.url == "https://example.com/dashboard"
```

---

## 🛠 GitHub Actions CI/CD Integration

**.github/workflows/ci.yml**

```yaml
name: Python Playwright CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: [3.10]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install

      - name: Run tests with Allure
        run: |
          pytest tests/ --alluredir=reports/

      - name: Upload Allure Report
        uses: actions/upload-artifact@v3
        with:
          name: allure-report
          path: reports/
```

---

## 🔹 Features

- ✅ Playwright Python Automation
- ✅ Page Object Model (POM)
- ✅ Pytest test runner
- ✅ Allure reporting
- ✅ GitHub Actions CI/CD
- ✅ Cross-browser testing support
- ✅ Configurable fixtures and utilities

---

## 📌 How to Use

1. Clone the repository
2. Set up `.venv` and install dependencies
3. Run tests locally or on CI/CD
4. Generate and view Allure reports (pytest tests/ --alluredir=report)
5. Push code to GitHub to trigger GitHub Actions

---
