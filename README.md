# ESP Guitars Web Scraper

This Python script scrapes guitar product data from the [ESP Guitars website](https://www.espguitars.com/guitars) using **Selenium**. It collects data across multiple pages and gathers detailed specs from each product's individual page.

---

## Features

- Scrapes multiple pages of guitar listings.
- Extracts:
  - Name
  - Color
  - Price
  - Product Link
  - Product Image
  - Description
  - Store Notice
  - Guitar Specifications (e.g., scale, body, neck, pickups, electronics, etc.)
- Stores data in JSON files (`products_page1.json`, `products_page2.json`, etc.).

---

## Requirements

- Python 3.7+
- Google Chrome installed
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and added to your system PATH

### Python Packages
Install via pip:
```bash
pip install selenium requests-html
```

---

## Usage

Run the script:
```bash
python scrape_espguitars.py
```

### Output

- **products_pageX.json** (where X = 1, 2, 3) — Contains product data per page.
- Each product entry includes:
  - `name`
  - `color`
  - `price`
  - `link`
  - `image`
  - `description`
  - `notice`
  - `scale`
  - `body`
  - `neck`
  - `fingerboard`
  - `fingerboard radius`
  - `bridge`
  - `bridge pickup`
  - `electronics`
  - `strings`

---

## Notes

- The script uses `sleep()` to avoid loading issues. You may need to adjust wait times or add explicit waits for reliability.
- Error handling is minimal — it assumes the site's structure remains stable.
- Pagination is hardcoded to scrape the first **3 pages**. You can adjust this in the `range(3)` loop.

---

## Disclaimer

This scraper is for educational and personal use only. Be respectful of the website's terms of service and avoid sending too many requests in a short period.
