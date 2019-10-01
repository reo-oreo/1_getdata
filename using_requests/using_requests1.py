import requests

#リクエスト情報
payload={'key1':'value1','key2':'value2'}

def test(url):

    r = requests.get(url)
    print("ステータスコード",r.status_code)
    print("レスポンスヘッダ",r.headers)
    print("content-typeのヘッダ",r.headers['content-type'])
    print("encoding",r.encoding)
    print("Text",r.text)
    print("Json",r.json())


def post_test(url,payload):

    r=requests.get(url,params=payload)
    print("ステータスコード",r.status_code)
    print("レスポンスヘッダ", r.headers)
    print("content-typeのヘッダ",r.headers['content-type'])
    print("encoding",r.encoding)
    print("Text",r.text)
    print("Json",r.json())

def session(url):
    s=requests.Session()
    s.get(url)
    r=s.get("http://httpbin.org/cookies")
    print(r.text)


if __name__ == '__main__':
    # post_test("https://weather.yahoo.co.jp/weather/",payload)
    url="http://httpbin.org/cookies/set/sessioncookie/123456789"
    session(url)






#URL
#https://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/
#https://requests-docs-ja.readthedocs.io/en/latest/user/advanced/



