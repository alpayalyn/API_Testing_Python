import requests

# 'visit-month'
# There are 2 different examples, first one;
# -> There won't be any response due to the website except 200. So in the second one we will be getting Some Response JSON Data.
# -> Main difference is Second one is SESSION BASED, though.
cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com', cookies=cookie)
print(response.status_code)

# SESSION BASED.
# We have an ENDPOINT which Returns the coookies written as A RESPONSE!!!! Unlike the one above.

sessionn = requests.session()
sessionn.cookies.update({'visit-month':'February'})
response = sessionn.get("https://httpbin.org/cookies",allow_Redirects=False, cookies={'visit-year':'2022'}, timeout=1)
# by writing TIMEOUT=1 it will wait 1 sec and then it will give the response for HEAVY LOAD webpages.
# request gönderilirken, 200'e düşmeden önce ilgili website yönelmeden önce başka bir URL'e redirect olabiliyor.
# Bu durumda kodumuzun içeriğine, print(response.history) ile "301" kodu var mı yok mu kontrol edebiliyoruz.
# request.get içerisine allow_Redirects=False yaparak da 301'in süreç içerisinde yer almasını engelliyoruz.
print(response.history)
print(response.status_code)
print(response.text)

# ATTACHMENTS SENDING FILE

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file':open('C:\\Users\\....','rb')}
r = requests.post(url,files=files)
print(r.status_code)
print(r.text)