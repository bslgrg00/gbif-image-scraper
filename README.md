This python script allows you to extract images and related metadata from the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) for any species. It retrieves occurrence records, filters for images (StillImage), and saves the associated metadata in an Excel file.

## Features:
- Fetches occurrence records from GBIF based on taxon keys.
- Downloads images and names them based on the catalog number.
- Saves metadata in an Excel file.

## Requirements:
- `requests`
- `pandas`

## How to Use:
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/gbif-image-scraper.git
    ```

2. Install required dependencies:
    ```bash
    pip install requests pandas
    ```

3. Find the `taxonKey` for your species from GBIF.

4. Run the script with comma-separated `taxonKeys`:
    ```bash
    python gbif_scrapper.py <taxonKey1>,<taxonKey2>,<taxonKey3>
    ```
    Example:
    ```bash
    python gbif_scrapper.py 1234567,9876543,9810246  # Replace with the actual taxonKeys for your species
    ```

5. The script will download images and save metadata to `metadata.xlsx`.
