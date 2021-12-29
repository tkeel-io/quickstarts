## 🚪 快速入门

本教程将引导大家熟悉 tKeel 平台中 **用户侧** 的基础操作。

1. 租户管理员/用户 登录流程 登录/刷新 获取菜单
2. 租户管理员 对用户进行 创建/列出/删除
3. 租户管理员 对插件进行 启用/停用


### 安装需要
🔧 在进行教程之前请先确保你做足了准备。
  * dapr 和 tKeel 需要安装在同一个 namespace 中，比如 keel-system，需要在 kubectl 的配置中指定，或者在命令参数中加上``` -n keel-system```。
  * 需要已安装并注册 **hello-tkeel** 插件。
  * 需要已经创建了租户。
1. [Kubernetes](https://kubernetes.io/)
2. [Dapr with k8s](https://docs.dapr.io/getting-started/)
3. [helm repo](https://https://github.com/tkeel-io/helm-charts)
4. [hello-tkeel/安装及注册插件/创建租户](../tkeel-manager/README_zh.md)

### 用户平台：

#### 登录流程

1. 登录
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/oauth/token?grant_type=password&username=5-test_tenant_admin&password=123456"
```
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "access_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIwMDAwMDAiLCJleHAiOjE2NDA3NjQ1MTksInN1YiI6InVzci01LTZhYWRhZjM4YjdmMWUwNjg2ZjhiYWI1MWJmMjg3YjQ2In0.m_CnzrIF6vPnSnB-qoWThRixQS4XI1PH-tgzIoBjMgK4jZW8iVvDFmHbBAXeH3SAdlm5G3csIJDzn9eN5g7j-A",
        "expires_in": 1800,
        "refresh_token": "NTA2M2RHOGETMWFKZC01ODVKLWI3NTETYTUZNMM5NJFIOTGX",
        "token_type": "Bearer"
    }
}
```

2. 刷新 Token
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/oauth/token?grant_type=refresh_token&refresh_token=NTA2M2RHOGETMWFKZC01ODVKLWI3NTETYTUZNMM5NJFIOTGX"
```
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "access_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIwMDAwMDAiLCJleHAiOjE2NDA3NjU0MDcsInN1YiI6InVzci01LTZhYWRhZjM4YjdmMWUwNjg2ZjhiYWI1MWJmMjg3YjQ2In0.YCA_8jHf8zTL_HMeMdlIS0qzHurPnw2Rs-uYI6tdFdlvD7DIaIn62J5z5EOdrYVKRQyu681RXK9EpK_0CQeERQ",
        "expires_in": 1800,
        "refresh_token": "YJDJNDVJZTITMGIYZC01YMFKLTLHYZMTYJZKNJDKMMVLODE3",
        "token_type": "Bearer"
    }
}
```
下文中用户平台租户管理员的 token 以返回值中 accessToken 替换。

TENANT_ID 为 5
```bash
TENANT_ADMIN_TOKEN='Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIwMDAwMDAiLCJleHAiOjE2NDA3NjU0MDcsInN1YiI6InVzci01LTZhYWRhZjM4YjdmMWUwNjg2ZjhiYWI1MWJmMjg3YjQ2In0.YCA_8jHf8zTL_HMeMdlIS0qzHurPnw2Rs-uYI6tdFdlvD7DIaIn62J5z5EOdrYVKRQyu681RXK9EpK_0CQeERQ'

TENANT_ID=5
```

3. 获取菜单
菜单为当前租户管理员已经启用的插件。
```bash
curl  -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/entries" \
      -H "Authorization: ${TENANT_ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.entry.v1.GetEntriesResponse"
    }
}
```

#### 用户管理
1. 创建用户
```bash
curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants/users" \
     -H "Authorization:${TENANT_ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d "{\"username\":\"test_user\",\"password\":\"123456\",\"tenant_id\":${TENANT_ID}}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "user_id": "usr-5-df80d8162affad50a7e7fa6fd58538c3",
        "external_id": "",
        "tenant_id": 5,
        "username": "test_user",
        "nick_name": "",
        "avatar": "",
        "email": ""
    }
}
```

2. 列出所有用户
租户管理员列出租户空间中所有用户
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants/users?tenant_id=${TENANT_ID}" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${TENANT_ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": [
        {
            "user_id": "usr-5-6aadaf38b7f1e0686f8bab51bf287b46",
            "external_id": "",
            "tenant_id": 5,
            "username": "test_tenant_admin",
            "nick_name": "",
            "avatar": "",
            "email": ""
        },
        {
            "user_id": "usr-5-df80d8162affad50a7e7fa6fd58538c3",
            "external_id": "",
            "tenant_id": 5,
            "username": "test_user",
            "nick_name": "",
            "avatar": "",
            "email": ""
        }
    ]
}
```

3. 删除指定用户
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants/users/usr-5-df80d8162affad50a7e7fa6fd58538c3" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${TENANT_ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": null
}
```

#### 插件管理

1. 启用插件
启用已经安装的插件。

PLUGIN_ID 安装的插件 ID。

```bash
PLUGIN_ID=hello-tkeel

curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/tenants" \
     -H "Authorization: ${TENANT_ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d '{"extra":"any data"}'
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/google.protobuf.Empty",
        "value": {}
    }
}
```

此时再次调用查看菜单接口应当输出已启用插件的菜单项。

```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.entry.v1.GetEntriesResponse",
        "entries": [
            {
                "id": "echo-test-users",
                "name": "echo-users",
                "path": "/users",
                "entry": "https://tkeel-console-plugin-users.pek3b.qingstor.com/index.html"
            },
            {
                "id": "echo-test",
                "name": "echo-test",
                "children": [
                    {
                        "id": "echo-test-plugins",
                        "name": "echo-test-plugins",
                        "path": "/plugins",
                        "entry": "https://tkeel-console-plugin-plugins.pek3b.qingstor.com/index.html"
                    }
                ]
            }
        ]
    }
}
```

2. 停用插件
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/tenants" \
     -H "Authorization: ${TENANT_ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d '{"extra":"any data"}'
```
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/google.protobuf.Empty",
        "value": {}
    }
}
```

此时再次调用查看菜单接口应当删除停用的插件的菜单项。

```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.entry.v1.GetEntriesResponse"
    }
}
```

#### 插件访问

插件必须启用才能访问。

```bash
HTTP_VERB=GET
METHOD=hello
USER_TOKEN=${TENANT_ADMIN_TOKEN}

curl -X${HTTP_VERB} "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/${PLUGIN_ID}/${METHOD}" \
     -H 'Content-Type: application/json' \
     -H "Authorization: ${USER_TOKEN}"
     -H ...
```

output

未启用：
```json
{
    "code": 403,
    "data": null,
    "msg": "not active"
}
```

已启用：
```json
{
    "res": {
        "msg": "hello tkeel",
        "ret": 0
    }
}
```
