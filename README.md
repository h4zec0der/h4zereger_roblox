Automate Roblox account creation with proxy support, random data generation, and browser automation

## 🚀 Features
```
✅ Automatic Roblox account creation
✅ Proxy rotation for anonymity
✅ Random username/password generation
✅ Selenium WebDriver automation
✅ Error handling and recovery
✅ Accounts saved to text file
✅ User-friendly command-line interface
```
# 📋 Usage

**🚀 Quick Start**

Install dependencies - Run install_dependencies.bat to install required packages
Prepare proxies (optional) - Create proxy.txt file with your proxy list (one per line)
Run the creator - Execute run_script.bat to start the account creation process

**🎮 Interactive Prompts**
When you run the script, you'll be prompted to:

```
 Use proxy? (y/n): y
 How much accounts create?: 5
```

**📝 Proxy Format**
Create a proxy.txt file with your proxies in one of these formats:

```
ip:port
ip:port:user:pass
http://ip:port
https://ip:port
```
**📊 Output**
All created accounts are automatically saved to accounts.txt in the format:
```
username:password
username:password
```
**🔧 Batch Files**
```
install_dependencies.bat - Install all required Python packages
run_script.bat - Run the main account creator
install_and_run.bat - Install dependencies and run in one step
```
**🔄 Proxy Rotation**
The tool automatically rotates through your proxy list, switching to the next proxy after each account creation attempt.

**⚡ Example Workflow**
```
# 1. Install dependencies
install_dependencies.bat

# 2. Create proxy.txt with your proxies
echo "192.168.1.1:8080" > proxy.txt
echo "192.168.1.2:8080:user:pass" >> proxy.txt

# 3. Run the creator
run_script.bat

# Follow prompts to create 10 accounts with proxy rotation
```
## 📱 Requirements
```
Python 3.7+
Chrome Browser
Internet connection
Windows OS (for batch files)
```

# 📋 How It Works
```
Creates unique usernames and strong passwords
Uses Selenium to control Chrome browser
Automatically fills out registration forms
Switches between proxies for better anonymity
Saves created accounts to accounts.txt
```
# ⚠️ Educational Purpose Only ⚠️

**This tool is intended for educational purposes and testing only. Always respect Roblox's Terms of Service and use responsibly.**

# 🚨 Legal Disclaimer
**This tool is provided AS-IS. The author is not responsible for any misuse or violations of terms of service. Use at your own risk.**

Created by: h4zec0der
