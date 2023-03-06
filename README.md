# Trendyol Web Scrapper

That script allows you to scrape about 1.5mil product info's from **Trendyol.com** (mostly clothes and cosmetics)

- **urls.json** : Includes API links of list of products.

- **trendyol.py** : ETL script that using API links.

- **settings.py** : Includes response *Headers* settings.
---

* To use it install **python3** and **scrapy** library then clone this project (I've used python==3.9.2 and scrapy==2.6.2 versions)

* Clone this repo into your local ```https://github.com/dorukmavis/trendyol_web_scrapper.git```

* Type ```scrapy crawl ty-url -O extracted_data.json/csv``` on your terminal. (check your cd is ./trendyol_web_scrapper/)

---
