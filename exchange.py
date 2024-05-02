import requests
import json
from datetime import datetime

response = requests.get('https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID') ##YOUR_APP_ID改成api

data = json.loads(response.text)

# 获取USD到CNY的汇率
usd_to_cny = data['rates']['CNY']

# 需要的货币列表
required_currencies = ['CNY', 'USD', 'EUR', 'GBP', 'CAD', 'JPY', 'KRW', 'HKD', 'TWD', 'ARS', 'TRY']

# 计算其他货币到CNY的汇率
rates = {}
for currency in required_currencies:
    rate = data['rates'].get(currency)
    if rate:
        # 货币到USD的汇率取倒数，得到1单位的货币对应多少USD
        one_unit_to_usd = 1 / rate
        # 1单位的货币对应的USD乘以1USD对应的CNY，得到1单位的货币对应多少CNY
        one_unit_to_cny = one_unit_to_usd * usd_to_cny
        # 保留4位小数
        one_unit_to_cny = round(one_unit_to_cny, 4)
        rates[currency] = one_unit_to_cny

# 创建新的字典来存储日期和汇率数据
new_data = {
    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'rates': rates
}

# 将数据写入到指定的文件中
with open('/path/to/exchange_rates.json', 'w') as f:
    json.dump(new_data, f, indent=4)
