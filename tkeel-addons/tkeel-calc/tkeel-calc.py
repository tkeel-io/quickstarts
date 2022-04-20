import json
import sys
import requests
from flask import Flask, jsonify, request
app = Flask(__name__)

keel_url = "http://127.0.0.1:3500/v1.0/invoke/keel/method/apis/"

addons_url = "http://127.0.0.1:3500/v1.0/invoke/keel/method/apis/addons/calc-int-x-y"


@app.route('/v1/identify', methods=['GET'])
def identify():
    print("identify", flush=True)
    return jsonify(
        {
            "res": {
                "ret": 0,
                "msg": "ok"
            },
            "plugin_id": "tkeel-calc",
            "verison": "v0.0.1",
            "tkeel_version": "v0.4.0",
            "addons_points": [
                {
                    "addons_point": "calc-int-x-y",
                    "desc": "计算传入的 x 和 y 值,x 和 y 必须是 int。"
                }
            ]
        }
    )


def get_addons(url, x="1", y="1", header={}):
    print("header", header, flush=True)
    try:
        resp = requests.get(
            url=f'{url}?x={x}&y={y}',
            headers=header
        )
        json_data = resp.json()
        print("addons response: ", json_data, flush=True)
        if json_data["code"] != "io.tkeel.SUCCESS":
            return False
        if "z" not in json_data["data"]:
            return False
        return json_data["data"]["z"]
    except:
        print("Unexpected error: ", sys.exc_info()[0])
    return False


@ app.route('/v1/addons/identify', methods=['POST'])
def addons_identify():
    print("addons_identify", flush=True)
    jsData = json.loads(request.get_data())
    print(jsData, flush=True)
    pluginInfo = jsData["plugin"]
    pid = pluginInfo["id"]
    endpoint = jsData["implemented_addons"]
    if endpoint[0]["addons_point"] == "calc-int-x-y":
        endpoint = endpoint[0]["implemented_endpoint"]
        header = {}
    for k, v in request.headers.items():
        if k == "Content-Length":
            continue
        header[k] = v
    if get_addons(url=f'{keel_url}{pid}/{endpoint}', header=header) != False:
        return jsonify({"res": {"ret": 0, "msg": "ok"}})
    return jsonify({"res": {"ret": -1, "msg": "invaild request"}})


@ app.route('/v1/status', methods=['GET'])
def status():
    print("status", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}, "status": 3})


@ app.route('/v1/tenant/enable', methods=['GET'])
def tenant_bind():
    print("tenant/bind", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}})


@ app.route('/v1/tenant/disable', methods=['GET'])
def tenant_unbind():
    print("tenant/unbind", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}})


@ app.get('/calc')
def calc():
    try:
        x = request.args.get(key="x", type=int)
        y = request.args.get(key="y", type=int)
    except ValueError:
        return jsonify({"res": "invaild args type"})
    except:
        return jsonify({"res": f"Unexpected error: {sys.exc_info()[0]}"})
    else:
        print(x, flush=True)
        print(y, flush=True)
        queryStr = str(request.query_string, encoding="utf-8")
        header = {}
        for k, v in request.headers.items():
            if k == "Content-Length":
                continue
            header[k] = v
        print({"query_string": queryStr}, flush=True)
        res = get_addons(url=addons_url,
                         x=request.args.get(key="x"), y=request.args.get(key="y"), header=header)
        if res == False:
            return jsonify({"code": "io.tkeel.INTERNAL_ERROR", "msg": "invaild addons calc-int-x-y", "data": {}})
        return jsonify({"code": "io.tkeel.SUCCESS", "msg": "", "data": {"res": f'{res}'}})


@ app.route('/hello', methods=['GET'])
def hello():
    print("hello", flush=True)
    return jsonify({"code": "io.tkeel.SUCCESS", "msg": "", "data": {"msg": "hello tkeel cal"}})


if __name__ == '__main__':
    app.run(port=8080)
