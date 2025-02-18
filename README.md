This python script allows you to extract image data and related metadata from the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) for any species. It fetches occurrences, filters for images (StillImage), and saves the associated metadata in an Excel file.

## Features:
- Extracts image data from GBIF occurrence records.
- Downloads images and stores them with filenames based on the catalog number.
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

4. Run the script with the `taxonKey` as an argument:
    ```bash
    python gbif_scrapper.py <taxonKey>
    ```
    Example:
    ```bash
    python gbif_scrapper.py 3173333  # Replace 3173333 with the actual taxonKey for your species
    ```

5. The script will download images and save metadata to `metadata.xlsx`.
