# Documentation Of MD Logistics for Developers.
This file contains the documentation for this application.

## add_user() Function.
This function gets the 'email' and 'password' of a user and adds it to the 'users' table in the database.
The module 're' is imported to validate the email with the help of a regex 'regex'.
The module 'getpass' is imported to make sure the password entered is not echoed (ie. displayed on the screen).
This measure is taken to ensure that the passwords of users are alwyas kept safe and hidden.
The 'email' and 'password' are hashed and then stored in the database to ensure the safety of users in the case of
a data breach or a hack.

