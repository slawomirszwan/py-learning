
import requests
import json

# Adres URL docelowej usługi
url = 'http://kodpocztowy.intami.pl/api/81-029'

# Dane w formacie JSON, które chcesz wysłać
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Przekształć dane na format JSON
json_data = json.dumps(data)

# Ustaw nagłówek "Content-Type" na "application/json" dla wysyłanych danych
headers = {'Content-Type': 'application/json'}

# Wyślij żądanie POST z danymi JSON na adres URL
# response = requests.post(url, data=json_data, headers=headers)
response = requests.post(url, headers=headers)

# Sprawdź, czy żądanie zostało pomyślnie wykonane (kod odpowiedzi 200)
if response.status_code == 200:
    # Wyświetl zawartość odpowiedzi
    print(response.json())
else:
    print('Błąd! Kod odpowiedzi:', response.status_code)


"""
pip install requests

(.venv) > pip install requests
Collecting requests
  Obtaining dependency information for requests from https://files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl.metadata
  Downloading requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting charset-normalizer<4,>=2 (from requests)
  Obtaining dependency information for charset-normalizer<4,>=2 from https://files.pythonhosted.org/packages/57/ec/80c8d48ac8b1741d5b963797b7c0c869335619e13d4744ca2f67fc11c6fc/charset_normalizer-3.3.2-cp311-cp311-win_am
d64.whl.metadata
  Downloading charset_normalizer-3.3.2-cp311-cp311-win_amd64.whl.metadata (34 kB)
Collecting idna<4,>=2.5 (from requests)
  Obtaining dependency information for idna<4,>=2.5 from https://files.pythonhosted.org/packages/c2/e7/a82b05cf63a603df6e68d59ae6a68bf5064484a0718ea5033660af4b54a9/idna-3.6-py3-none-any.whl.metadata
  Downloading idna-3.6-py3-none-any.whl.metadata (9.9 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Obtaining dependency information for urllib3<3,>=1.21.1 from https://files.pythonhosted.org/packages/a2/73/a68704750a7679d0b6d3ad7aa8d4da8e14e151ae82e6fee774e6e0d05ec8/urllib3-2.2.1-py3-none-any.whl.metadata
  Downloading urllib3-2.2.1-py3-none-any.whl.metadata (6.4 kB)
Collecting certifi>=2017.4.17 (from requests)
  Obtaining dependency information for certifi>=2017.4.17 from https://files.pythonhosted.org/packages/ba/06/a07f096c664aeb9f01624f858c3add0a4e913d6c96257acb4fce61e7de14/certifi-2024.2.2-py3-none-any.whl.metadata
  Downloading certifi-2024.2.2-py3-none-any.whl.metadata (2.2 kB)
Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Downloading certifi-2024.2.2-py3-none-any.whl (163 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.8/163.8 kB 153.5 kB/s eta 0:00:00
Using cached charset_normalizer-3.3.2-cp311-cp311-win_amd64.whl (99 kB)
Using cached idna-3.6-py3-none-any.whl (61 kB)
Downloading urllib3-2.2.1-py3-none-any.whl (121 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.1/121.1 kB 1.2 MB/s eta 0:00:00
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1

[notice] A new release of pip is available: 23.2.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip


curl -H 'Accept:application/json' 'http://kodpocztowy.intami.pl/api/81-029'
"""
