import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'

def get_html():
    url = 'https://vacuumwars.com/best-vacuum-cleaners/robot-vacuums/'
    headers = {'User-Agent': UA}
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        return response.content
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    sys.exit(0)
    
def get_html_tables(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.find_all('table')

def process_table(tables) -> list[dict]:
    table_data = []
    for table in tables:
        if not 'Mopping Performance' in str(table):
            continue
        model_name = ''
        rows = {}

        for row in table.find_all('tr'):
            if not model_name:
                cells_header = [cell.get_text(strip=True) for cell in row.find_all(['th'])]
                model_name = cells_header[1]
                
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['td'])]
            if not row_data:
                continue
            rows[row_data[0]] = float(row_data[1])
            
        if rows:
            rows['Model'] = model_name
            table_data.append(rows)        
    return table_data


def save_to_excel(table_ld) -> None:
    df = pd.DataFrame(table_ld)
    file_name = 'vacuums_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    df.to_excel(f'{file_name}.xlsx', index=False)

def main():
    html = get_html()
    tables = get_html_tables(html)
    table_ld = process_table(tables)
    save_to_excel(table_ld)

if __name__ == "__main__":
    main()
