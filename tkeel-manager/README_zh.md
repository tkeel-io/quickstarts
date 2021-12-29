## 🚪 快速入门

本教程将引导大家熟悉 tKeel 平台中 **管理侧** 的基础操作。

1. 对仓库进行 添加/查询/删除。
2. 对插件进行 安装/注册/注销/卸载。
3. 对租户进行 创建/删除。

### 安装需要
🔧 在进行教程之前请先确保你做足了准备。
  * dapr和tkeel需要安装在同一个 namespace 中，比如 keel-system，需要在 kubectl 的配置中指定，或者在命令参数中加上``` -n keel-system```。
  * 需要提供一个仓库地址并且将此插件打包上传至仓库。
1. [Kubernetes](https://kubernetes.io/)
2. [Dapr with k8s](https://docs.dapr.io/getting-started/)
3. [helm repo](https://https://github.com/tkeel-io/helm-charts)

### 管理平台：
* 系统管理员 登录
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/oauth2/admin?password=${ADMIN_PASSWORD}"
```
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.oauth2.v1.IssueTokenResponse",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0S2VlbCIsImV4cCI6IjIwMjEtMTItMjhUMDg6MTg6MDAuNDAxMTY3ODMxWiIsImlhdCI6IjIwMjEtMTItMjhUMDc6MTg6MDAuNDAxMTY3ODMxWiIsImlzcyI6InJ1ZGRlciIsImp0aSI6Ijc2Mjk0YzBlLTc2MjEtNDcwYy04M2I5LWM1M2YxOWE4NWQ4OCIsIm5iZiI6IjIwMjEtMTItMjhUMDc6MTg6MDAuNDAxMTY3ODMxWiIsInN1YiI6ImFkbWluIn0.AbJtk8dZxpj1jsxuCNbrLV1j6uPy-NHO7S6fkOQusQc",
        "token_type": "Bearer",
        "expires_in": 3600
    }
}
```
下文中所有管理平台的 token 均以返回值中 accessToken 替换。
```bash
ADMIN_TOKEN='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0S2VlbCIsImV4cCI6IjIwMjEtMTItMjhUMDg6MTg6MDAuNDAxMTY3ODMxWiIsImlhdCI6IjIwMjEtMTItMjhUMDc6MTg6MDAuNDAxMTY3ODMxWiIsImlzcyI6InJ1ZGRlciIsImp0aSI6Ijc2Mjk0YzBlLTc2MjEtNDcwYy04M2I5LWM1M2YxOWE4NWQ4OCIsIm5iZiI6IjIwMjEtMTItMjhUMDc6MTg6MDAuNDAxMTY3ODMxWiIsInN1YiI6ImFkbWluIn0.AbJtk8dZxpj1jsxuCNbrLV1j6uPy-NHO7S6fkOQusQc'
```

#### 仓库管理
1. 获取仓库信息
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/repos" \
     -H "Authorization:${ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.repo.v1.ListRepoResponse"
    }
}
```

2. 添加仓库
可将主仓库的 helm-chart fork 后，更改 index.yaml 后设置 page 即可上传测试用的插件包。
此处 url 为 `https://tkeel-io.github.io/helm-charts` 即 `https://github.com/tkeelio/helm-charts/tree/repo/index` 内容。
```bash
REPO_NAME=tkeel-default

curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/repos/${REPO_NAME}" \
     -H "Authorization:${ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d '{"url":"https://tkeel-io.github.io/helm-charts"}'
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

3. 获取仓库所有安装包
列出指定仓库名称下所有的安装包（chart 包）。
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/repos/${REPO_NAME}/installers" \
     -H "Authorization:${ADMIN_TOKEN}" \
     -H 'Content-Type: application/json'
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.repo.v1.ListRepoInstallerResponse",
        "brief_installers": [
            {
                "name": "plugins",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-plugin-components",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-plugin-components",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "core",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "core-broker",
                "version": "0.3.0",
                "repo": "tkeel-default",
                "installed": true
            },
            {
                "name": "hello-tkeel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "hello-tkeel",
                "version": "0.2.0",
                "repo": "tkeel-default"
            },
            {
                "name": "iothub",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "rudder",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-middleware",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-middleware",
                "version": "0.2.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-middleware",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "keel",
                "version": "0.1.0",
                "repo": "tkeel-default",
                "installed": true
            },
            {
                "name": "auth",
                "version": "0.1.0",
                "repo": "tkeel-default"
            },
            {
                "name": "hello-tkeel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "keel",
                "version": "0.2.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-plugin-components",
                "version": "0.2.0",
                "repo": "tkeel-default"
            },
            {
                "name": "iothub",
                "version": "0.2.0",
                "repo": "tkeel-default",
                "installed": true
            },
            {
                "name": "rudder",
                "version": "0.2.0",
                "repo": "tkeel-default"
            },
            {
                "name": "keel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            {
                "name": "tkeel-device",
                "version": "0.2.0",
                "repo": "tkeel-default",
                "installed": true
            },
            {
                "name": "core",
                "version": "0.2.0",
                "repo": "tkeel-default"
            }
        ]
    }
}
```

4. 获取仓库指定的安装包
获取指定仓库中的指定安装包和版本。

`INSTALLER_NAME` 指定的安装包名字。
`INSTALLER_VERSION` 指定的安装包版本。

```bash
INSTALLER_NAME=hello-tkeel
INSTALLER_VERSION=0.3.0

curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/repos/${REPO_NAME}/installers/${INSTALLER_NAME}/${INSTALLER_VERSION}" \
     -H "Authorization:${ADMIN_TOKEN}" \
     -H 'Content-Type: application/json'
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.repo.v1.GetRepoInstallerResponse",
        "installer": {
            "name": "hello-tkeel",
            "version": "0.3.0",
            "repo": "tkeel-default",
            "configuration": "cmVwbGljYUNvdW50OiAxDQpwbHVnaW5TZWNyZXQ6IGNoYW5nZW1lDQpwbHVnaW5Qb3J0OiA4MDgwDQoNCmRhcHJDb25maWc6IGhlbGxvLXRrZWVsDQoNCmltYWdlUHVsbFNlY3JldHM6ICIiDQoNCmltYWdlOg0KICByZXBvc2l0b3J5OiB0a2VlbGlvL2hlbGxvLXRrZWVsDQogIHRhZzogMC4zLjANCiAgcHVsbFBvbGljeTogQWx3YXlzDQo="
        }
    }
}
```
其中 configuration 中包含的是 charts 中 values.yaml 文件 base64 后的字符串。

5. 删除仓库
删除仓库操作。
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/repos/${REPO_NAME}" \
     -H "Authorization:${ADMIN_TOKEN}" \
     -H 'Content-Type: application/json'
``` 
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.repo.v1.DeleteRepoResponse",
        "repo": {
            "name": "tkeel-default",
            "url": "https://tkeel-io.github.io/helm-charts"
        }
    }
}
```

#### 插件管理
1. 安装插件
```bash
PLUGIN_ID=hello-tkeel

curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}" \
     -d '{"installer":{"name":"hello-tkeel","version":"0.3.0","repo":"tkeel-default","configuration":"cmVwbGljYUNvdW50OiAxDQpwbHVnaW5TZWNyZXQ6IGNoYW5nZW1lDQpwbHVnaW5Qb3J0OiA4MDgwDQoNCmRhcHJDb25maWc6IGhlbGxvLXRrZWVsDQoNCmltYWdlUHVsbFNlY3JldHM6ICIiDQoNCmltYWdlOg0KICByZXBvc2l0b3J5OiB0a2VlbGlvL2hlbGxvLXRrZWVsDQogIHRhZzogMC4zLjANCiAgcHVsbFBvbGljeTogQWx3YXlzDQo=","type":1}}'
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.plugin.v1.InstallPluginResponse",
        "plugin": {
            "id": "hello-tkeel",
            "status": "UNREGISTER",
            "brief_installer_info": {
                "name": "hello-tkeel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            }
        }
    }
}
```

2. 注册插件

> * **必须** 经平台安装的插件才能被注册进来。
> * **必须** 经平台注册后的插件才能被用户启用。

```bash
curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/register" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}" \
     -d '{"secret":"changeme"}'
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
3. 获取插件信息
获取指定名称的插件信息。
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.plugin.v1.GetPluginResponse",
        "plugin": {
            "id": "hello-tkeel",
            "tkeel_version": "v0.3.0",
            "secret": "changeme",
            "register_timestamp": "1640678469",
            "active_tenantes": [
                "_tKeel_system"
            ],
            "status": "RUNNING",
            "brief_installer_info": {
                "name": "hello-tkeel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            "console_entries": [
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
}
```

4. 列出所有插件
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```

output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.plugin.v1.ListPluginResponse",
        "plugin_list": [
            {
                "id": "core-broker",
                "plugin_version": "v0.3.0",
                "tkeel_version": "v0.3.0",
                "secret": "changeme",
                "register_timestamp": "1640679000",
                "active_tenantes": [
                    "_tKeel_system"
                ],
                "status": "REGISTER",
                "brief_installer_info": {
                    "name": "core-broker",
                    "version": "0.3.0",
                    "repo": "tkeel"
                }
            },
            {
                "id": "hello-tkeel",
                "tkeel_version": "v0.3.0",
                "secret": "changeme",
                "register_timestamp": "1640678948",
                "active_tenantes": [
                    "_tKeel_system"
                ],
                "status": "RUNNING",
                "brief_installer_info": {
                    "name": "hello-tkeel",
                    "version": "0.3.0",
                    "repo": "tkeel-default"
                },
                "console_entries": [
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
        ]
    }
}
```

5. 注销插件
仅注销，并未从 K8S 中删除。当前未对此做过多处理，后续可在此处处理同名插件问题。
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/register"  \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```
output
```json
{"code":200, "msg":"ok", "data":{"@type":"type.googleapis.com/api.plugin.v1.UnregisterPluginResponse", "plugin":{"id":"hello-tkeel", "tkeel_version":"v0.3.0", "secret":"changeme", "register_timestamp":"1640678948", "active_tenantes":["_tKeel_system"], "status":"RUNNING", "brief_installer_info":{"name":"hello-tkeel", "version":"0.3.0", "repo":"tkeel-default"}, "console_entries":[{"id":"echo-test-users", "name":"echo-users", "path":"/users", "entry":"https://tkeel-console-plugin-users.pek3b.qingstor.com/index.html"}, {"id":"echo-test", "name":"echo-test", "children":[{"id":"echo-test-plugins", "name":"echo-test-plugins", "path":"/plugins", "entry":"https://tkeel-console-plugin-plugins.pek3b.qingstor.com/index.html"}]}]}}}
```

6. 卸载插件
从 K8S 中删除。

> * **必须** 是未注册的插件才能被删除。

```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}"  \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```
output
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.plugin.v1.UninstallPluginResponse",
        "plugin": {
            "id": "hello-tkeel",
            "tkeel_version": "v0.3.0",
            "secret": "changeme",
            "register_timestamp": "1640678948",
            "status": "UNREGISTER",
            "brief_installer_info": {
                "name": "hello-tkeel",
                "version": "0.3.0",
                "repo": "tkeel-default"
            },
            "console_entries": [
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
}
```
#### 租户管理
1. 创建租户
```bash
curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}" \
     -d '{  "title":"test_tenant","remark":"any word","admin":{"username":"test_tenant_admin","password":"123456"}}' 
```

output:
```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "tenant_id": 4,
        "title": "test_tenant",
        "remark": "any word",
        "admin": {
            "tenant_id": 0,
            "username": "test_tenant_admin",
            "password": "",
            "nick_name": "",
            "avatar": "",
            "email": ""
        }
    }
}
```

2. 删除租户
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants/${TENANT_ID}" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```

output:
```json
{
    "code": 200,
    "msg": "ok",
    "data": null
}
```

3. 获取所有租户
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```

output:
```json
{
    "code": 200,
    "msg": "ok",
    "data": [
        {
            "id": 1,
            "title": "TenantDemo",
            "remark": "this is demo tenant"
        },
        {
            "id": 2,
            "title": "TenantDemo1",
            "remark": "this is demo tenant"
        },
        {
            "id": 3,
            "title": "TenantDemo2",
            "remark": "this is demo tenant"
        },
        {
            "id": 5,
            "title": "test_tenant",
            "remark": "any word"
        }
    ]
}
```

4. 获取指定租户下所有用户
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/tenants/users?tenant_id=${TENANT_ID}&user=${USER_ID}" \
     -H 'Content-Type: application/json' \
     -H "Authorization:${ADMIN_TOKEN}"
```
