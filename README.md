1. 云控json
| 字段 | 说明 |
| :--- | :---:  |
| test_id | ""   **必填** |
|test_group | ""  **必填**|
|test_state | 1: 测试中，2：结束测试  **必填** |
| silence | true：静默，无UI表现 **必填** |
|negotiate_type | 0：无效；其他：和CGS Proxy等协议类型，一般会调用特定接口 |
| tips_info | json |
| menu_info | json |
| setting_info | json |
| extend_info |  json类型，不同AB测试，内容不同，定制化  |
| score_info |  json|
