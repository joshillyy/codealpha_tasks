# Project Overview

This project was developed as part of the CodeAlpha Data Analytics Internship Task 1.
The objective of this project is to collect book data from a website using web scraping techniques and create a custom dataset for analysis.

# Objectives

Extract data from a public website using Python.
Understand HTML structure and web navigation.
Create a structured dataset.
Perform basic data cleaning and analysis.
Visualize insights using charts.

# Tools and Technologies

Python
Requests
BeautifulSoup
Pandas
Matplotlib
Jupyter Notebook
VS Code

# Website Used

Books to Scrape
https://books.toscrape.com/

# Data Collected

The following information was collected:

Book Title
Price
Rating
Availability

# Project Structure

Book_Market_Analysis/

├── data/
│ └── books.csv

├── notebooks/
│ └── analysis.ipynb

├── src/
│ └── scraper.py

├── screenshots/

├── project_report.md

└── README.md

# Methodology

Inspected the website HTML structure.
Identified relevant tags and classes containing book information.
Extracted data using BeautifulSoup.
Stored the extracted information in a Pandas DataFrame.
Exported the dataset to CSV format.
Performed data cleaning and validation.
Conducted exploratory data analysis.
Created visualizations to identify trends.

# Analysis Performed

Average Book Price
Highest Priced Book
Lowest Priced Book
Rating Distribution
Price Distribution

# Project Insights

1. Total books collected: 20

2. Average book price: £35.48

3. Highest book price: £57.20

4. Lowest book price: £10.15

5. Price distribution shows most books are priced between £20 and £50.

# Conclusion

This project demonstrates the use of web scraping for data collection and basic data analytics techniques. The generated dataset can support further exploratory analysis and visualization tasks.
