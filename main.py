import os
from os import system
try:
	import telebot
except:
	system('pip pip install pyTelegramBotAPI')
	import telebot
try:
	import requests
except:
	system('pip install requests')
	import requests
try:
	import youtube_dl
except:
	system('pip install youtube_dl')
	import youtube_dl

import Bot
import json



token = '7073723735:AAFPfNKXGZBFuIEh5F0iL3t4HORXAufI0Ig'
guid = 'u0FuaM2033784d4289904f1557ef7104'

telgram_bot = telebot.TeleBot(token)
rubika_bot = Bot




def save_photo(_message):
	_photo = _message.photo[-1]
	_file_info = telgram_bot.get_file(_photo.file_id)
	_file_path = _file_info.file_path
	
	
	_url = f"https://api.telegram.org/file/bot{token}/{_file_path}"
	_file = requests.get(_url).content
	with open('photo.jpg','wb') as create_file:
		create_file.write(_file)
	with open('photo.jpg','rb') as photo:
		photo = photo.read()
		print('photo is saved(')
	return photo

def save_video(_message):
	_video = _message.video
	_file_info = telgram_bot.get_file(_video.file_id)
	_file_path = _file_info.file_path
	
	
	_url = f"https://api.telegram.org/file/bot{token}/{_file_path}"
	_file = requests.get(_url).content
	
	with open('video.mp4','wb') as create_file:
		create_file.write(_file)
	with open('video.mp4','rb') as video:
		video = video.read()
		print('saved')
	return video


def delete_file(file_path):
	if os.path.exists(file_path):
	    os.remove(file_path)
	    print(f"{file_path} has been successfully deleted.")
	else:
	    print(f"{file_path} does not exist.")
	
	

def porn_hub_down(link):
	try:
		url = link
		output_path = 'video.mp4'
		ydl_opts = {'outtmpl': output_path,}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
			with open('video.mp4','rb') as video:
				Video = video.read()
				telgram_bot.send_message(6878002162,'video dwonloaded')
		return Video
		
	except:
		telgram_bot.send_message(6878002162,'Error Download !')
		return None


	
	
	
def set_file_inline(_file_name,_mime,_access_hash_rec,dec_data,size):
	print(_access_hash_rec)
	file_inline = {
	"access_hash_rec":_access_hash_rec,
	"auto_play":False,
	"dc_id":dec_data['dc_id'],
	"file_id":int(dec_data['id']),
	"file_name":_file_name,
	"height":'0',
	"is_round":False,
	"is_spoil":False,
	"mime":_mime,
	"size":size,
	"time":'0',
	"type":"File",
	"width":'0'
	}
	return file_inline
	


		
	
	
	

@telgram_bot.message_handler(content_types=['photo','text','video'])
def handler_telgram(message):
	try:
		if(message.content_type=='text'):
			text = message.text
			
			if text == 's':
				print(rubika_bot.sendMessage(text,guid))
			
			if text.startswith("PD"):
				telgram_bot.reply_to(message,'start to downloading')
				video_link = text.replace('PD ','')
				
				
				
				video =	porn_hub_down(video_link)
				upload_data = json.loads(rubika_bot.requestSendFile('video.mp4',len(video),'mp4'))['data']
			access_hash_rec = rubika_bot.upload_file(video,upload_data,telegram_bot_token=token,chat_id=message.chat.id)['access_hash_rec']
			
			print(rubika_bot.send_Photo(set_file_inline('video.mp4','mp4',access_hash_rec,upload_data,len(video)),guid))
			delete_file('video.mp4')
			
			
		elif(message.content_type=='photo'):
			photo = save_photo(message)
			upload_data = json.loads(rubika_bot.requestSendFile('photo.jpg',len(photo),'jpg'))['data']
			access_hash_rec = rubika_bot.upload_file(photo,upload_data)['access_hash_rec']
			print(rubika_bot.send_Photo(set_file_inline('photo.jpg','jpg',access_hash_rec,upload_data,len(photo)),guid))
			delete_file('photo.jpg')
			
			
		elif(message.content_type == 'video'):
			video = save_video(message)
			upload_data = json.loads(rubika_bot.requestSendFile('video.mp4',len(video),'mp4'))['data']
			access_hash_rec = rubika_bot.upload_file(video,upload_data,telegram_bot_token=token,chat_id=message.chat.id)['access_hash_rec']
			print(rubika_bot.send_Photo(set_file_inline('video.mp4','mp4',access_hash_rec,upload_data,len(video)),guid))
			delete_file('video.mp4')
			
			
			
	except Exception as e:
				telgram_bot.reply_to(message,str(e))
				
			
	
telgram_bot.polling()





