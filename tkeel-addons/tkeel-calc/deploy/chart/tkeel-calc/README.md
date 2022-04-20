# tkeel-calc
**tkeel-calc** 是 **tKeel** 官方开发的一个用于演示 **tKeel** 平台的插件扩展机制的插件。

## API

| API    | METHOD | reqeust          | RESPONSE                   | DESC                                                                   |
| ------ | ------ | ---------------- | -------------------------- | ---------------------------------------------------------------------- |
| /calc  | 'GET'  | x,y  (均为int型) | {"res": ${RES}}            | 将请求中的 x 和 y 的值计算后返回，根据插件当前扩展点的实现不同结果不同 |
| /hello | 'GET'  | null             | {"msg": "hello tkeel cal"} | hello tkeel cal                                                        |

## Permission
无内部权限限制。

## FrontEnd
无前端页面。