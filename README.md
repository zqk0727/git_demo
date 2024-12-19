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

2. tips_info json
| 字段 | 说明 |
| :--- | :---:  |
| show_rounds | 2 |
|start_test_tips | "您被选中参与限时内测，可针对本游戏开启“码率提升”功能" |
|start_test_tips | "”细节增强“功能的限时测试已结束，感谢您的参与" |

3. menu_info json
| 字段 | 说明 |
| :--- | :---:  |
| show_rounds | 1|
|red_dot_desc | "限时内测" |
|reddot_always_show |false |
|menu_desc |"细节增强" |
|menu_show_switch |true |
|menu_show_guide |true |
|guide_desc |"细节增强功能介绍，更清晰" |

4. setting_info json
| 字段 | 说明 |
| :--- | :---:  |
|start_value | ""|
|stop_value | "" |

5. extend_info json
| 字段 | 说明 |
| :--- | :---:  |
|type | 1:恒定画质， 2: FPS测试| 
|quality | ["标清", "高清", "超清", "至臻"]|
|SQoE | [0, 0, 9.5, 9.8]|

6. score_info json
| 字段 | 说明 |
| :--- | :---:  |
|enable |  true 总控制开关 | 
|questions |  array |    

|  questions 数组 | 说明 |
| :--- | :---:  |
|id |  提问ID,必选添 |    
|title |  "" |       
|desc |  "" |   
|score_grade |  5 |   
|score_values |  [1, 2,3,4,5] |   
|style |  1 |   
|condition |  json |
|questionnaire |  string |
|show_commit_icon |  boolean |
|commit_desc |  string |

|  condition json | 说明 |
| :--- | :---:  |
|key |  express |       

7. CSAT 用户满意度评分弹窗表达式
支持的运算符
| 语法说明 |  
| :--- | :---: | ---: |
|运算符 |== | != | >| >= | <| <= | 
| 数据类型 |int | bool | float |string  | 

| key | express | 说明 |
| :--- | :---: | ---: |
| hangup | hangup==false | 没有挂机 |
| bitrate_changed | bitrate_changed==false | 没有改过画质 |
| game_rounds | game_rounds>=1 | 第一轮进游戏弹窗 |
| popup_counts | popup_counts<5 |  最多弹窗几次 |
| scored | scored==false |  没有评过分(区分问题ID) |
| vip | vip==true |  VIP身份评分 |
| svip | svip==true |  SVIP身份评分 |
| invoke_setSQoE | invoke_setSQoE==true |  调用过恒定画质接口 |
| invoke_setSQoE_sud | invoke_setSQoE_sud==true |  调用过超清9.5 恒定画质接口 |
| invoke_setSQoE_pd | invoke_setSQoE_pd==true |  调用过至臻9.8恒定画质接口 |
| version | version>="0.11.1000.13201"|  版本号控制 |
| open_questionnaire | open_questionnaire==false|  没点开过问卷调查链接 |
| fps_changed | fps_changed== false|  没改过帧率 |
| need_scored | need_scored== true|  问卷调查需要前面有评分才显示 |
