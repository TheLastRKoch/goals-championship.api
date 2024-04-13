import requests


class UtilWebRequest():

    def __base_request(self, method, headers, parameters, url, body):
        return requests.request(
            method=method,
            headers=headers,
            params=parameters,
            url=url,
            data=body
        )

    def get(self, headers, parameters, url, body):
        return self.__base_request("GET", headers, parameters, url, body)

    def check_auth(self, headers, parameters, url, body):
        r = self.__base_request("GET", headers, parameters, url, body)
        if r.status_code // 10 == 20:
            return True
        return False
