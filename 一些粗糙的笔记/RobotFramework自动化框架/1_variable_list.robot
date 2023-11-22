*** Settings ***
Documentation    Suite description
Library    Collections

*** Variables ***
@{list_var}   monday    tuesday     wednesday   thursday

*** Test Cases ***
Test list-1
    [Documentation]    列表赋值
    ${boysname}  set variable    Tom     Moly    Judy
    LOG    ${boysname}      #  打印用例列表
    LOG    ${list_var}      #  打印变量文件变量

Test list-2
    [Documentation]    列表Collections.create方式赋值
    ${girlsname}     create list    Julia    Alice   Lucky
    LOG    ${girlsname}

Test list-3
    [Documentation]    列表的处理方式
    ${list_var_1}   set variable    monday    tuesday     wednesday   thursday
    LOG    ${list_var_1}
    append to list  ${list_var_1}     friday
    LOG    ${list_var_1}
    insert into list    ${list_var_1}     0       sunday
    LOG    ${list_var_1}

    remove from list    ${list_var_1}     0
    LOG    ${list_var_1}
    remove values from list    ${list_var_1}  friday
    LOG    ${list_var_1}

Test list-4
    [Documentation]    列表切片获值
    LOG    ${list_var}[0]
    LOG    ${list_var}[2:]
*** Keywords ***