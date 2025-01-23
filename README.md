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

---

## Installation

### Prerequisites

1. Python 3.7+
2. Pip (Python package manager)
3. Google Chrome and [ChromeDriver](https://chromedriver.chromium.org/)
4. Twilio account for SMS notifications

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/price-tracker.git
   cd price-tracker
