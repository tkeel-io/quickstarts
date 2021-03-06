## ðª å¿«éå¥é¨

æ¬æç¨å°å¼å¯¼å¤§å®¶çæ tKeel å¹³å°ä¸­ **ç¨æ·ä¾§** çåºç¡æä½ã

1. ç§æ·ç®¡çå/ç¨æ· ç»å½æµç¨ ç»å½/å·æ° è·åèå
2. ç§æ·ç®¡çå å¯¹ç¨æ·è¿è¡ åå»º/ååº/å é¤
3. ç§æ·ç®¡çå å¯¹æä»¶è¿è¡ å¯ç¨/åç¨


### å®è£éè¦
ð§ å¨è¿è¡æç¨ä¹åè¯·åç¡®ä¿ä½ åè¶³äºåå¤ã
  * dapr å tKeel éè¦å®è£å¨åä¸ä¸ª namespace ä¸­ï¼æ¯å¦ keel-systemï¼éè¦å¨ kubectl çéç½®ä¸­æå®ï¼æèå¨å½ä»¤åæ°ä¸­å ä¸``` -n keel-system```ã
  * éè¦å·²å®è£å¹¶æ³¨å **hello-tkeel** æä»¶ã
  * éè¦å·²ç»åå»ºäºç§æ·ã
1. [Kubernetes](https://kubernetes.io/)
2. [Dapr with k8s](https://docs.dapr.io/getting-started/)
3. [helm repo](https://https://github.com/tkeel-io/helm-charts)
4. [hello-tkeel/å®è£åæ³¨åæä»¶/åå»ºç§æ·](../tkeel-manager/README_zh.md)

### ç¨æ·å¹³å°ï¼

#### ç»å½æµç¨

1. ç»å½
```bash
curl -XGET "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/security/v1/oauth/token?grant_type=password&username=otz03t72-test_tenant_admin&password=123456"
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

2. å·æ° Token
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
ä¸æä¸­ç¨æ·å¹³å°ç§æ·ç®¡çåç token ä»¥è¿åå¼ä¸­ accessToken æ¿æ¢ã

TENANT_ID ä¸º 5
```bash
TENANT_ADMIN_TOKEN='Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0a2VlbCIsImV4cCI6MTY0MzIyMzE5Niwic3ViIjoidXNyLTkxNTcwMGYzZmMxZDI2OWM4YTJlZGFjYzY1NGYifQ.y96odLi5T8_bQZDX4-1Xh-HKYorhD_ZR1bdd9gCDyAD00LqCAzZXQAxM3Lf5yS5YmTi-Noy3Rar0QuNF2g299A'

TENANT_ID=5
```

3. è·åèå
èåä¸ºå½åç§æ·ç®¡çåå·²ç»å¯ç¨çæä»¶ã
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

#### ç¨æ·ç®¡ç
1. åå»ºç¨æ·
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

2. ååºææç¨æ·
ç§æ·ç®¡çåååºç§æ·ç©ºé´ä¸­ææç¨æ·
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

3. å é¤æå®ç¨æ·
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

#### æä»¶ç®¡ç

1. å¯ç¨æä»¶
å¯ç¨å·²ç»å®è£çæä»¶ã

PLUGIN_ID å®è£çæä»¶ IDã

```bash
PLUGIN_ID=hello-tkeel

curl -XPOST "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/tenants" \
     -H "Authorization: ${TENANT_ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d '"YW55IGRhdGE="'
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

æ­¤æ¶åæ¬¡è°ç¨æ¥çèåæ¥å£åºå½è¾åºå·²å¯ç¨æä»¶çèåé¡¹ã

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

2. åç¨æä»¶
```bash
curl -XDELETE "http://${KEEL_SERVICE}:${KEEL_PORT}/apis/rudder/v1/plugins/${PLUGIN_ID}/tenants" \
     -H "Authorization: ${TENANT_ADMIN_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d '"YW55IGRhdGE="'
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

æ­¤æ¶åæ¬¡è°ç¨æ¥çèåæ¥å£åºå½å é¤åç¨çæä»¶çèåé¡¹ã

```json
{
    "code": 200,
    "msg": "ok",
    "data": {
        "@type": "type.googleapis.com/api.entry.v1.GetEntriesResponse"
    }
}
```

#### æä»¶è®¿é®

æä»¶å¿é¡»å¯ç¨æè½è®¿é®ã

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

æªå¯ç¨ï¼
```json
{
    "code": 403,
    "data": null,
    "msg": "not active"
}
```

å·²å¯ç¨ï¼
```json
{
    "res": {
        "msg": "hello tkeel",
        "ret": 0
    }
}
```
