# WL Assignment Details

## APIS

 1. **Get All Users** : Get All Users from the Database
 2. **Login User** : This API does two things, if user exists, it authenticates else creates the user
 3. **GetSignedUsers** : This API returns a list of userid's with the number of times they have logged in.

## Architecture

[Architecture Diagram](https://github.com/yogeetagup/WL_Assignment/blob/main/wl_assignment.drawio)

![wl_assignment](https://user-images.githubusercontent.com/47107793/116728712-df206c80-aa03-11eb-812b-8a5c967c2df2.png)


## Database Used

For this Assignment SqlLite Database is used. Two tables are used **User**[*Built in Django User model*] and **Account**[*Capture the user login Activity*]
