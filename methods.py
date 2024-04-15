from os import system

import Config
import json
import random

try:
	import requests
except:
	system('pip install requests')
	import requests

client = Config.client

def getChatsUpdates():
	_input = {"state":"9999999"}
	_method = {
		"method":"getChatsUpdates",
		"client":client,
		"input":_input
		}
	return _method
	
def sendMessage(_text,_object_guid):
	_rnd = random.randint(100000,999999)
	_input = {"text":_text,
	"rnd":_rnd,
	"object_guid":_object_guid
	}
	_method = {
		"method":"sendMessage",
		"client":client,
		"input":_input
		}
	return _method
def send_Photo(_file_inline,_object_guid):
	
	_rnd = random.randint(100000,999999)
	_input = {
		"is_mute":False,
		"object_guid":_object_guid,
		"rnd":_rnd,
		"file_inline":_file_inline
		
	}
	_method = {
	"method":"sendMessage",
	"client":client,
	"input":_input
	}
	return _method
	
def deleteMessages(_message_id,_object_guid):
	_input = {"message_ids":[_message_id],"object_guid":_object_guid,"type":"Global"}
		
	_method = {
		"method":"deleteMessages",
		"client":client,
		"input":_input
		}
	return _method
	
def requestSendFile(_name,_size,_mime):
	_input = {"file_name":_name,
	"size":_size,
	"mime":_mime
	}
	_method = {
	"method":"requestSendFile",
	"client":client,
	"input":_input
	}
	return _method

def upload_file(_data_file,dec_data,telegram_bot_token=None,chat_id=None):
	bytef = _data_file
	size = str(len(bytef))
	url = dec_data['upload_url']
	header = {
	'auth': Config.auth,	'Host': dec_data['upload_url'].replace('https://','').replace('/UploadFile.ashx',''),
	'chunk-size': size,
	'data-length': size,
    'file-id': str(dec_data['id']),
	'access-hash-send': dec_data['access_hash_send'],'data-type': 'application/octet-stream',
 }
	while True:
		if len(bytef) <= 131072:
			header['part-number'], header['total-part'] = '1', '1'
			j = requests.post(url=url, data=bytef, headers=header)
			response_up = json.loads(j.text)
			
			
			return response_up['data']
		else:
			t = len(bytef) // 131072 + 1
			#telegram method
			if telegram_bot_token !=None:
						message_id = json.loads(requests.get( f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={chat_id}&text=start to uploading...").text)['result']['message_id']
			for i in range(1, t+1):
				if i != t:
					k = (i - 1) * 131072
					header['chunk-size'], header['part-number'], header['total-part'] = '131072', str(i),str(t)
					requests.post(url=url, data=bytef[k:k + 131072], headers=header)
					send_status = ('\r' + f'{round(k / 1024) / 1000} MB '+str(round(len(bytef) / 1024) / 1000)) 
					#telegram method!
					if message_id != None:
						requests.get( f"https://api.telegram.org/bot{telegram_bot_token}/editMessageText?chat_id={chat_id}&message_id={message_id}&text={send_status}")
						
					print(send_status)
				else:
					k = (i - 1) * 131072
					header['chunk-size'], header['part-number'], header['total-part'] = str(len(bytef[k:])), str(i),str(t)
					p = requests.post(url=url, data=bytef[k:], headers=header)
					print('\r' + f'{round(len(bytef) / 1024) / 1000} MB /', sep='', end=f' {round(len(bytef) / 1024) / 1000} MB')
					response_up = json.loads(p.text)
					return response_up['data']
	

	