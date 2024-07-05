"""
 
"""
from interface_auto.interface_frame.apis.ceshiren import Ceshiren


class CeshirenSearch(Ceshiren):

    def search(self, data):
        '''
        搜索接口
        :return:
        '''
        search_url = f"{self.base_url}/search"
        req = {
            "method": "GET",
            "url": search_url,
            "params": data,
            "headers": {
                "Accept": "application/json"
            }
        }
        r = self.send_api(req)
        return r