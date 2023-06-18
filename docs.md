# Documentation for MD Logistics Application.
This file contains the documentation for this application.

# Functions for Users

### emailValidator()
Uses the regular expressions module "re" to validate an email (i.e to make sure that the email is of the right format. eg: [name]@[provider].com )

### userNameValidator()
Checks if the user name already exists in the database. This is to ensure there are no duplicates of a specific user name.

### getResponse()
Gets response from a user and then performs an action based on the user's response.

### add_user()
Gets data from user, validates the data, hashes the data and then stores it in the database. The data is hashed to keep the contents fo the database safe in case of a data breach.

### loginUser()
Gets data from user and then logs in the user if the user exists and the data provided matchs with what already exists in the database.

### removeUser()
Removes or deletes a user from the database based on the data provided by a user.

### updateUserPassword()
Updates the password of a user

### updateUserEmail()
updates the email of a user

# Functions for Items