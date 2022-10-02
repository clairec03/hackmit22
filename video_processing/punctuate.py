# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "http://bark.phon.ioc.ee/punctuator"
  
# your API key here
API_KEY = "14166869651028217730222362070"
  
# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''
  
# data to be sent to api
data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'python'}

headers = {'Content-Type': 'multipart/form-data; boundary=---------------------------14166869651028217730222367000'}
	
data = "----------------------------14166869651028217730222367000\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\nRevolution is often the easy part I mean you think destroying a death star is hard trying negotiating a trade treaty with gun guns right anyway so the late 20th century was not the first time that Empire is disintegrated Rome comes to mind also the Persians and of course the American Revolution ended one kind of European Imperial experiment but in all those cases Empire struck back you see what I did that I mean Britain lost its 13 colonies but later controlled half of Africa and all of India and what makes the recent decolonization so special is that at least so far no empires have emerged to replace the ones that fell and this was largely due to World War Two because on some level the Allies were fighting to stop Nazi imperialism Hitler wanted to take over Central Europe and Africa and probably the Middle East and the Allied defeat of the Nazis discredited the whole idea of Empire so the English French and Americans couldn't very well say to the Colonial \r\n-----------------------------14166869651028217730222367000--\r\n"
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data, headers=headers)
  
# extracting response text 
print(r)
pastebin_url = r.text
print(r.json)
print(r.text)
print(r.headers)
print(r.content)
print("The pastebin URL is:%s"%pastebin_url)