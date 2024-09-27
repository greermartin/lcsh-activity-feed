import requests
import json
import os

def download_json(base_url, index, max_downloads):
    if index > max_downloads:
        print(f"Reached the maximum number of downloads ({max_downloads})")
        return

    url = f"{base_url}{index}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        filename = f"dataset_{index}.json"
        with open(filename, "w") as file:
            json.dump(response.json(), file, indent=2)
        print(f"Downloaded and saved {filename}")
        
        # Recursively call the function with the next index
        download_json(base_url, index + 1, max_downloads)
    elif response.status_code == 404:
        print(f"Reached the end of the data at index {index}")
    else:
        print(f"Failed to download data at index {index}. Status code: {response.status_code}")

# Base URL without the index and .json extension
base_url = "https://id.loc.gov/authorities/subjects/activitystreams/feed/"

# Create a directory to store the downloaded files
os.makedirs("downloaded_datasets", exist_ok=True)
os.chdir("downloaded_datasets")

# Start downloading from index 1, with a maximum of 10 downloads
download_json(base_url, 1, 10)




