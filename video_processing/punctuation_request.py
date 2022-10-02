import requests
def punctuate(text):
    url = "http://bark.phon.ioc.ee/punctuator"

    data='text=' + str(text)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=data)

    return response.text 
