### Car Brand Data Scraper and Database Updater

This Python script scrapes data from a specific webpage, processes it, and updates a PostgreSQL database with the retrieved information. Additionally, it exports the data to a CSV file for further analysis or storage.

#### Overview

The script performs the following tasks:

- **Web Scraping:** Utilizes BeautifulSoup and Requests libraries to scrape data from spinny.com, specifically targeting the top-selling car brands in India.
- **Data Processing:** Extracts relevant information such as brand name, units sold, year-over-year growth percentage, and market share percentage from the scraped HTML table.
- **Database Interaction:** Connects to a PostgreSQL database, clears the existing data in the Car_Brand table, and inserts the freshly scraped data.
- **CSV Export:** Saves the scraped data into a CSV file named car_brand_data.csv.

#### Requirements

- Python 3.x
- BeautifulSoup (bs4)
- Requests
- psycopg2 (PostgreSQL adapter)
- PostgreSQL

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Akshay2001001003/WebScraping.git
    ```



## Usage

1. Navigate to the project directory:

    ```bash
    cd WebScraping
    ```

2. Install dependencies:

    ```bash
    pip install beautifulsoup4
    pip install psycopg2
	pip install requests
    ```

    Additionally, ensure that PostgreSQL is installed on your system. If not, follow the [official installation instructions](https://www.postgresql.org/download/).
	
4. Change the db object in the 4th line of webscrapping.py as per your PostgresConfigurations .
3. Run the scraping script:

    ```bash
    python scraper.py
    ```
 


## LICENCE


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
