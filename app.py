"""story.q-writer.com Proxy"""

from flask import request, Response, Flask
from requests import post

app = Flask(__name__)


@app.route('/', methods=['POST'])
def _proxy(*args, **kwargs):
    resp = requests.post(
        url="https://pelevin.gpt.dobro.ai/generate/",
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


if __name__ == '__main__':
    app.run()
