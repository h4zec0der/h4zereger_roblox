from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time
import string
import os

class h4zereger:
    def __init__(self):
        self.accounts_created = 0
        self.use_proxy = False
        self.proxies = []
        self.current_proxy_index = 0
        
    def load_proxies(self):
        try:
            if os.path.exists('proxy.txt'):
                with open('proxy.txt', 'r', encoding='utf-8') as f:
                    proxies = [line.strip() for line in f if line.strip()]
                    print(f"Loaded proxies: {len(proxies)}")
                    return proxies
            else:
                print("File proxy.txt doesnt exist!")
                return []
        except Exception as e:
            print(f"Error loading proxy: {e}")
            return []
    
    def generate_random_username(self, length=8):
        letters = string.ascii_lowercase
        digits = string.digits
        return ''.join(random.choice(letters + digits) for _ in range(length))
    
    def generate_random_password(self, length=12):
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = '!@#$%^&*'
        
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(symbols)
        ]
        
        all_chars = uppercase + lowercase + digits + symbols
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        
        random.shuffle(password)
        return ''.join(password)
    
    def get_next_proxy(self):
        if not self.proxies:
            return None
        
        proxy = self.proxies[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies)
        
        proxy = proxy.replace('http://', '').replace('https://', '')
        return proxy
    
    def setup_driver(self, proxy=None):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        
        if proxy and self.use_proxy:
            chrome_options.add_argument(f'--proxy-server=http://{proxy}')
            print(f"Используем прокси: {proxy}")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        return driver
    
    def save_account(self, username, password):
        with open('accounts.txt', 'a', encoding='utf-8') as f:
            f.write(f"{username}:{password}\n")
    
    def create_account(self, attempt_number):
        proxy = self.get_next_proxy() if self.use_proxy else None
        driver = self.setup_driver(proxy)
        
        try:
            print(f"\n[{attempt_number}] Trying to create account...")
            if proxy:
                print(f"Proxy: {proxy}")
            
            username = self.generate_random_username()
            password = self.generate_random_password()
            
            driver.get("https://www.roblox.com/signup")
            
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "signup-username"))
            )
            
            driver.find_element(By.ID, "signup-username").send_keys(username)
            driver.find_element(By.ID, "signup-password").send_keys(password)
            
            Select(driver.find_element(By.ID, "DayDropdown")).select_by_value("12")
            Select(driver.find_element(By.ID, "MonthDropdown")).select_by_value("Jan")
            Select(driver.find_element(By.ID, "YearDropdown")).select_by_value("2000")
            
            time.sleep(2)
            gender_selectors = [
                'input[name="gender"][value="2"]',
                'input[type="radio"][name="gender"]',
                '.rbx-radio-label',
                '[data-testid*="gender"]'
            ]
            
            for selector in gender_selectors:
                try:
                    elements = driver.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        elements[0].click()
                        break
                except:
                    continue
            
            time.sleep(5)
            
            signup_buttons = [
                '#signup-button',
                'button[type="submit"]',
                '.btn-primary'
            ]
            
            for selector in signup_buttons:
                try:
                    button = driver.find_element(By.CSS_SELECTOR, selector)
                    if button.is_enabled():
                        button.click()
                        break
                except:
                    continue
            
            time.sleep(8)
            
            if "home" in driver.current_url or "welcome" in driver.current_url:
                self.accounts_created += 1
                self.save_account(username, password)
                print(f"✅ Success! Account created: {username}:{password}")
                return True
            else:
                print("❌ Unable to create account")
                return False
                
        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}...")
            return False
        finally:
            driver.quit()
            time.sleep(random.uniform(2, 5)) 
    
    def run(self):
        print("=== h4zecoder AutoRobloxReger ===")
        print("Created by: https://github.com/h4zec0der")
        print("-" * 40)

        proxy_choice = input("Use proxy? (y/n): ").lower().strip()
        self.use_proxy = proxy_choice in ['y', 'yes', 'да', 'д']
        
        if self.use_proxy:
            self.proxies = self.load_proxies()
            if not self.proxies:
                print("Proxy not loaded. Continue without proxy.")
                self.use_proxy = False
        
        try:
            num_accounts = int(input("How much accounts create?: "))
        except:
            num_accounts = 1
        
        print(f"\nStarting to create {num_accounts} accounts...")
        print("All accounts will be saved to file: accounts.txt")
        print("-" * 40)
        
        successful = 0
        for i in range(1, num_accounts + 1):
            if self.create_account(i):
                successful += 1
            
            print(f"Progress: {successful}/{num_accounts} successful")
        
        print("\n" + "=" * 40)
        print("Yay! Creation completed!")
        print(f"Successfully created: {successful}/{num_accounts} accounts")
        print(f"Accounts output file: accounts.txt")
        print("=" * 40)

if __name__ == "__main__":
    registrator = h4zereger()
    registrator.run()