import argparse

import requests
from flask import *

b2b_server = Flask('B2B SERVER')


def get_url(roomid, source):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'
    }
    response = requests.get(
        'http://api.live.bilibili.com/room/v1/Room/playUrl?cid='
        f'{roomid}&quality=4&platform=web',
        headers=headers)
    if response.status_code == 200:
        stream_url = response.json()['data']['durl'][source]['url'].replace(
            '\\u0026', '&')
        return stream_url
    return None


@b2b_server.route('/player/<int:roomid>')
def on_player(roomid):
    source = 0
    if 'source' in request.args:
        source = int(request.args['source'])
    return render_template(
        'index.html',
        roomid=roomid,
        url=get_url(roomid, source)
    )


@b2b_server.route('/<int:roomid>')
def on_stream(roomid):
    source = 0
    if 'source' in request.args:
        source = int(request.args['source'])
    url = get_url(roomid, source)
    if url is not None:
        return redirect(url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="B2B Python")
    parser.add_argument('-p', '--port', nargs='?', default=5000,
                        help='设定B2B Python运行的端口,默认为5000')
    args = parser.parse_args()
    b2b_server.run(host='0.0.0.0', port=args.port)
