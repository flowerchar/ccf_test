 
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

    def post_message(self, data):
        '''
        发帖接口
        :return:
        '''
        post_url = f"{self.base_url}/posts"
        req = {
            "method": "POST",
            "url": post_url,
            "json": data,
            "headers": {
                "Accept": "application/json"
            }
        }
        r = self.send_api(req)
        return r

    def delete_message(self, data):
        '''
        删除帖子接口
        :return:
        '''
        delete_url = f"{self.base_url}/delete"
        req = {
            "method": "DELETE",
            "url": delete_url,
            "json": data,
            "headers": {
                "Accept": "application/json"
            }
        }
        r = self.send_api(req)
        return r

    def put_message(self, data):
        '''
        更新帖子接口
        :return:
        '''
        put_url = f"{self.base_url}/put"
        req = {
            "method": "PUT",
            "url": put_url,
            "json": data,
            "headers": {
                "Accept": "application/json"
            }
        }
        r = self.send_api(req)
        return r