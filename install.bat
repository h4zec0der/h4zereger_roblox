@echo off
echo Installing dependencies...
echo.

python -m pip install --upgrade pip
pip install selenium
pip install webdriver-manager

echo.
echo Dependencies installed successfully!
echo Press any key to exit...
pause