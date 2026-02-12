import pandas as pd
import requests
import io

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"

#Mimic a real browser so Wikipedia doesn't block you
headers = {
    "User-Agent": "Mozilla/5.0 "
}

#Fetch the data
response = requests.get(url, headers=headers)

if response.status_code == 200:
    #Convert the HTML text into a stream that Pandas understands
    html_content = io.StringIO(response.text)
    
    dfs = pd.read_html(html_content)
    
    df = dfs[1]
    
    print(f"Scraped {len(df)} rows.")
    print(df.head())
    