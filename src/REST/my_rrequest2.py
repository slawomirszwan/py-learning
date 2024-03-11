#https://kodpocztowy.intami.pl/
# pip install requests
import requests
# pip install requests

# Adres URL docelowej usługi
#tutaj parametry w GET w adresie , ale moga być też w POST wtedy dołączamy do BODY dane
url = 'http://kodpocztowy.intami.pl/api/81-029'

# Dane w formacie JSON, które chcesz wysłać
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# Przekształć dane na format JSON
# json_data = json.dumps(data)

# Ustaw nagłówek "Content-Type" na "application/json" dla wysyłanych danych
headers = {'Content-Type': 'application/json'}

# Wyślij żądanie POST z danymi JSON na adres URL
# response = requests.post(url, data=json_data, headers=headers)
response = requests.post(url, headers=headers)

# Sprawdź, czy żądanie zostało pomyślnie wykonane (kod odpowiedzi 200)
if response.status_code == 200:
    # Wyświetl zawartość odpowiedzi
    print(response.json())
    """
[
{'kod': '81-029', 'miejscowosc': 'Gdynia', 'ulica': 'Jabłkowa', 'gmina': 'Gdynia', 'powiat': 'Gdynia', 
'wojewodztwo': 'pomorskie', 'numeracja': []}, 
{'kod': '81-029', 'miejscowosc': 'Gdynia', 'ulica': 'Północna', 'gmina': 'Gdynia', 'powiat': 'Gdynia', 
'wojewodztwo': 'pomorskie', 'numeracja': []}, 
{'kod': '81-029', 'miejscowosc': 'Gdynia', 'ulica': 'Przemysłowa', 'gmina': 'Gdynia', 'powiat': 'Gdynia', 
'wojewodztwo': 'pomorskie', 'numeracja': []}, 
{'kod': '81-029', 'miejscowosc': 'Gdynia', 'ulica': 'Wiśniowa', 'gmina': 'Gdynia', 'powiat': 'Gdynia', 
'wojewodztwo': 'pomorskie', 'numeracja': []}
]

Process finished with exit code 0
    
    """
else:
    print('Błąd! Kod odpowiedzi:', response.status_code)

"""
metody obchodzenia zabezpieczeń że korzystanie 100 request z jednego adresu WWW
https://stackoverflow.com/questions/55872164/how-to-rotate-proxies-on-a-python-requests

"""