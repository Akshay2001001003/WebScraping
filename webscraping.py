import csv
from bs4 import BeautifulSoup
import requests
import psycopg2

# Database connection parameters
db = {
    "database": "postgres",
    "user": "postgres",
    "password": "12",
    "host": "localhost",
    "port": 5432
}

# URL of the Spinny website
url = 'https://www.spinny.com/blog/index.php/top-selling-car-brands-in-india/'

try:
    # Establish connection to PostgreSQL
   with psycopg2.connect(**db) as con:
        cursor = con.cursor()

        # Fetch HTML content from the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='wptb-preview-table')
        table_rows = table.find_all('tr')[1:]  # Exclude header row


        for row in table_rows:
            cells = row.find_all('td')
            brand_name = cells[0].get_text(strip=True)
            units_sold_march_2024 = int(cells[1].get_text(strip=True).replace(',', ''))
            units_sold_march_2023 = int(cells[2].get_text(strip=True).replace(',', ''))
            yoy_growth_percentage = float(cells[3].get_text(strip=True).replace('%', ''))
            market_share_percentage = float(cells[4].get_text(strip=True).replace('%', ''))

            # Check if data matches existing data
            cursor.execute("SELECT * FROM Car_Brand WHERE Brand_Name = %s AND Units_Sold_March_2024 = %s AND Units_Sold_March_2023 = %s AND YoY_Growth_Percentage = %s AND Market_Share_Percentage = %s",
                           (brand_name, units_sold_march_2024, units_sold_march_2023, yoy_growth_percentage, market_share_percentage))
            existing_data = cursor.fetchone()

            if not existing_data:
                # Insert data into the database
                cursor.execute("INSERT INTO Car_Brand (Brand_Name, Units_Sold_March_2024, Units_Sold_March_2023, YoY_Growth_Percentage, Market_Share_Percentage) VALUES (%s, %s, %s, %s, %s)",
                               (brand_name, units_sold_march_2024, units_sold_march_2023, yoy_growth_percentage, market_share_percentage))

        # Fetch all rows from the table
        cursor.execute("SELECT * FROM Car_Brand")
        rows = cursor.fetchall()

        # Print the fetched rows
        for row in rows:
            print(row)

        # Write data to CSV file
        csv_file = "car_brand_data.csv"
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Brand_Name', 'Units_Sold_March_2024', 'Units_Sold_March_2023', 'YoY_Growth_Percentage', 'Market_Share_Percentage'])
            writer.writerows(rows)

        # Commit the transaction
        con.commit()

except (psycopg2.Error, requests.RequestException) as err:
    print(f"Error occurred: {err}")
finally:
    # Close cursor and database connection
    cursor.close()
