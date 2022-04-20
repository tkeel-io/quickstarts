# 🚪 快速入门

本指南将快速演示 **tKeel** 平台插件的扩展功能。

本指南包含三个插件:
1. tkeel-cal: 计算插件，插件提供 cal 接口，并声明 calc-int-x-y 扩展点，通过不同插件来实现本扩展点，当前接口的返回值也随之改变。
2. tkeel-cal-add: 加法插件，插件提供 add 接口来实现 tkeel-cal 插件的 calc-int-x-y 扩展点，通过将 x 和 y 相加再返回具体的结果给 tkeel-cal 插件。
3. tkeel-cal-mul: 乘法插件，插件提供 mul 接口来实现 tkeel-cal 插件的 calc-int-x-y 扩展点，通过将 x 和 y相乘在返回具体的结果给 tkeel-cal 插件。

## 安装需要
🔧 在进行教程之前请先确保你做足了准备。
* 成功安装 tKeel 平台。

## Step 1. 安装 tkeel-cal 插件
通过管理平台安装 tkeel-cal 插件，安装完成后即可通过 管理平台的 token 访问对应的 cal 接口：
```bash
curl --location --request GET 'http://{{tkeel}}/apis/tkeel-calc/calc?x=1&y=2' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0S2VlbCIsImV4cCI6IjIwMjItMDQtMTFUMDg6NTA6MTIuOTIzNTk1NjY3WiIsImlhdCI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsImlzcyI6InJ1ZGRlciIsImp0aSI6IjZlM2NkYmMzLTNkZjItNDkwMS04NzIzLTdiMTg3ZWNiMWY4NyIsIm5iZiI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsInN1YiI6ImFkbWluIn0.kjqjq_zB8iEm3pZGb7f31PiPVK2xrvkQ2XypadYYQnQ'
```

response:
```json
{
    "code": "io.tkeel.INTERNAL_ERROR",
    "data": {},
    "msg": "invaild addons calc-int-x-y"
}
```

## Step 2. 安装 tkeel-cal-add 插件
通过管理平台安装 tkeel-cal-add 插件，安装完成后再次通过管理平台的 token 访问对应的 cal 接口：
```bash
curl --location --request GET 'http://{{tkeel}}/apis/tkeel-calc/calc?x=1&y=2' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0S2VlbCIsImV4cCI6IjIwMjItMDQtMTFUMDg6NTA6MTIuOTIzNTk1NjY3WiIsImlhdCI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsImlzcyI6InJ1ZGRlciIsImp0aSI6IjZlM2NkYmMzLTNkZjItNDkwMS04NzIzLTdiMTg3ZWNiMWY4NyIsIm5iZiI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsInN1YiI6ImFkbWluIn0.kjqjq_zB8iEm3pZGb7f31PiPVK2xrvkQ2XypadYYQnQ'
```

response:
```json
{
    "code": "io.tkeel.SUCCESS",
    "data": {
        "res": "3"
    },
    "msg": ""
}
```

## Step 3. 卸载 tkeel-cal-add 插件，并安装 tkeel-cal-mul 插件
通过管理平台卸载 tkeel-cal-add 插件，卸载完成后再安装 tkeel-cal-mul 插件，安装完成后再次通过管理平台的 token 访问对应的 cal 接口：
```bash
curl --location --request GET 'http://{{tkeel}}/apis/tkeel-calc/calc?x=1&y=2' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0S2VlbCIsImV4cCI6IjIwMjItMDQtMTFUMDg6NTA6MTIuOTIzNTk1NjY3WiIsImlhdCI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsImlzcyI6InJ1ZGRlciIsImp0aSI6IjZlM2NkYmMzLTNkZjItNDkwMS04NzIzLTdiMTg3ZWNiMWY4NyIsIm5iZiI6IjIwMjItMDQtMTFUMDc6NTA6MTIuOTIzNTk1NjY3WiIsInN1YiI6ImFkbWluIn0.kjqjq_zB8iEm3pZGb7f31PiPVK2xrvkQ2XypadYYQnQ'
```

response:
```json
{
    "code": "io.tkeel.SUCCESS",
    "data": {
        "res": "2"
    },
    "msg": ""
}
```