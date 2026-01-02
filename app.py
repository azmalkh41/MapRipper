from flask import Flask, render_template, request, send_file, jsonify
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from urllib.parse import urlparse

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    termux_chrome = '/data/data/com.termux/files/usr/bin/chromium'
    termux_driver = '/data/data/com.termux/files/usr/bin/chromedriver'
    
    if os.path.exists(termux_chrome):
        options.binary_location = termux_chrome
    
    try:
        if os.path.exists(termux_driver):
            service = Service(executable_path=termux_driver)
            return webdriver.Chrome(service=service, options=options)
        return webdriver.Chrome(options=options)
    except Exception as e:
        print(f"[v0] Driver Error: {str(e)}")
        raise e

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        try:
            driver = get_driver()
        except Exception as e:
            return jsonify({'error': f'Failed to start browser: {str(e)}'}), 500

        try:
            driver.get(url)
            
            WebDriverWait(driver, 15).until(lambda d: "google.com/maps" in d.current_url)
            
            # Wait for images to load (scrolling might help)
            time.sleep(5) 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            elements = driver.find_elements(By.TAG_NAME, 'img')
            image_urls = []
            
            for el in elements:
                src = el.get_attribute('src')
                if src and ('googleusercontent.com' in src or 'lh3.googleusercontent.com' in src):
                    # Remove resolution params and set to high res (s1600 or s32767)
                    base_url = src.split('=')[0]
                    high_res = f"{base_url}=s1600"
                    if high_res not in image_urls:
                        image_urls.append(high_res)

            return jsonify({'images': image_urls, 'count': len(image_urls)})
        except Exception as e:
            return jsonify({'error': f'Extraction failed: {str(e)}'}), 500
        finally:
            driver.quit()
    except Exception as e:
        # Final fallback for JSON
        return jsonify({'error': f'System error: {str(e)}'}), 500

if __name__ == '__main__':
    # Run on 0.0.0.0 so it's accessible from other devices in the network
    app.run(host='0.0.0.0', port=5000, debug=True)
