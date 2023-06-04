import json
from flask import Flask,render_template
import requests 


def send_request(stock):
        response = requests.get(
            url=f"https://api.tickertape.in/stocks/info/{stock}",
            headers={
                "Host": "api.tickertape.in",
                "Connection": "keep-alive",
                "sec-ch-ua": "\"Brave\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
                "Accept": "application/json, text/plain, */*",
                "accept-version": "7.11.0",
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                "sec-ch-ua-platform": "\"macOS\"",
                "Sec-GPC": "1",
                "Accept-Language": "en-GB,en",
                "Origin": "https://www.tickertape.in",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Accept-Encoding": "gzip, deflate, br",
                "Cookie": "ttk_prefer_broker=kite; scnm=Sandeep; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2MmMyYTQxMmFmYjViNzlhYjMyM2I3ZTUiLCJjc3JmVG9rZW4iOiI2ZGZjM2U4ZSIsInJlZnJlc2hUb2tlbiI6ImI4OTRhYjQwLTg5YzYtNGVhYi04MWRlLWMyODU0OWY5MzAyNV82NDJjODA5Y2YxNzBjNzJlZTAwNDFlNjgiLCJzdWJzSWQiOiJCMDAxIiwiaWF0IjoxNjgwNjM4MTA4LCJleHAiOjE2ODA2Mzg3MDd9.AgLjzole-9773TFL7KpvZaVbJqX6Nw0aXUfpvHqCnHo; x-lp-tk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbiI6ZmFsc2UsImlhdCI6MTY4NTkwMDIwMSwiZXhwIjoxNjg1OTI5MDAxfQ.F2YB2iT0_N6sDFl2EFBjLkLQBBZ4prW_JH7NxFpEaa8; x-lp-auth=6403a64b110198e4415d9732d4895da085921caabac37004fe26bf14e956e051",
            },
        )
        return response
        





app = Flask(__name__)

@app.route('/')
def hello():
    name = ["VARB"]
    response = send_request(name[0])
    return render_template('index.html',data=response.json(),name=name)
    

if __name__ == '__main__':
    app.run(debug=True,port=5550)
