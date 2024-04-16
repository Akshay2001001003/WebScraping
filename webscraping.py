import csv
from bs4 import BeautifulSoup
import requests
import psycopg2
con = psycopg2.connect(
database="postgres",
user="postgres",
password="12",
host="localhost",
port= '5432'
)
cursor_obj = con.cursor()
response = requests.get('https://www.spinny.com/blog/index.php/top-selling-car-brands-in-india/')
cursor_obj.execute("DELETE FROM Car_Brand")


html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', class_='wptb-preview-table')
table_row=table.findAll('tr')

for row in table_row[1:]:
    cells = row.find_all('td')
    brand_name = cells[0].get_text(strip=True)
    units_sold_march_2024 = int(cells[1].get_text(strip=True).replace(',', ''))
    units_sold_march_2023 = int(cells[2].get_text(strip=True).replace(',', ''))
    yoy_growth_percentage = float(cells[3].get_text(strip=True).replace('%', ''))
    market_share_percentage = float(cells[4].get_text(strip=True).replace('%', ''))

    cursor_obj.execute("INSERT INTO Car_Brand (Brand_Name, Units_Sold_March_2024, Units_Sold_March_2023, YoY_Growth_Percentage, Market_Share_Percentage) VALUES (%s, %s, %s, %s, %s)",
                       (brand_name, units_sold_march_2024, units_sold_march_2023, yoy_growth_percentage, market_share_percentage))

cursor_obj.execute("SELECT * FROM Car_Brand")
rows = cursor_obj.fetchall()

for row in rows:
    print(row)

csv_file = "car_brand_data.csv"

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([desc[0] for desc in cursor_obj.description])
    writer.writerows(rows)

con.commit()

cursor_obj.close()
con.close()