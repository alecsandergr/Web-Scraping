# Scraping a website

This project uses `scrapy` to scrape information from the courses in [Datacamp](https://www.datacamp.com/courses-all).

There are two version for each file, one in .py and another in .ipynb.

- [crawl.ipynb](/datacamp_courses/crawl.ipynb)
- [craw.py](/datacamp_courses/crawl.py)
- [scrap_with_requests.ipynb](/datacamp_courses/scrap_with_requests.ipynb)
- [scrap_with_requests.py](/datacamp_courses/scrap_with_requests.py)

## Extract data

This project extract the course title, its description and its chapters. The extracted data looks like this sample, where the key is the course title and its values are the description and the chapters:

```json
{"Introduction to DAX in Power BI": 
    {"Description": 
        "Enhance your Power BI knowledge, by learning the fundamentals of Data Analysis Expressions (DAX) such as calculated columns, tables, and measures.",
    "Chapters": ["Getting Started with DAX",
                 "Context in DAX Formulas",
                 "Working with Dates"]
    }
}
```

There are some lines dedicated to print the dictionary information and the output, from one course, looks like this: 

```
Course: Introduction to DAX in Power BI
Description: Enhance your Power BI knowledge, by learning the fundamentals of Data Analysis Expressions (DAX) such as calculated columns, tables, and measures.
    Chapter 1: Getting Started with DAX
    Chapter 2: Context in DAX Formulas
    Chapter 3: Working with Dates
```