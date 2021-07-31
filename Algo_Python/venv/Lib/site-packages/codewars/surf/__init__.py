import aiohttp

class Surfer(object):
    """Library to surf the web in ASYNC style
    This class is designed to execute multiple request without pauzing /
    stopping the code.
    """

    def __init__(self, loop = None):
        """This class needs a `event loop` from asyncio in order to work.

        Parameter
        ---------
        loop
            Object: Asyncio event loop.
            Description: The asyncio event loop can be created with the following snippet
                `asyncio.get_event_loop()`

        Note
        ----
        Initialize this class only ONCE if you'are planning to use it.
        """
        if loop is None: raise AttributeError("The asyncio get_event_loop is missing. Surfer is unable to surf.")
        else: self.__loop = loop
    
    async def __request_get(
        self,
        url: str,
        header: dict,
        auth: tuple,
        json: bool,
        decode: bool,
        timeout : int
        ):
        timeout = aiohttp.ClientTimeout(total=timeout)
        if json: header["accept"] = "application/json"
        if auth: auth_session = aiohttp.ClientSession(auth=aiohttp.BasicAuth(*auth), timeout=timeout)
        else: auth_session = aiohttp.ClientSession(timeout=timeout)
        async with auth_session as session:
            async with session.get(url, headers=header) as response:
                if json and decode:
                    return (response.status, await response.json(encoding='utf8'))
                elif json and decode == False:
                    return (response.status, await response.json())
                else:
                    return (response.status, await response.read())

    def get(self,
        url: str = None,
        header: dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            },
        auth: tuple = (),
        json: bool = False,
        decode: bool = False,
        timeout: int = 5
        ):
        """Execute a GET request

        Parameters
        ----------
        url
            Default: None
            Type: str
            Description: The request url
        
        header
            Default: Mozilla user agent
            Type: Dict
            Description: The headers of your request in key, value format

        Auth
            Default: ()
            Type: Tuple
            Description: (Username : str, Password : str)
        
        json
            Default: False
            Type: Bool
            True: Returns json format
            False: Returns string format

        decode
            Default: False
            Type: Bool
            True: Decode json format to utf8
            False: Skips this step

        timeout
            Default: 5
            Type: int
            Description: Stops the request after timeout hit X seconds

        Note
        ----
        The parameter `decode` is useful for some websites / apis. Most of the
        time you do not need this option. But if a request still returns encoded
        data after a solid json request, then you might consider to turn this
        option on.

        Returns
        -------
        Response
            Type: Tuple
            Content: (Response Status Code : int, Response Data, )
            Description: The response data depends on the settings provided.
        """
        if url is None: raise AttributeError('Did you forget to assign a url?')
        return self.__loop.run_until_complete(self.__request_get(
            url=url, header=header, auth=auth, json=json, decode=decode, timeout=timeout))

    async def __request_post(
        self,
        url: str,
        header: dict,
        auth: tuple,
        data: dict,
        json: bool,
        decode: bool,
        timeout : int
        ):
        timeout = aiohttp.ClientTimeout(total=timeout)
        if data.keys(): header["Content-Type"] = "application/json"
        if auth: auth_session = aiohttp.ClientSession(auth=aiohttp.BasicAuth(*auth), timeout=timeout)
        else: auth_session = aiohttp.ClientSession(timeout=timeout)
        async with auth_session as session:
            async with session.post(url, headers=header, data=data) as response:
                if json and decode:
                    return (response.status, await response.json(encoding='utf8'))
                elif json and decode == False:
                    return (response.status, await response.json())
                else:
                    return (response.status, await response.read())

    def post(self,
        url: str = None,
        header: dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            },
        auth: tuple = (),
        data: dict = {},
        json: bool = False,
        decode: bool = False,
        timeout: int = 5,
        ):
        """Execute a POST request

        Parameters
        ----------
        url
            Default: None
            Type: str
            Description: The request url
        
        header
            Default: Mozilla user agent
            Type: Dict
            Description: The headers of your request in key, value format

        Auth
            Default: ()
            Type: Tuple
            Description: (Username : str, Password : str)
        
        data
            Default: Empty dict
            Type: Dict
            Description: The date you would like to post

        json
            Default: False
            Type: Bool
            True: Returns json format
            False: Returns string format

        decode
            Default: False
            Type: Bool
            True: Decode json format to utf8
            False: Skips this step

        timeout
            Default: 5
            Type: int
            Description: Stops the request after timeout hit X seconds

        Note
        ----
        The parameter `decode` is useful for some websites / apis. Most of the
        time you do not need this option. But if a request still returns encoded
        data after a solid json request, then you might consider to turn this
        option on.

        Returns
        -------
        Response
            Type: Tuple
            Content: (Response Status Code : int, Response Data, )
            Description: The response data depends on the settings provided.
        """
        if url is None: raise AttributeError('Did you forget to assign a url to the surfer?')
        return self.__loop.run_until_complete(self.__request_post(
            url=url, header=header, auth=auth, data=data, json=json, decode=decode, timeout=timeout))
