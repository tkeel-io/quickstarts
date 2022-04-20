# tkeel-calc-add
**tkeel-calc-add** 是 **tKeel** 官方开发的一个用于演示 **tKeel** 平台的插件扩展机制的插件。

## API

| API    | METHOD | reqeust          | RESPONSE                       | DESC                             |
| ------ | ------ | ---------------- | ------------------------------ | -------------------------------- |
| /add   | 'GET'  | x,y  (均为int型) | {"res": ${X+Y}}                | 将请求中的 x 和 y 的值相加后返回 |
| /hello | 'GET'  | null             | {"msg": "hello tkeel cal add"} | hello tkeel cal add              |

## Permission
无内部权限限制。

## FrontEnd
无前端页面。