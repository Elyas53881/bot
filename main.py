from os import system
try:
  import requests
except:
  system('pip install requests')
  import requests
print(requests.get('https://rubika.ir'))

  
