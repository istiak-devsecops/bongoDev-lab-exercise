import requests
from bs4 import BeautifulSoup

# Replace with the actual blog URL
url = "https://example-blog.com"

# Send a GET request to the blog page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <h2> tags
titles = soup.find_all('h2')

# Print each title
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.get_text(strip=True)}")
