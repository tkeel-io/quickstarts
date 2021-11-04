## 🚪 快速入门
Core 是 tKeel 的一个重要基础组件，也拥有单独部署能力，使用相关特性做满足广大用户需求的功能也是我们竭力想要的。

### 安装需要
🔧 在使用 Core 之前请先确保你做足了准备。 
1. [Kubernetes](https://kubernetes.io/)
2. [Dapr with k8s](https://docs.dapr.io/getting-started/)


### 通过 tKeel 安装
Core 作为 tKeel 的基础组件，相关 API 的调用均通过 keel 代理实现。（详细请见[tKeel CLI 安装文档](https://github.com/tkeel-io/cli ))

![img.png](img/core-invoke.png)

外部程序可以通过keel代理调用core的API接口，通过设备接入提供的mqtt broker发送数据，从core订阅的数据会写入pubsub，subclient消费pubsub的数据。

keel有两种访问形式。  
#### 外网流量访问

```
KEEL_NODE_PORT=30777 # 如果有更改请查看keel的chart中plugin_components.pluginPort变量
curl http://$NODE_ID:$KEEL_NODE_PORT/$VERSION/$PLUGIN_ID/$METHOD
```
 
#### 内部流量访问
1. 直接访问  
    ```bash
    curl http://keel:$PORT/$VERSION/$PLUGIN_ID/$METHOD
    ```
2. dapr边车访问
    ```bash
    curl http://127.0.0.1:3500/v1.0/invoke/keel/$PLUGIN_ID/$METHOD
    ```
#### 示例
在 tKeel 相关组件安装完成之后，[Python 示例](code/iot-paas.py) 展示了生成 MQTT 使用的 `token`，然后创建实体，上报属性，获取快照，订阅实体的属性等功能。  
为了方便说明，下面是我们使用外部流量方式访问 Keel，和 Python 作为示例语言的代码。我们需要keel和mqtt broker的服务端口用于演示。

##### 1. 下载示例代码
```bash
git clone https://github.com/tkeel-io/quickstarts.git
cd quickstarts/hello-world
```

##### 2. 获取服务IP和端口
1. k8s 部署ip地址
```bash
kubectl get -o jsonpath="{.status.addresses}" node master1
[{"address":"192.168.123.5","type":"InternalIP"},{"address":"master1","type":"Hostname"}]%
```
2. Keel 服务端口
```bash
kubectl get -o jsonpath="{.spec.ports[0].nodePort}" services keel
30707
```
3. MQTT Server 服务端口
```bash
kubectl get -o jsonpath="{.spec.ports[0].nodePort}" services emqx
31875
```
##### 3. 修改相关配置
keel openapi 服务地址为k8s ip:keel暴露的nodeport端口，broker的ip为k8s ip端口为mqtt server的端口。

修改quickstarts/hello-core/code/iot-paas.py文件相关ip和端口
```python
// Source: quickstarts/hello-core/code/iot-paas.py 
keel_url = "http://192.168.123.5:30707/v0.1.0"
broker = "192.168.123.5"
port = 31875
```
##### 4. 运行代码
运行消费pubsub的client，需要先运行client创建订阅使用的pubsub。
```bash
kubectl create -f code/subclient/client.yaml
```
运行iot-paaspy，运行之后会创建相关的token，实体，上报属性。
```bash
python3 code/iot-paas.py

base entity info
entity_id =  iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95
entity_type =  device
user_id =  abc
--------------------------------------------------------------------------------
get entity token
token= eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJrZWVsIiwiZWlkIjoiaW90ZC0wYTdjZjVhZDhjOGY0OTM2YTM3NmI4ZWMyOGJiMWU5NSIsImV4cCI6IjIwMjItMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlhdCI6IjIwMjEtMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlzcyI6Im1hbmFnZXIiLCJqdGkiOiI3MDYyMDRlNS02MGEyLTRiZjYtYjgwNC0zZDU4OTcxM2RhYWMiLCJuYmYiOiIyMDIxLTExLTA0VDAxOjM5OjM4LjcyNjI1MjE4MVoiLCJzdWIiOiJlbnRpdHkiLCJ0aWQiOiIiLCJ0eXAiOiJkZXZpY2UiLCJ1aWQiOiJhYmMifQ.FExemvaZv0xEid0wBVChKi8dnqqWsE4MyadqVhvJzeI7CSvSSTSymLWroFl-zb5cJTsgUVGXNOENU3GabrdQtZLbK2FseME3GOsz33UAIR69--bJRtBbqPASKEOXsmlApRPjL5mGr3sFp5ECaL4rDx-6o52Iz4yqchhROaUEENc
--------------------------------------------------------------------------------
create entity with token
{'id': 'iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95', 'type': 'device', 'owner': 'abc', 'status': 'active', 'version': 1, 'plugin_id': 'pluginA', 'last_time': 1635989979862, 'mappers': None, 'properties': {'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJrZWVsIiwiZWlkIjoiaW90ZC0wYTdjZjVhZDhjOGY0OTM2YTM3NmI4ZWMyOGJiMWU5NSIsImV4cCI6IjIwMjItMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlhdCI6IjIwMjEtMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlzcyI6Im1hbmFnZXIiLCJqdGkiOiI3MDYyMDRlNS02MGEyLTRiZjYtYjgwNC0zZDU4OTcxM2RhYWMiLCJuYmYiOiIyMDIxLTExLTA0VDAxOjM5OjM4LjcyNjI1MjE4MVoiLCJzdWIiOiJlbnRpdHkiLCJ0aWQiOiIiLCJ0eXAiOiJkZXZpY2UiLCJ1aWQiOiJhYmMifQ.FExemvaZv0xEid0wBVChKi8dnqqWsE4MyadqVhvJzeI7CSvSSTSymLWroFl-zb5cJTsgUVGXNOENU3GabrdQtZLbK2FseME3GOsz33UAIR69--bJRtBbqPASKEOXsmlApRPjL5mGr3sFp5ECaL4rDx-6o52Iz4yqchhROaUEENc'}}
create entity iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95 success
--------------------------------------------------------------------------------
create subscription
{'mode': 'realtime', 'source': 'ignore', 'filter': 'insert into abc select iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95.p1', 'target': 'ignore', 'topic': 'abc', 'pubsub_name': 'client-pubsub'}
{'id': 'iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95sub', 'type': 'SUBSCRIPTION', 'owner': 'abc', 'status': 'active', 'version': 1, 'plugin_id': 'pluginA', 'last_time': 1635989981005, 'mappers': None, 'properties': {'filter': 'insert into abc select iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95.p1', 'mode': 'realtime', 'pubsub_name': 'client-pubsub', 'source': 'ignore', 'target': 'ignore', 'topic': 'abc'}}
--------------------------------------------------------------------------------
get subscription
{'id': 'iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95sub', 'type': 'SUBSCRIPTION', 'owner': 'abc', 'status': 'active', 'version': 1, 'plugin_id': 'pluginA', 'last_time': 1635989981005, 'mappers': None, 'properties': {'filter': 'insert into abc select iotd-0a7cf5ad8c8f4936a376b8ec28bb1e95.p1', 'mode': 'realtime', 'pubsub_name': 'client-pubsub', 'source': 'ignore', 'target': 'ignore', 'topic': 'abc'}}
--------------------------------------------------------------------------------
update properties by mqtt
Connected to MQTT Broker!
{"p1": {"value": 25, "time": 1635989984}}
--------------------------------------------------------------------------------
get entity
{'p1': {'time': 1635989984, 'value': 25}, 'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJrZWVsIiwiZWlkIjoiaW90ZC0wYTdjZjVhZDhjOGY0OTM2YTM3NmI4ZWMyOGJiMWU5NSIsImV4cCI6IjIwMjItMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlhdCI6IjIwMjEtMTEtMDRUMDE6Mzk6MzguNzI2MjUyMTgxWiIsImlzcyI6Im1hbmFnZXIiLCJqdGkiOiI3MDYyMDRlNS02MGEyLTRiZjYtYjgwNC0zZDU4OTcxM2RhYWMiLCJuYmYiOiIyMDIxLTExLTA0VDAxOjM5OjM4LjcyNjI1MjE4MVoiLCJzdWIiOiJlbnRpdHkiLCJ0aWQiOiIiLCJ0eXAiOiJkZXZpY2UiLCJ1aWQiOiJhYmMifQ.FExemvaZv0xEid0wBVChKi8dnqqWsE4MyadqVhvJzeI7CSvSSTSymLWroFl-zb5cJTsgUVGXNOENU3GabrdQtZLbK2FseME3GOsz33UAIR69--bJRtBbqPASKEOXsmlApRPjL5mGr3sFp5ECaL4rDx-6o52Iz4yqchhROaUEENc'}
{"p1": {"value": 76, "time": 1635989989}}
```
k8s中运行的client的日志里会打印出订阅的属性数据。
```bash
kubectl logs -f client-98cc866df-mg4wg -c python
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [03/Nov/2021 11:02:14] "GET /dapr/config HTTP/1.1" 404 -
127.0.0.1 - - [03/Nov/2021 11:02:14] "GET /dapr/subscribe HTTP/1.1" 200 -
{'id': '0f8ac498-ad9f-4e6a-bc66-4c2cac4cc3a3', 'specversion': '1.0', 'source': 'core', 'type': 'com.dapr.event.sent', 'pubsubname': 'client-pubsub', 'traceid': '00-b46bd00b53ed6b1f269b47d9ad1e1206-7585025a75b6d58c-00', 'datacontenttype': 'text/plain', 'topic': 'abc', 'data': '{"p1":{"time":1635989984,"value":25}}'}
127.0.0.1 - - [04/Nov/2021 01:39:44] "POST /dsstatus HTTP/1.1" 200 -
{'specversion': '1.0', 'type': 'com.dapr.event.sent', 'topic': 'abc', 'pubsubname': 'client-pubsub', 'traceid': '00-2385b49b92141587108bbbcdb3c11aaf-16ed33df7371137b-00', 'data': '{"p1":{"time":1635989989,"value":76}}', 'id': '31cf5fe0-da42-407f-9d3f-7d7311a7ec06', 'datacontenttype': 'text/plain', 'source': 'core'}
127.0.0.1 - - [04/Nov/2021 01:39:49] "POST /dsstatus HTTP/1.1" 200 -

```

##### 5. 代码说明
###### 创建 token
```python
// Source: examples/iot-paas.py
def create_entity_token(entity_id, entity_type, user_id):
    data = dict(entity_id=entity_id, entity_type=entity_type, user_id=user_id)
    token_create = "/auth/token/create"
    res = requests.post(keel_url + token_create, json=data)
    return res.json()["data"]["entity_token"]
```

###### 创建实体
```python
// Source: examples/iot-paas.py
def create_entity(entity_id, entity_type, user_id, plugin_id, token):
    query = dict(entity_id=entity_id, entity_type=entity_type, user_id=user_id, source="abc", plugin_id=plugin_id)
    entity_create = "/core/plugins/{plugin_id}/entities?id={entity_id}&type={entity_type}&owner={user_id}&source={source}".format(
        **query)
    data = dict(token=token)
    res = requests.post(keel_url + entity_create, json=data)
    print(res.json())
```

###### 上报实体属性
```python
// Source: examples/iot-paas.py
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(entity_id)
client.username_pw_set(username=user_id, password=token)
client.on_connect = on_connect
client.connect(host=broker, port=port)
client.loop_start()
time.sleep(1)
payload = json.dumps(dict(p1=dict(value=random.randint(1, 100), time=int(time.time()))))
client.publish("system/test", payload=payload)
```

###### 获取实体快照
```python
// Source: examples/iot-paas.py
def get_entity(entity_id, entity_type, user_id, plugin_id):
    query = dict(entity_id=entity_id, entity_type=entity_type, user_id=user_id, plugin_id=plugin_id)
    entity_create = "/core/plugins/{plugin_id}/entities/{entity_id}?type={entity_type}&owner={user_id}&source={plugin_id}".format(
        **query)
    res = requests.get(keel_url + entity_create)
    print(res.json()["properties"])

```

###### 订阅实体
运行订阅实体之前，先要创建订阅目的地的pubsub，可以通过运行消费topic的示例yaml创建[消费示例yaml](code/subclient/client.yaml)

```python
// Source: examples/iot-paas.py
def create_subscription(entity_id, entity_type, user_id, plugin_id, subscription_id):
    query = dict(entity_id=entity_id, entity_type=entity_type, user_id=user_id, source="abc", plugin_id=plugin_id, subscription_id=subscription_id)
    entity_create = "/core/plugins/{plugin_id}/subscriptions?id={subscription_id}&type={entity_type}&owner={user_id}&source={source}".format(
        **query)
    data = dict(mode="realtime", source="ignore", filter="insert into abc select " + entity_id + ".p1", target="ignore", topic="abc", pubsub_name="client-pubsub")
    print(data)
    res = requests.post(keel_url + entity_create, json=data)
    print(res.json())
```

###### 消费 topic 数据
消费程序作为一个独立的app消费相关topic数据并展示[消费示例](code/subclient)
```python
// Source: examples/subclient/app.py
import flask
from flask import request, jsonify
from flask_cors import CORS
import json

app = flask.Flask(__name__)
CORS(app)

@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{'pubsubname': 'client-pubsub',
                      'topic': 'abc',
                      'route': 'data'}]
    return jsonify(subscriptions)

@app.route('/data', methods=['POST'])
def ds_subscriber():
    print(request.json, flush=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
app.run()
```