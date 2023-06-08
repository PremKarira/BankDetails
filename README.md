# BankDetails
Employees storing bank details in the company database.

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
    - signup as a first time user 
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/signup.png?raw=true"></p><br>

* Login
    - entering details after signup
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/login.png?raw=true"></p><br>

## Three Cases
* Case 1 : New User
    - First time login asks for bankdetails
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/newUser.png?raw=true"></p><br>

* Case 2 : OLd user but can update details once
    - If bankdetails are already present, it asks for updated details
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/UpdateDetails.png?raw=true"></p><br>

* Case 3 : No updates allowed, so show details
    - if once update is already done, it just shows details
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/NoUpdatesAllowed.png?raw=true"></p><br>

## Admin Panel
* Login details
    - email : admin
    - password : admin
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/AdminPanel.png?raw=true"></p><br>
