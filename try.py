import requests
headers = {
    'Authorization': 'Token 30f315c042f91326b62f2557b14ceb81ec1b8093'
    
    }
url = "http://127.0.0.1:8000/api/profile"
payload = ""
response = requests.get(url, headers=headers, )
print(response.text)
