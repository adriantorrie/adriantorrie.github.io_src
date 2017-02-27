import pandas as pd
import requests as r
import xml.etree.cElementTree as etree

class Client():
    # class variables
    _web_service = 'http://ws.eoddata.com/data.asmx'
    _namespace ='http://ws.eoddata.com/Data'
    
    def __init__(self, username, password):
        # instance variables
        self._session = r.Session()
        self._token = self._login(username, password)
        
    def _web_call(self, call, kwargs, pattern=None):
        url = '/'.join((self._web_service, call))
        response = self._session.get(url, params=kwargs, stream=True)

        if response.status_code == 200:
            if pattern==None:
                return etree.parse(response.raw).getroot()
            else:
                root = etree.parse(response.raw).getroot()
                elements = root.findall(pattern %(self._namespace))
                items = [element.items() for element in elements]
                
                temp = []
                for item in items:
                    temp.append(dict(item))
                
                return pd.DataFrame(temp)
    
    def _login(self, username, password):
        call = 'Login'
        kwargs = {'Username': username, 'Password': password}

        root = self._web_call(call, kwargs)
        return root.get('Token')
            
    # -------------------------------------------------------------------------
    # visible functions
    def close_session():
        self._session.close(self)
        
    def get_session(self):
        return self._session
    
    def get_web_service(self):
        return self._web_service
        
    def get_namespace(self):
        return self._namespace
            
    def get_token(self):
        return self._token
        
    def get_exchange_list(self):
        call = 'ExchangeList'
        kwargs = {'Token': self._token,}
        pattern = ".//{%s}EXCHANGE"
        
        return self._web_call(call, kwargs, pattern)
        
    def get_exchange_codes(self):
        return list(self.get_exchange_list()['Code'])

