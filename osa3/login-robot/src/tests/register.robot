*** Settings ***
Resource  resource.robot
Test Setup  Input New

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  foobar123
    Input New Command
    Input Credentials  kalle  busbar123
    Output Should Contain  Invalid username: Already in use

Register With Too Short Username And Valid Password
    Input Credentials  ka  foobar123
    Output Should Contain  Invalid username: Should be at least three 'a-z' characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  källe  foobar123
    Output Should Contain  Invalid username: Should be at least three 'a-z' characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  foobar1
    Output Should Contain  Invalid password: Should be at least eight characters long and contain at least one character that isn't a letter

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  foobaronetwothree
    Output Should Contain  Invalid password: Should be at least eight characters long and contain at least one character that isn't a letter

*** Keywords ***
Input New
    Input New Command