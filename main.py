import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params, timeout=5)
        dic = response.json()
        response = requests.put(dic['href'], data=open(file_path, 'rb'), headers=headers, timeout=5)
        print(response)

if __name__ == '__main__':
    path_to_file = '1.txt'
    token = ''

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

