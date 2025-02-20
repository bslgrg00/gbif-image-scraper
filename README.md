# 🌍 GBIF Image Scraper 
![GBIF Logo](logo.png) GBIF Image Scraper
📸 A python script to extract images and metadata from the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) for any species.  

---

## 📌 Features  
✅ Fetches **occurrence records** from GBIF using `taxonKey`.  
✅ Downloads **species images** and names them based on the **catalog number**.  
✅ Saves **metadata** in an **Excel file (`metadata.xlsx`)**.  
✅ Easy-to-use **command-line interface**.  

---

## 📦 Requirements  
Before running the script, ensure you have the required dependencies installed:  
- `requests`
- `pandas`

---

## ⚙️ Installation & Usage
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

---

## 📂 Output  
✅ Images are saved in the `images/` directory.  
✅ Metadata is stored in `metadata.xlsx`.  


