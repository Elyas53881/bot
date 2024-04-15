from os import system
import Config
import enc
import json
import io
import base64

try:
	import requests
except:
	system('pip install requests')
	import requests 
#try:
#	import PIL
#except:
#	system('pip install pillow')
#	import PIL.Image
#	


auth = Config.auth
private_key = Config.private_key
server_link = Config.server_link

encryption = enc.rubika(auth=auth,Private_key=private_key)

def create_json_send(_auth,_data_enc,_sign):
		 _data_send = {
	    "api_version": "6",
    "auth": encryption.changeAuthType(_auth),
    "data_enc": _data_enc,
    "sign":_sign
	}
		 return json.dumps(_data_send)

def post_data(_data):
		data = json.loads(_data)
		response = requests.post(server_link,json=data)
		return response.text

def method_runner(_method):
	_data_enc = encryption.encrypt(json.dumps(_method))
	_sign = encryption.makeSignFromData(data_enc=_data_enc)
	_data_for_send = create_json_send(_auth=auth,_data_enc=_data_enc,_sign=_sign)
	return encryption.decrypt(json.loads(post_data(_data=_data_for_send))['data_enc'])
	

#def getThumbInline(image_bytes: bytes) -> str:
#        
#        
#        im, output = PIL.Image.open(io.BytesIO(image_bytes)), io.BytesIO()
#        width, height = im.size
#        im.save(output, format='PNG')
#        im_data = output.getvalue()
#        image_data = base64.b64encode(im_data)
#        if not isinstance(image_data, str):
#            image_data = image_data.decode()
#        return image_data

# 
#def getImageSize(image_bytes: bytes) -> list:
#        
#        im = PIL.Image.open(io.BytesIO(image_bytes))
#        width, height = im.size
#        return [width, height]

