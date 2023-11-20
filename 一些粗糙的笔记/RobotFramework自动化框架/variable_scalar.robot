*** Settings ***
Documentation    Suite description

*** Variables ***
${scalar_var}   这里是参数模块

*** Test Cases ***
Test scalar-1
    [Documentation]    标量赋值
    ${boyname}  set variable    Tom
    log    ${boyname}

Test scalar-2
    [Documentation]    标量判断赋值
    ${girlname}     set variable if    2==3    Alice   Lucky
    LOG    ${girlname}

Test scalar-3
    [Documentation]    标量切片获值
    ${girlname}     set variable    沈晚霞
    LOG    first_name:${girlname}[0]
    LOG    last_name:${girlname}[-2:]
*** Keywords ***
