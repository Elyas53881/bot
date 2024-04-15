import requests
import json
data= '{"api_version":"6","auth":"kakxgkaryqxuiqvgiyrorjnhgxvhwftz","data_enc":"BY7wBmTjxuCr6NVzTeNeqrXGEvyc+WgdOpoWdVVtkiTOHeuyxICcfZTlHqsUK8hgyCX1+KQMPhWwIP8hI+k0wGIRIIjtfK4R8+VW49Lzpz5rWhagYcV+i6/7YkjalvSQkeT3UYuEnpTBodFVpBlOLO6QNv1cAs1Rza7NEvKxh3qU9/1ZYrHWhTkmHC2lL4RkSzjnT/paD8YTgRg8tOYaOQ+i9TOxVmcSoKC9FlE+xULSPRLC3fwov6jmQUcXcbSmZ3Hyj7j5IM0JXCc8wWmBrQ\u003d\u003d","sign":"ZC132EHq3rwUBDmQO8JpOEPiBJ7x/MfqE27LhGHQZBwjBnq8US6wjtygwHUj84Xr0JvCsnHqsKf7NnjGlOVfiA5sBzImm/NCXhI6gayWYwgPgiWEDc9XU3r71ErIoQcVS8pbvyxNo2NpcytOSb4cX1b8bMqKGTdfUUWvY+KyhrY\u003d"}'
server_link = 'https://messengerg2c5.iranlms.ir/'
dataj = json.loads(data)
print(requests.post(server_link,json=dataj).text)
