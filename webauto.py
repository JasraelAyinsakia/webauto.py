import webbrowser as wb

# Set Chrome browser path
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

# Register Chrome browser
wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))

# Function to open URLs
def webauto():
    url = input("Enter a website URL (e.g., https://www.google.com): ")
    if not url.startswith("http"):
        url = "https://" + url
    print(f"Opening: {url}")
    wb.get('chrome').open(url)

# Call the function
webauto()
