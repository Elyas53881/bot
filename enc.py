from os import system
from base64 import b64encode as b64e, urlsafe_b64decode as b64d, b64decode
import json
try:
	 from Crypto.Util.Padding import pad, unpad
	 from Crypto.Cipher import AES
	 from Crypto.Hash import SHA256
	 from Crypto.Signature import pkcs1_15
	 from Crypto.PublicKey import RSA
	 
except:
	system('pip install pycryptodome')
	from Crypto.Util.Padding import pad, unpad
	from Crypto.Cipher import AES
	from Crypto.Hash import SHA256
	from Crypto.Signature import pkcs1_15
	from Crypto.PublicKey import RSA
	



class rubika:
	
	def __init__(self,auth,Private_key:str):
		self.private_key = None
		self.auth_send = None
		self.orginal_auth = auth
		
		
		if auth != None:
			#check and set auth
			if len(auth) == 32 :
				self.key = auth
				
				
				self.auth_send = self.changeAuthType(auth)
				
				#set auth
				self.key = bytearray(self.secret(self.key),'utf-8')
				
			
			
				
				self.private_key = RSA.import_key('-----BEGIN RSA PRIVATE KEY-----\n'+ Private_key+ '\n-----END RSA PRIVATE KEY-----')
				
				
			else:
				print(color.red,'invalid auth')
		else:
			print(color.red,'Please enter the auth !')
			
	
			
	def secret(self,e):
	       t, n, s = e[0:8], e[16:24] + e[0:8] + e[24:32] + e[8:16], 0
	       while s < len(n):
	           e = n[s]
	           if e >= '0' and e <= '9':
	               t = chr((ord(e[0]) - ord('0') + 5) %10 + ord('0'))
	               n = self.replaceCharAt(n, s, t)
	           else:
	               t = chr((ord(e[0]) - ord('a') + 9) %26 + ord('a'))
	               n = self.replaceCharAt(n, s, t)
	           #
	           s += 1
	       return n
        
	def replaceCharAt(self, e, t, i):
		return e[0:t] + i + e[t + len(i):]
	
	def encrypt(self,text):
		raw = pad(text.encode('UTF-8'), AES.block_size)
		iv = bytearray.fromhex('0' * 32)
		aes = AES.new(self.key, AES.MODE_CBC, iv)
		enc = aes.encrypt(raw)
		result = b64e(enc).decode('UTF-8')
		return result
		
	def decrypt(self,text):
	       iv = bytearray.fromhex('0' * 32)
	       aes = AES.new(self.key, AES.MODE_CBC, iv)
	       dec = aes.decrypt(b64d(text.encode('UTF-8')))
	       result = unpad(dec, AES.block_size).decode('UTF-8')
	       return result
	       
	       
	       
	       
	  
	def makeSignFromData(self,data_enc:str):
	       sha_data = SHA256.new(data_enc.encode('UTF-8'))
	       signature = pkcs1_15.new(self.private_key).sign(sha_data)
	       return b64e(signature).decode('UTF-8')
	       
	       
	       
	    
	def changeAuthType(self, auth_enc):
	       n = ''
	       lowercase = 'abcdefghijklmnopqrstuvwxyz'
	       uppercase = 'abcdefghijklmnopqrstuvwxyz'.upper()
	       digits = '0123456789'
	       for s in auth_enc:
	               if s in lowercase:
	               	n += chr(((32 - (ord(s) - 97)) % 26) + 97)
	               elif s in uppercase:
	               	n += chr(((29- (ord(s) - 65)) % 26) + 65)
	               elif s in digits:
	               	n += chr(((13 - (ord(s)- 48)) % 10) + 48)
	               else:
	               		n += s
	       return n
	      

	

	       
	       

	

	
		
		
		
		
		
		
		
		
		
		
class color:
	cyan = "\033[0;36m"
	red = "\033[0;31m"
	green = "\033[0;32m"