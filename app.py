from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import pandas as pd
import os
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Header for web scraping
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

# Helper Functions
def get_amazon_price(dom):
    try:
        # Adjust the XPath to match the current Amazon structure
        item_price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
        item_price = item_price.replace(',', '').replace('₹', '').strip()
        return int(float(item_price))
    except (IndexError, ValueError):
        return None  # Price not found or invalid format

def fetch_dynamic_price(url):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service('path/to/chromedriver'), options=options)
    driver.get(url)
    try:
        price_element = driver.find_element(By.CLASS_NAME, "a-offscreen")
        return int(price_element.text.replace(',', '').replace('₹', '').strip())
    except Exception:
        return None
    finally:
        driver.quit()

def get_product_name(dom):
    try:
        name = dom.xpath('//span[@id="productTitle"]/text()')
        return name[0].strip()
    except IndexError:
        return "Unknown Product"

# Routes
@app.route('/')
def home():
    return render_template('index.html')  # Homepage

@app.route('/add_url', methods=['GET', 'POST'])
def add_url():
    if request.method == 'POST':
        url = request.form['product_url']
        price = request.form['product_price']

        # Save to CSV
        df = pd.read_csv('master_Data.csv') if os.path.exists('master_Data.csv') else pd.DataFrame(columns=['url', 'price', 'name'])
        new_data = {'url': url, 'price': int(price), 'name': 'Product'}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv('master_Data.csv', index=False)
        flash('URL successfully added!', 'success')
        return redirect(url_for('add_url'))

    return render_template('add_url.html')

@app.route('/track')
def track():
    try:
        df = pd.read_csv('master_Data.csv')
    except FileNotFoundError:
        flash("No data to track. Please add URLs first.", "warning")
        return redirect(url_for('add_url'))

    results = []
    for _, row in df.iterrows():
        url = row['url']
        master_price = row['price']
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_dom = et.HTML(str(soup))

        current_price = get_amazon_price(main_dom)
        product_name = get_product_name(main_dom)

        if current_price is None:
            status = "Price not available"
        elif current_price < master_price:
            status = f"Price dropped to {current_price}!"
        else:
            status = "No change"

        results.append({
            'name': product_name,
            'url': url,
            'master_price': master_price,
            'current_price': current_price,
            'status': status
        })

    return render_template('track.html', results=results)

@app.route('/notify')
def notify():
    # Example Notification Code
    account_sid = os.getenv('AC38b15e4b20d8868a51dac50e04d7fdd2')
    auth_token = os.getenv('aa8920f0583311a5c9a21801346e20ca')

    if not account_sid or not auth_token:
        flash("Twilio credentials not set.", "danger")
        return redirect(url_for('track'))

    client = Client(account_sid, auth_token)

    # Fetch data and send SMS for price drops
    try:
        df = pd.read_csv('master_Data.csv')
        message_content = "Price drops detected:\n"
        for _, row in df.iterrows():
            message_content += f"{row['name']} - {row['url']}\n"

        message = client.messages.create(
            body=message_content,
            from_='+14155238886',  # Replace with your Twilio number
            to='+7999878432'       # Replace with your number
        )
        flash("Notification sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send notification: {str(e)}", "danger")

    return redirect(url_for('track'))

if __name__ == '__main__':
    app.run(debug=True)