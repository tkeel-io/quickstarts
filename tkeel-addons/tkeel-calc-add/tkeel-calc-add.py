from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/v1/identify', methods=['GET'])
def identify():
    print("identify", flush=True)
    return jsonify(
        {
            "res": {
                "ret": 0,
                "msg": "ok"
            },
            "plugin_id": "tkeel-calc-add",
            "verison": "v0.0.1",
            "tkeel_version": "v0.4.0",
            "implemented_plugin": [
                {
                    "plugin": {
                        "id": "tkeel-calc",
                        "version": "v0.0.1",
                    },
                    "addons": [
                        {
                            "addons_point": "calc-int-x-y",
                            "implemented_endpoint": "add"
                        }
                    ]
                }
            ]
        }
    )


@app.route('/v1/status', methods=['GET'])
def status():
    print("status", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}, "status": 3})


@app.route('/v1/tenant/enable', methods=['GET'])
def tenant_bind():
    print("tenant/bind", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}})


@app.route('/v1/tenant/disable', methods=['GET'])
def tenant_unbind():
    print("tenant/unbind", flush=True)
    return jsonify({"res": {"ret": 0, "msg": "ok"}})


@app.get('/add')
def add():
    x = request.args.get(key="x", type=int)
    y = request.args.get(key="y", type=int)
    print(x, flush=True)
    print(y, flush=True)
    header = {}
    for k, v in request.headers.items():
        if k == "Content-Length":
            continue
        header[k] = v
    return jsonify({"code": "io.tkeel.SUCCESS", "msg": "", "data": {"z": f'{x+y}'}})


@app.route('/hello', methods=['GET'])
def hello():
    print("hello", flush=True)
    return jsonify({"code": "io.tkeel.SUCCESS", "msg": "", "data": {"msg": "hello tkeel cal add"}})


if __name__ == '__main__':
    app.run(port=8080)
