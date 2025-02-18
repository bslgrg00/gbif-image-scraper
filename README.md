This python script allows you to extract image data and related metadata from the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) for any species. It fetches occurrences, filters for images (StillImage), and saves the associated metadata in an Excel file.

## Features:
- Extracts image data from GBIF occurrence records.
- Downloads images and stores them with filenames based on the catalog number.
- Saves metadata including year, country, locality, and image URL in an Excel file.

## Requirements:
- `requests`
- `pandas`

You can install the required libraries with:

```bash
pip install requests pandas
