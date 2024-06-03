# Secure eCommerce Application

## Description

This project is a secure eCommerce application designed to protect against the OWASP Top 10 and CWE Top 25 security vulnerabilities. The application allows customers to create accounts, log in, search for and purchase products, while administrators can manage users, logs, and products. The system supports multiple users simultaneously and complies with GDPR and The Payment Services Regulations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and set up the secure eCommerce application, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/dev-web3js/secure_app.git
   cd secure_app
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv env
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```sh
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```

4. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory of the project and add the necessary environment variables. Example:

   ```sh
   FLASK_APP=app
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   MAIL_SERVER=smtp.mailtrap.io
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your_mailtrap_username
   MAIL_PASSWORD=your_mailtrap_password
   ```

6. **Run the database migrations**:
   ```sh
   flask db upgrade
   ```

## Usage

To run the application, follow these steps:

1. **Start the Flask application**:

   ```sh
   flask run
   ```

2. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

3. **Run tests**:
   To run the tests and generate reports, execute:
   ```sh
   pytest > test_reports/pytest_report.txt
   pylint app.py > test_reports/pylint_report.txt
   flake8 app.py > test_reports/flake8_report.txt
   ```

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```sh
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes and commit them**:
   ```sh
   git commit -m "Add some feature"
   ```
4. **Push to the branch**:
   ```sh
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License.
