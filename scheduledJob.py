from bs4 import BeautifulSoup
from datetime import datetime
import requests


def job():
    http_response = requests.get('https://en.wikipedia.org/wiki/Kim_Jong-un')
    soup = BeautifulSoup(http_response.text, 'html.parser')
    is_dead = soup.find("th", string="Died")

    file = open('isDead.txt', 'w')
    datetimelog = open('log.txt', 'w')

    if is_dead is None:
        file.write('false')
    else:
        file.write('true')

    datetimelog.write(datetime.now().strftime("%d-%b-%Y (%H:%M:%S)"))


job()