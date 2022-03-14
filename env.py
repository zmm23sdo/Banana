import os

def envClient():
    env = os.getenv('env')
    if env == 'T':
        URL = 'https://client-banana-test.chunsutech.com/'
    elif env == 'P':
        URL = 'client_product'
    else:
        URL = 'https://client-banana-dev.chunsutech.com/'
    return URL

def envAdmin():
    env = os.getenv('env')
    if env == 'T':
        URL = 'https://admin-banana-test.chunsutech.com/'
    elif env == 'P':
        URL = 'admin_product'
    else:
        URL = 'https://admin-banana-dev.chunsutech.com/'
    return URL

admin_Url = envAdmin()
client_Url = envClient()
# print(f'admin Url: {admin_Url}')
# print(f'client Url: {client_Url}')