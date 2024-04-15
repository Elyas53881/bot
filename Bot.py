from os import system

try:
	import requests
except:
	system('pip install requests')
	import requests
	


import methods
import tools
import json
Methods = methods 
Tools = tools

def getChatsUpdates():
	return tools.method_runner(Methods.getChatsUpdates())
	
	
def sendMessage(_text,_object_guid):
	return  tools.method_runner(Methods.sendMessage(_text=_text,_object_guid=_object_guid))
	
def send_Photo(_file_inline,_object_guid):
	return  tools.method_runner(Methods.send_Photo(_file_inline=_file_inline,_object_guid=_object_guid))

def deleteMessages(_message_id,_object_guid):
	return tools.method_runner(Methods.deleteMessages(_message_id=_message_id,_object_guid=_object_guid))
	
def requestSendFile(_name,_size,_mime):
	return tools.method_runner(Methods.requestSendFile(_name=_name,_size=_size,_mime=_mime))
	
	
	#telegram method
def upload_file(_data_file,_dec_data,telegram_bot_token=None,chat_id=None):
	return Methods.upload_file(_data_file=_data_file,dec_data=_dec_data,telegram_bot_token=telegram_bot_token,chat_id=chat_id)
	
	
	
	
	
	
	
	
def encrypt(_text):
	return tools.encryption.encrypt(_text)
def decrypt(_text):
	return tools.encryption.decrypt(_text)
def get_message_id_from_ws(_data):
	return json.loads(_data)['message_updates'][0]['message_id']
def get_websocket_object_guid_from_ws(_data):
	return json.loads(_data)['message_updates'][0]['object_guid']
def get_message_text_form_ws(_data):
	return json.loads(_data)['message_updates'][0]['message']['text']
def get_message_id_from_response(_data):
	return json.loads(_data)['data']['message_updates'][0]['message_id']
	
def check_froward_from_ws(_data):
	info = json.loads(_data)['message_updates'][0]['message']
	if('forwarded_from' in info):
		
		return True
	else:
		return False
		
		
	
	
	

