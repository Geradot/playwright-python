# Playwright Python Test Automation Framework

## Project Description

This is a comprehensive test automation framework built with Playwright for Python, designed to test the [AutomationExercise](https://automationexercise.com) web application. The framework follows the Page Object Model (POM) design pattern and implements component-based architecture for better code reusability and maintainability.

### Key Features

- **Page Object Model (POM)**: Clean separation of page logic and test code
- **Component-Based Architecture**: Reusable UI components for common elements
- **Data-Driven Testing**: YAML-based test data management
- **Modular Structure**: Organized test suites for different functionality areas
- **Pytest Integration**: Leverages pytest fixtures and plugins for enhanced testing capabilities
- **Cross-Browser Support**: Chromium browser support via Playwright (easily extensible to Firefox and WebKit)

## Requirements

- **Python**: 3.10 or higher
- **Operating System**: Windows, macOS, or GNU/Linux
- **Dependencies**: Listed in `requirements.txt`

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/Geradot/playwright-python.git
cd playwright-python
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```powershell
playwright install chromium
```

Or install all browsers:

```powershell
playwright install
```

## Running Tests

### Run All Tests

```powershell
pytest
```

### Run Specific Test File

```powershell
pytest tests/test_register_and_login.py
```

### Run Tests with Verbose Output

```powershell
pytest -vv -s --tb="short"
```

### Run Tests in Headed Mode (Visible Browser)

```powershell
pytest --headed
```

### Run Tests with Specific Browser

```powershell
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Run Tests in Parallel

```powershell
pytest -n auto
```

### Run Tests with HTML Report

```powershell
pytest --html=report.html --self-contained-html
```

### Run Specific Test by Name

```powershell
pytest -k "test_name"
```

### Run Tests with Screenshots on Failure

```powershell
pytest --screenshot on
```

### Run Tests with Video Recording

```powershell
pytest --video on
```

## Test Categories

- **test_register_and_login.py** - User registration and authentication tests
- **test_products_and_cart.py** - Product browsing and shopping cart tests
- **test_other.py** - Miscellaneous functionality tests

## Configuration

The framework uses pytest fixtures for configuration:

- **base_url**: Configured in `config/conftest.py` (default: https://automationexercise.com)
- **Browser context**: Session-scoped browser context for efficient test execution
- **Page fixture**: Function-scoped page instances for test isolation

## Test Data

Test data is managed through YAML files in the `data/` directory and loaded via the `data_loader` utility. This approach provides:

- Easy data maintenance
- Separation of test logic and test data
- Support for multiple user profiles and test scenarios
