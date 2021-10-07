[![tests](https://github.com/DamirZaripov16/test_api-project/actions/workflows/tests.yml/badge.svg)](https://github.com/DamirZaripov16/test_api-project/actions/workflows/tests.yml)
# ["Stores"](https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0) api-autotests️
***
## 🧭 Navigation

1. [About](#about)<br>
2. [Installation](#installation)<br>
3. [Instruments](#instruments)<br>
4. [Checks](#checks)<br>
5. [Allure reports](#allure-reports)
## ❓ About
In this project the api-autotests cover all the methods and responses in "Stores" Swagger.<br>
As usual I have chosen _Page Object model_ as a code design pattern to ensure further comfort editing and extension.
## ⬇️ Installation
1. Define a directory on a local machine
2. Clone the [project](https://github.com/DamirZaripov16/test_api-project) <br>
   ```git clone https://github.com/DamirZaripov16/test_api-project```
3. Open the project
4. Install all the requirements within **requirements.txt** <br>
   ```pip install -r /path/to/requirements.txt```
## ⚙️ Instruments
### _**Pytest**_
* The Easiest and yet the best test-writing tool in Python
* Multiple tests execution in parallel to reduce general execution time
* Unique way to detect tests in your project without additional imports etc.
* Fixture support.<br>
### _**Requests**_
* Commonly-used library for checking statuses and responses
### _**Logger**_
* Helps to track what exactly happening during test execution with minimum effort
* Easy to implement
### _**Github Actions**_
* "The final gate" to ensure the success of your recent build<br>
* Automated integration possibility with your linters, validators etc.<br>
### _**Allure reports (see ["Allure reports"](https://github.com/DamirZaripov16/test_ui-project#allure-reports) section for more)**_
* Detailed tests execution reports
* User-friendly dashboard to help to keep in touch with tests state<br>
* Gives a negative feedback by creating a screenshot<br>
## ✔️Checks
### ✔**Registration**
|Positive tests |Required fields negative tests|
| --- | --- |
|Successful registration of a user|Empty user data registration|

**Initial file and detailed docstring-test cases**: ```tests\register\test_register.py```
### ✔**Authentication**
|Positive tests| Negative tests|
| --- | --- |
|Successful authentication of a user|Authentication with random username and password|

**Initial file and detailed docstring-test cases**: ```tests\authentication\test_authentication.py```
### ✔**User Info**
|Positive tests|Negative tests|
| --- | --- |
|Successful user info addition |User info addition without header|
|Successful user info deletion|Non-existing user info addition|
|Getting the user info |Getting the user info without header|
|Successful user info update |Getting the non-existing user info|
| |User info update without header|
| |User info update without authentication header|
| |User info update with invalid header|
| |User info update with invalid user id|


**Initial file and detailed docstring-test cases**:<br> 
```tests\user_info\test_add_user_info.py```<br>
```tests\user_info\test_delete_user_info.py```<br>
```tests\user_info\test_get_user_info.py```<br>
```tests\user_info\test_update_user_info.py```
### ✔**Store**
|Positive tests|Negative tests|
| --- | --- |
|Successful store addition|Store addition without header|
|Getting the store|Already existing store addition|
| |Getting the store without header|
| |Getting the store with non-existing name|

**Initial file and detailed docstring-test cases**:<br> 
```tests\store\test_add_store.py```<br>
```tests\store\test_get_store.py```
### ✔**Store items**
|Positive tests|Negative tests|
| --- | --- |
|Successful store item addition|Store item addition without header|
|Getting the store item|Already existing store item addition|
|Getting all the store items |Store item addition without data|
|Successful store item update |Store item addition with invalid name|
| |Getting the store item without header|
| |Getting the store item with non-existing name|
| |Store item update without header|
| |Store item update with invalid name|

**Initial file and detailed docstring-test cases**:<br> 
```tests\store_item\test_add_store_item.py```<br>
```tests\store_item\test_get_store_item.py```<br>
```tests\store_item\test_update_store_item.py```
### ✔**User balance**
|Positive tests|Negative tests|
| --- | --- |
|Successful user balance addition|User balance addition without header|
|Getting the user balance|User balance addition with empty data|
| |User balance addition with invalid balance|
| |Getting the user balance without header|
| |Getting the user balance with non-existing user|

**Initial file and detailed docstring-test cases**:<br>
```tests\user_balance\test_add_user_balance.py```<br>
```tests\user_balance\test_get_user_balance.py```
### ✔**Payment**
|Positive tests|Negative tests|
| --- | --- |
|Successful payment addition|Payment addition without header|
| |Payment addition with empty data|
| |Payment addition with invalid item id|

**Initial file and detailed docstring-test cases**: ```tests\payment\test_add_payment.py```
##  📄 **Allure reports**
1) Install _**Allure commandline application**_ on your OS<br>
**Windows-users**:
   1) Run _**PowerShell**_ and install _**Allure commandline application**_ by the following command:
   <br>```scoop install allure```<br>
   2) Download _**Allure commandline application**_ manually if you don't have **_scoop_** installed<br>
   3) Java is required no matter which installation way you choose<br>
**Linux and MacOS users** check [this](https://docs.qameta.io/allure/#_installing_a_commandline).
2) Run ```pytest --alluredir=allure_reports``` on your IDE for tests completion data generation
3) Run ```allure serve allure_reports``` to see status dashboard after tests are completed
