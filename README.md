# Snapdeal Product Scraper

## Project Description

This project is a **Python web scraping automation script** that collects product information from Snapdeal.
It searches for **"mens watches"** on Snapdeal, scrolls through the product listings, and extracts important details such as:

* Product name
* Product price
* Number of ratings
* Product discount

The scraped data is stored in a **Pandas DataFrame** and can be exported to an Excel file.

---

## Technologies Used

* Python
* Selenium
* Pandas
* Chrome WebDriver

---

## Project Workflow

1. Open Snapdeal website.
2. Search for **"mens watches"**.
3. Scroll down the page to load more products.
4. Click the **See More Products** button until all products load.
5. Extract product information:

   * Product title
   * Product price
   * Number of ratings
   * Discount
6. Store the data in a **Pandas DataFrame**.
7. Optionally export the data to **Excel**.

---

## Requirements

Install the required libraries before running the script.

```bash
pip install selenium pandas
```

You also need to download **ChromeDriver** compatible with your Chrome browser.

Download from:
https://chromedriver.chromium.org/

Place the chromedriver file in:

```
C:/Windows/chromedriver.exe
```

Or update the path in the script.

---

## How to Run the Script

1. Clone the repository:

```bash
git clone https://github.com/your-username/scrap-snapdeal.git
```

2. Navigate to the project folder:

```bash
cd scrap-snapdeal
```

3. Run the Python script:

```bash
python project_snapdeal.py
```

---

## Output

The script extracts product data and stores it in a **Pandas DataFrame**.

You can save the data to Excel by uncommenting the following line:

```python
df.to_excel("scrap_project(snapdeal).xlsx", index=False)
```

The Excel file will contain:

* Product Name
* Price
* Ratings
* Discount

---

## Example Output

| Product Name       | Price   | Ratings | Discount |
| ------------------ | ------- | ------- | -------- |
| Men's Analog Watch | Rs. 799 | (120)   | 60% Off  |

---

## Learning Purpose

This project demonstrates:

* Web automation with Selenium
* Handling dynamic pages
* Infinite scrolling scraping
* Data extraction with Python
* Data processing using Pandas

---

## Author

Abhilash Alle

