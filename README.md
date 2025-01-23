# Price Tracker Web Application

A Flask-based web application that allows users to track product prices on Amazon, store price thresholds, and receive notifications when the price drops below the desired value. The app leverages web scraping with `BeautifulSoup` and `lxml`, dynamic data retrieval with Selenium, and SMS notifications with Twilio.

---

## Features

- **Track Prices**: Add product URLs and desired price thresholds to monitor price changes.
- **Web Scraping**: Use `BeautifulSoup` and `lxml` to fetch product details like name and price from Amazon.
- **Dynamic Price Fetching**: Employ Selenium for real-time price updates when static scraping fails.
- **CSV Storage**: Save product details, URLs, and thresholds locally in a CSV file.
- **Notifications**: Get SMS alerts for price drops via Twilio integration.
- **Responsive Interface**: Simple HTML templates with Flask to manage user interaction.

## Installation
### Prerequisites

1. Python 3.7+
2. Pip (Python package manager)
3. Google Chrome and [ChromeDriver](https://chromedriver.chromium.org/)
4. Twilio account for SMS notifications

### Setup
## 1. Clone the repository:

   git clone https://github.com/yourusername/price-tracker.git
   cd price-tracker

## 2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows

## 3. Install dependencies:

pip install -r requirements.txt

## 4. Set up environment variables for Twilio:

# Create a .env file in the root directory:

AC38b15e4b********ac50e04d7fdd2=your_account_sid
aa892*************9a21801346e20ca=your_auth_token
Replace your_account_sid and your_auth_token with your Twilio credentials.

## 5. Ensure chromedriver is available in your PATH or specify its location in the code:

driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)

## 6. Run the application:

flask run
The application will be available at http://127.0.0.1:5000.

## Usage

1.Navigate to the homepage.
2.Add a product URL and your desired price threshold on the Add URL page.
3.Check the Track page to see product status and price comparisons.
4.Use the Notify option to send SMS alerts for price drops.

## File Structure

price-tracker/
|-- static/                # Static files (CSS, JS, etc.)
|-- templates/             # HTML templates
|-- app.py                 # Main Flask application
|-- master_Data.csv        # CSV file storing product details
|-- requirements.txt       # Python dependencies
|-- README.md              # Documentation

## Technologies Used

>Backend: Flask
>Web Scraping: BeautifulSoup, lxml, Selenium
>Database: CSV files
>Notifications: Twilio API

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements.

1.Fork the repository.
2.Create a feature branch:
git checkout -b feature-name
3.Commit changes:
git commit -m "Description of changes"
4.Push to your branch
git push origin feature-name
5.Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

>Flask Documentation
>Twilio API
>BeautifulSoup Documentation
>Selenium Documentation

### Happy Tracking!
