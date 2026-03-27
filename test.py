import pandas as pd
import requests

def get_uniform_polyhedra():
    url = "https://en.wikipedia.org/wiki/List_of_uniform_polyhedra"
    
    # Send a custom User-Agent to tell Wikipedia we are a regular browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Fetch the webpage using requests
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    # Pass the text of the response into pandas
    tables = pd.read_html(response.text)
    polyhedra =[]
    
    for df in tables:
        # Check if the table has a 'Name' column
        if "Name" in df.columns:
            # Extract the names, drop NaN values, and add to our list
            names = df["Name"].dropna().tolist()
            polyhedra.extend(names)
            
    # Print them out separated by a newline
    print('\n'.join(polyhedra))

if __name__ == "__main__":
    get_uniform_polyhedra()
