import requests

class APIdemo:
    def do_get(self,url,params=None,headers=None,**kwargs):
        return requests.get(url=url,params=params,headers=headers,**kwargs)


    def do_post(self,url,data=None,headers=None,**kwargs):
        return requests.post(url=url,data=data,headers=headers,**kwargs)