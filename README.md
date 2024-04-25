DUMMY LANDING PAGE

This is a working demo of a basic landing page with basic user functionality. 
Registration page - ![](Screenshot(492).png)


Login page - ![](Screenshot(493).png)


End page - ![](Screenshot(494).png)



I have primarily used Django for the backend and HTML, CSS, Bootstrap, and vanilla JavaScript for the frontend. All the data entered by users will be stored in the Django backend.

This project aims to build a basic landing page with user functionality. It features a header with sections for 'Home', 'About Us', 'Register', and 'Login', as well as a footer with 'Home' and 'About Us' sections. The 'Home', 'About Us', and 'Register' sections are mapped/linked to the homepage/registration page, which contains an HTML form for user registration. The 'Login' section is linked to the login page for users who have previously registered already. 

The registration form, titled 'User Data', includes fields for username, name, email address, password, gender, and skills. It also features a submit button to save the data and a reset button to clear the form. The constraints for these inputs are as follows:
1. The username must be unique and between 4 to 32 characters long.
2. The email address must be unique and not previously registered.
3. The password must be at least 8 characters long, contain alphanumeric characters, and include at least one special character.
4. All fields are mandatory and must be filled in.

If a user enters invalid inputs, a popup displaying the error message will appear.

Upon submitting the form for the first time, a confirmation email with a unique link will be sent to the provided email address. Users must click on this link to confirm their registration. 

After confirming their registration, users can log in using valid credentials. If invalid credentials are entered, a popup with an error message will be displayed, and the user will be restricted from logging in.

Upon successful login, users will be directed to an end page displaying a popup message "You're logged in successfully". This end page will also feature a sign-out button for logging out. Upon logout, users will be redirected to the homepage.


