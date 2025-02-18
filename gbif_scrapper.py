import requests
import pandas as pd
import argparse
from urllib.parse import urljoin

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Download images and metadata from GBIF for multiple species.")
    parser.add_argument("taxonKeys", type=str, help="Comma-separated list of GBIF taxon keys for the species of interest.")
    return parser.parse_args()

# GBIF API endpoint for occurrences
api_url = "https://api.gbif.org/v1/occurrence/search"

# Parse arguments
args = parse_arguments()

# Parse the taxonKeys from the input string (e.g., "3173333,1234567")
taxon_keys = [int(key) for key in args.taxonKeys.split(",")]

# List to store metadata
metadata_list = []

# Dictionary to track image counts per catalog number
image_count = {}

# Function to download an image
def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Fetch occurrences and process data for each taxonKey
for taxon_key in taxon_keys:
    print(f"Fetching data for taxonKey: {taxon_key}")
    
    # Parameters for the API request
    params = {
        "taxonKey": taxon_key,  # Use current taxonKey
        "limit": 20,            # Number of results per request
        "offset": 0,            # Start from the first result
        "mediaType": "StillImage"  # Filter for occurrences with images
    }

    while True:
        # Send a GET request to the GBIF API
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
        
        # Parse the JSON response
        data = response.json()
        
        # Check if there are no more results
        if not data.get("results"):
            print("No more results found.")
            break
        
        # Process each occurrence
        for occurrence in data["results"]:
            if "media" in occurrence:
                for media in occurrence["media"]:
                    # Check if the "type" key exists and is "StillImage"
                    if media.get("type") == "StillImage":
                        # Safely access image URL
                        image_url = media.get("identifier")
                        if not image_url:
                            print(f"Skipping media object (no identifier): {media}")
                            continue
                        
                        # Extract metadata
                        catalog_number = occurrence.get("catalogNumber", "NA")
                        year = occurrence.get("year", "NA")
                        month = occurrence.get("month", "NA")
                        country = occurrence.get("country", "NA")
                        decimal_latitude = occurrence.get("decimalLatitude", "NA")
                        decimal_longitude = occurrence.get("decimalLongitude", "NA")
                        state_province = occurrence.get("stateProvince", "NA")
                        verbatim_locality = occurrence.get("verbatimLocality", "NA")
                        
                        # Handle duplicate catalog numbers by appending an index
                        if catalog_number == "NA":
                            # For unknown catalog numbers, use a placeholder
                            catalog_number = "Unknown"
                        
                        if catalog_number not in image_count:
                            image_count[catalog_number] = 1
                        else:
                            image_count[catalog_number] += 1
                        
                        # Generate image filename using catalogNumber and index
                        filename = f"{catalog_number}_{image_count[catalog_number]}.jpg"
                        
                        # Download the image
                        download_image(image_url, filename)
                        
                        # Append metadata to the list
                        metadata_list.append({
                            "taxonKey": taxon_key,
                            "catalogNumber": catalog_number,
                            "year": year,
                            "month": month,
                            "country": country,
                            "decimalLatitude": decimal_latitude,
                            "decimalLongitude": decimal_longitude,
                            "stateProvince": state_province,
                            "verbatimLocality": verbatim_locality,
                            "imageFilename": filename,
                            "imageURL": image_url
                        })
                    else:
                        # Debugging: Print media objects without "type" or with unexpected types
                        print(f"Skipping media object (missing or invalid type): {media}")
        
        # Update the offset for the next page of results
        params["offset"] += params["limit"]

# Save metadata to an Excel file
if metadata_list:
    df = pd.DataFrame(metadata_list)
    df.to_excel("metadata.xlsx", index=False)
    print("Metadata saved to metadata.xlsx")
else:
    print("No metadata found.")
