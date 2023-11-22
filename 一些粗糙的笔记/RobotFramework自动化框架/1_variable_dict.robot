*** Settings ***
Documentation    Suite description
Library    Collections

*** Variables ***
&{the_girl}   name=沈晚霞    foot_size=38     like_food=小炒肉

*** Test Cases ***
Test dict-1
    [Documentation]    字典赋值
    ${the_boy}  create dictionary    name=沈煜东    foot_size=41     like_food=小炒肉
    LOG    ${the_boy}       #  打印用例字典
    LOG    ${the_girl}      #  打印变量文件字典

Test dict-2
    [Documentation]    字典添加
    ${the_boy}  create dictionary    name=沈煜东    foot_size=41     like_food=小炒肉
    set to dictionary    ${the_boy}     favirate=${the_girl}    car=ES6
    LOG    ${the_boy}
    remove from dictionary    ${the_boy}    like_food
    LOG    ${the_boy}
    ${the_girl_1}   pop from dictionary    ${the_boy}   favirate
    LOG    ${the_boy}
    LOG    ${the_girl_1}
    keep in dictionary    ${the_boy}    name
    LOG    ${the_boy}

Test dict-3
    [Documentation]    字典获值
    ${the_boy}  create dictionary    name=沈煜东    foot_size=41     like_food=小炒肉
    LOG    ${the_boy}[name]             #  ${dict}[key] 方法获取value
    LOG    ${the_boy.foot_size}         #  ${dict.key}  方法获取value
*** Keywords ***