import requests
headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/json',
    'X-Auth-Token': 'jtgyB8eVf0xCsHsXF4wyAmDmbweI3mDaDFW3j4yZ'
}
a = requests.get(url='https://www.yuque.com/api/v2/users/u22709359',
            headers=headers).json()
print(a)