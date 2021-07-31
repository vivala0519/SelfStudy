from codewars.surf import Surfer
import unittest, asyncio

class TestSurf(unittest.TestCase):

    def setUp(self):
        """Executes before EACH test"""
        self.surf = Surfer(asyncio.get_event_loop())

    def tearDown(self):
        """Executes after EACH test"""
        del self.surf

    def test_ReadHTML(self):
        data = self.surf.get(
            url='http://httpbin.org/ip'
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            type(data[1]),
            bytes,
            "The webpage did not returned bytes"
        )
    
    def test_ReadJSON(self):
        data = self.surf.get(
            url='http://httpbin.org/ip',
            json=True
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            type(data[1]),
            dict,
            "The webpage did not returned valid JSON"
        )
    
    def test_UserAgentHTML(self):
        data = self.surf.get(
            url='http://httpbin.org/user-agent'
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            b'{\n  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"\n}\n',
            "The webpage did not returned our User-Agent"
        )
    
    def test_UserAgentJSON(self):
        data = self.surf.get(
            url='http://httpbin.org/user-agent',
            json=True
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'},
            "The webpage did not returned valid JSON User-Agent"
        )
    
    def test_HeaderHTML(self):
        data = self.surf.get(
            url='http://httpbin.org/headers'
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            type(data[1]),
            bytes,
            "The webpage did not returned our headers"
        )
    
    def test_HeaderJSON(self):
        data = self.surf.get(
            url='http://httpbin.org/headers',
            json=True
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            {'headers': {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}},
            "The webpage did not returned valid JSON headers"
        )

    def test_PostJSON(self):
        data = self.surf.post(
            url='http://httpbin.org/post',
            header={'api_key': 'special-key'},
            data={
                "id": 0x78f1935,
                "username": "codewars",
            },
            json=True
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            {'args': {}, 'data': 'id=126818613&username=codewars', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Api-Key': 'special-key', 'Content-Length': '30', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'Python/3.6 aiohttp/3.5.4'}, 'json': None, 'origin': '80.115.74.192, 80.115.74.192', 'url': 'https://httpbin.org/post'},
            "The webpage did not returned valid JSON post"
        )

    def test_BasicAUTH(self):
        data = self.surf.get(
            url='http://httpbin.org/basic-auth/test/test1123',
            auth=('test', 'test1123'),
            json=True
            )

        self.assertEqual(
            data[0],
            200,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            {'authenticated': True, 'user': 'test'},
            "Could not connect with basic authentication"
        )

    def test_BasicUNAUTH(self):
        data = self.surf.get(
            url='http://httpbin.org/basic-auth/test/test1123',
            auth=('test', 'test11234'),
            json=False
            )

        self.assertEqual(
            data[0],
            401,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            data[1],
            b'',
            "Could not connect with basic authentication"
        )