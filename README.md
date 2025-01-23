Price Tracker Web Application

A Flask-based web application that allows users to track product prices on Amazon, store price thresholds, and receive notifications when the price drops below the desired value. The app leverages web scraping with BeautifulSoup and lxml, dynamic data retrieval with Selenium, and SMS notifications with Twilio.

Features

Track Prices: Add product URLs and desired price thresholds to monitor price changes.

Web Scraping: Use BeautifulSoup and lxml to fetch product details like name and price from Amazon.

Dynamic Price Fetching: Employ Selenium for real-time price updates when static scraping fails.

CSV Storage: Save product details, URLs, and thresholds locally in a CSV file.

Notifications: Get SMS alerts for price drops via Twilio integration.

Responsive Interface: Simple HTML templates with Flask to manage user interaction.

Installation

Prerequisites

Python 3.7+

Pip (Python package manager)

Google Chrome and ChromeDriver

Twilio account for SMS notifications

Setup

Clone the repository:

git clone https://github.com/yourusername/price-tracker.git
cd price-tracker

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows

Install dependencies:

pip install -r requirements.txt

Set up environment variables for Twilio:

Create a .env file in the root directory:

AC38b15e4***********04d7fdd2=your_account_sid
aa8920f0*************801346e20ca=your_auth_token

Replace your_account_sid and your_auth_token with your Twilio credentials.

Ensure chromedriver is available in your PATH or specify its location in the code:

driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)

Run the application:

flask run

The application will be available at http://127.0.0.1:5000.

Usage

Navigate to the homepage.

Add a product URL and your desired price threshold on the Add URL page.

Check the Track page to see product status and price comparisons.

Use the Notify option to send SMS alerts for price drops.

File Structure

price-tracker/
|-- static/                # Static files (CSS, JS, etc.)
|-- templates/             # HTML templates
|-- app.py                 # Main Flask application
|-- master_Data.csv        # CSV file storing product details
|-- requirements.txt       # Python dependencies
|-- README.md              # Documentation

Technologies Used

Backend: Flask

Web Scraping: BeautifulSoup, lxml, Selenium

Database: CSV files

Notifications: Twilio API

Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements.

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit changes:

git commit -m "Description of changes"

Push to your branch:

git push origin feature-name

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments

Flask Documentation

Twilio API

BeautifulSoup Documentation

Selenium Documentation

Happy Tracking!
