import requests
import json


# <script src="https://www.cbr-xml-daily.ru/daily_json.js"></script>

r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

def refresh():
    with open('daily_json.json', 'w', encoding ='utf-8') as file:
        file.write(r.content.decode('utf-8'))
    
refresh()
data = dict

filename = 'daily_json.json'
def init_dict(filename):
    with open(filename, 'r', encoding = 'utf-8') as json_file:
        data = json.load(json_file)
    return data    

data = init_dict(filename)


def find_valute(name):
    msg = ''
    for i in data['Valute']:
        if name.lower() in data['Valute'][i]["CharCode"].lower() or name.lower() in data['Valute'][i]['Name'].lower():
            msg += (data['Valute'][i]["CharCode"] + " " + data['Valute'][i]['Name'] + " " + 
                    str(data['Valute'][i]['Value']) + '\n')
    return msg




# str = '<a href="https://www.cbr-xml-daily.ru/">Курсы ЦБ РФ в XML и JSON, API</a>'