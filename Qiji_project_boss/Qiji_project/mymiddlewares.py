from Qiji_project import settings
import random
class FreeRandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(settings.PROXIES)
        request.meta['proxy'] = 'http://'+ proxy['host']