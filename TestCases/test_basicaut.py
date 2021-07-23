import requests
from requests.auth import HTTPBasicAuth


#basic authentication
#api cannot use directly we need to send usrname and pswd amd access
def test_with_authentication():
    response = requests.get(r'http://github.com/user', auth=HTTPBasicAuth('rikurinka','Kgshema!901'))
    print(response.text)
