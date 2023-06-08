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
    - 
    <p align="center"><img src="https://github.com/PremKarira/BankDetails/blob/main/images/AdminPanel.jpg?raw=true"></p><br>

* Login
    - 
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/login.png?raw=true"></p><br>

## Three Cases
* Case 1 : New User
    - 
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/login.png?raw=true"></p><br>

* Case 2 : OLd user but can update details once
    - 
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/login.png?raw=true"></p><br>

* Case 3 : No updates allowed, so show details
    - 
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/login.png?raw=true"></p><br>

## Dashboard Walkthrough
* Books in Store
    - The dashboard displays a list of books available in the store.
    - Each book entry includes the title, description, and price.
    - To edit a book, click the "Edit" button next to the book entry.
    - To delete a book, click the "Delete" button next to the book entry.
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/dashboard.png?raw=true"></p><br>

* Add New Book
    - To add a new book to the store, fill in the "Title," "Description," and "Price" fields in the "Add New Book" section.
    - Click the "Add Book" button to add the book to the store.
    - The book will be displayed in the "Books in Store" section.
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/addbook.png?raw=true"></p><br>

* Edit Book
    - When you click the "Edit" button next to a book, the form in the "Edit Book" section will be populated with the book's details.
    - Modify the desired fields (e.g., title, description, price) in the form.
    - Click the "Update Book" button to save the changes.
    - The book's details will be updated in the "Books in Store" section.
    <p align="center"><img src="https://github.com/PremKarira/Book-Management/blob/main/images/editbook.png?raw=true"></p><br>

* Cancel Edit
    - If you wish to cancel the edit without saving any changes, click the "Cancel" button in the "Edit Book" section.
The form will be cleared, and the edit section will be hidden.