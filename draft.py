connectorConfig = {
    "type": "json",
    "returnType": "json",
    "onloadTrigger": False,
    "dataSourceType": "interface",
    "customData": {"type": "value", "code": "{}", "storeType": "string",
                   "list": [{"id": "8a881370-1e2d-11ef-abb1-89047233e570", "label": "", "value": ""}]},
    "interfaceType": "custom",
    "url": "http://hapi.hikvision.com.cn/mock/7331/syd",
    "componentId": "hapi",
    "serviceType": "hapi",
    "authorizationType": "noAuthorization",
    "authorizationValue": {"method": "aksk", "ak": "", "sk": ""},
    "requestType": "post",
    "modelCode": "",
    "modelOpType": "query",
    "componentSet": "copasTopicSet",
    "headerParamStruct": {
        "root": {"type": "object", "disabledType": True, "desc": "根节点", "disabledTitle": True, "bindValue": "",
                 "disabledBindValue": True, "bindType": "bind"}},
    "paramStruct": {
        "root": {"type": "object", "disabledType": True, "desc": "根节点", "disabledTitle": True, "bindValue": "",
                 "disabledBindValue": True}},
    "pathParamStruct": {
        "root": {"type": "object", "disabledType": True, "desc": "根节点", "disabledTitle": True, "bindValue": "",
                 "disabledBindValue": True, "properties": {}}},
    "resultStruct": {
        "root": {"type": "object", "disabledType": True, "desc": "根节点", "disabledTitle": True, "bindValue": "",
                 "disabledBindValue": True}}, "dealParamStructFun": "", "dealResultFun": "",
    "successEvent": [],
    "successMsgConfig": {"enable": False, "msgSource": "interface", "msgText": "数据请求成功"},
    "failEvent": [],
    "failMsgConfig": {"enable": True, "msgSource": "interface", "msgText": "系统异常，请联系管理员"},
    "pollingConfig": {"enable": False, "pollingTime": 1},
    "loadingConfig": {"enable": False, "target": "all"},
    "extraInfo": ""
}
