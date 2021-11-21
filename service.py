from bs4 import BeautifulSoup
import requests

async def get_data():
    url = "https://www.meteonova.ru/allergy/27553-Nizhniy_Novgorod.htm"
    result = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    soup = BeautifulSoup(result.text, 'html.parser')

    allergy_div = soup.find("div", {"id": "frc_content_weather"})
    table = allergy_div.find("table")

    attributes = dict()

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            attributes[columns[0].get_text()] = columns[len(columns)-1].get_text()

    return attributes
