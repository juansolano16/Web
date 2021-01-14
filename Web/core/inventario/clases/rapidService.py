import requests
import json


class rapidServiceC():
    mail = 'tecnologia@mastermoto.com.ec'
    password = '1792181364001'

    def login(self):
        try:
            url = "https://www.rapidservice.com.ec/api/user/login"
            #payload = "{\"mail\":\"" + self.mail + "\",\"pass\":\"" + self.password + "\"}"
            param = {'mail': self.mail,'pass': self.password}
            payload = json.dumps(param)
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload)
            data = json.loads(response.text)
        except Exception as e:
            data = {'error': str(e)}
        return data

    def getProductos(self, token, cookie):
        try:
            url = "https://www.rapidservice.com.ec/api/productosfijos"
            payload = {}
            headers = {'X-CSRF-Token': token, 'Cookie': cookie}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.text)
        except Exception as e:
            data = {'error': str(e)}
        return data

    def guia(self, token, cookie):
        try:
            url = "https://www.rapidservice.com.ec/api/productosfijos"
            payload = {}
            headers = {'X-CSRF-Token': token, 'Cookie': cookie}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.text)
        except Exception as e:
            data = {'error': str(e)}
        return data

    def estadoGuia(self, qr):
        try:
            url = "https://www.rapidservice.com.ec/api/wsrastreo?field_qr_value=" + qr
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.text)
        except Exception as e:
            data = {'error': str(e)}
        return data

    def loguot(self, token, cookie):
        try:
            url = "https://www.rapidservice.com.ec/api/user/logout"
            payload = {}
            files = {}
            headers = {'X-CSRF-Token': token, 'Cookie': cookie}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            data = json.loads(response.text)
        except Exception as e:
            data = {'error': str(e)}
        return data
