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