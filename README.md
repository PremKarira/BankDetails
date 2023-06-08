# BankDetails
Employees storing bank details in the company database.

Bankdetails API
    api/bankdetails
        get - full list of all bankdetails
        post - add new bankdetail
    api/bankdetails/id
        get - get by id
        delete - delete by id
        *put - check if update allowed , if yes, save to update request
    api/bankdetails/updates
        get - get all update request
        post- accept update
    api/users
        get - get all users
        post - add new user (signup)
    api/users/login
        post - check email pass 

## API documentation

_http://[site]:[port]/api/endpoints_

## Endpoints: 
* *users* [POST]
   - Sign up as a new user
   - Required json body params - ‘email’, ‘password’
* *user/login* [POST]
   - Login with existing creds
   - Required json body params - ‘email’, ‘password’
* *users* [GET]
   - Get list of all users
   
* */bankdetails* [GET] 
  - Get list of all the stored bankdetails
   
* */bankdetails* [POST] 
  - Add new bankdetails of a particular user
  - Required json body params - 'email','account_holder_name','account_number','ifsc_code','bank_name','branch_name'
   
* */bankdetails/id* [GET] 
  - Get details by id
   
* */bankdetails/id* [DELETE] 
  - Delete a record by id
   
* */bankdetails/id* [PUT] 
  - for pushing record in update table and setting **update_allowed as false**
   
* */bankdetails/updates* [GET] 
  - Get list of updates to be accepted by admin
   
* */bankdetails/updates* [POST] 
  - Updates record in bankdetails table and deletes from update table
  - Required json body params - 'email','account_holder_name','account_number','ifsc_code','bank_name','branch_name'


## Signup & Login
* Signup
    - test
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/signup.png?raw=true"></p><br>

* Login
    - 
    <p align="center"><img src=""></p><br>

## Three Cases
* Case 1 : New User
    - 
    <p align="center"><img src=""></p><br>

* Case 2 : OLd user but can update details once
    - 
    <p align="center"><img src=""></p><br>

* Case 3 : No updates allowed, so show details
    - 
    <p align="center"><img src=""></p><br>
