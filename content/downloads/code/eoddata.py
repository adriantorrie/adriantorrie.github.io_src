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
        """Makes the call to the web sevice.
        
        Args:
         - call    string    Name of the webservice call to make
         - *kwargs dict      Has the parameter payload (key-value pairs)
                             the web service call expects. Will typically
                             require a token (string) to be passed in.
         - pattern string    The pattern to search for in the returned
                             XML. When None, this will assume a login
                             call is being made, as all other responses
                             will provide an XML response.
        """
        url = '/'.join((self._web_service, call))
        response = self._session.get(url, params=kwargs, stream=True)

        # 200 is a successfull http response
        if response.status_code == 200:
            
            # if no pattern is provided to search for then the raw
            # response is returned
            if pattern==None:
                return etree.parse(response.raw).getroot()
            
            # search for the pattern and return a pandas DataFrame
            else:
                root = etree.parse(response.raw).getroot()
                elements = root.findall(pattern %(self._namespace))
                items = [element.items() for element in elements]
                
                temp = []
                for item in items:
                    temp.append(dict(item))
                
                return pd.DataFrame(temp)
    
<<<<<<< Updated upstream
    def _login(self, username, password):
        call = 'Login'
        kwargs = {'Username': username, 'Password': password}

        root = self._web_call(call, kwargs)
        return root.get('Token')
            
=======
    def _get_token(self, username=None, password=None):
        # get credentials from file if none are passed in
        if username == None and password == None:
            credentials_file_path = os.path.join(os.path.expanduser('~'), '.eoddata', 'credentials')
            
            # test permissions are 0600 (ONLY user can read/write)
            # do this to ensure the credentials file hasn't been
            # compromised
            if (os.path.exists(credentials_file_path) and
                oct(os.stat(credentials_file_path).st_mode)[-3:] == '600'):
                try:
                    with open(credentials_file_path) as f:    
                        credentials = json.load(f)
                        username = credentials['username']
                        password = credentials['password']
                finally:
                    del credentials
        
        # login to return token 
        try:
            call = 'Login'
            kwargs = {'Username': username, 'Password': password}
        finally:
            del username
            del password

        root = self._web_call(call, kwargs)
        return root.get('Token')
    
    def _get_exchange_codes(self):
        return list(self.exchange_list()['Code'])

>>>>>>> Stashed changes
    # -------------------------------------------------------------------------
    # external functions
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
<<<<<<< Updated upstream
        
    def get_exchange_list(self):
=======
    
    def get_exchange_codes(self):
        return self._exchange_codes
      
    # -------------------------------------------------------------------------
    # external functions for the client
    def country_list(self):
        call = 'CountryList'
        kwargs = {'Token': self._token,}
        pattern = ".//{%s}CountryBase"
        
        return self._web_call(call, kwargs, pattern)
    
    def exchange_list(self):
>>>>>>> Stashed changes
        call = 'ExchangeList'
        kwargs = {'Token': self._token,}
        pattern = ".//{%s}EXCHANGE"
        
        return self._web_call(call, kwargs, pattern)
        
    def get_exchange_codes(self):
        return list(self.get_exchange_list()['Code'])

