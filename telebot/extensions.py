import json
import requests
from config import exchanges

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        

        url = f'https://api.apilayer.com/exchangerates_data/convert?to={exchanges[quote]}&from={exchanges[base]}&amount={amount}'
        payload = {}
        headers= {
            "apikey": "YfgzYsci0NOG40HqHQTKkarDsMOnO6rE"
        }
        r = requests.request("GET", url, headers=headers, data = payload)
        resp = json.loads(r.content)
        price = resp['result']
        text = f"Цена {amount} {base} в {quote} : {price}"
        
        return text
