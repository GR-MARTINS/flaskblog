# Flask Blog

## What is the Flask Blog?

The Flask Blog is a simple Flask app created to showcase the versatility of the Flask in web applications development. Flask Blog lets you create an user account. After creating the account, you will be able to create, update and delete posts, view posts from other users, change their username and profile picture and also change their password in case forget.

## What are the technologies and tools used in the project?

Flask Extensions:
* ```dynaconf```
* ```flask-bcrypt```
* ```flask-jwt-extended```
* ```flask-login```
* ```flask-mail```
* ```flask-sqlalchemy```
* ```flask-wtf```

Other python libraries:
* ```datetime```
* ```itsdangerous```
* ```os```
* ```PIL```
* ```python-dotenv```
* ```secrets```

Database:
* PostgreSQL

Pages;
* HTML
*  CSS

## Where to access the Flask Blog?
App in production. Access the project at https://grgm-flaskblog.herokuapp.com/

Initial project Steps:

- [x] Start Projetc
- [x] Templates
- [x] Forms and validation
- [x] Database
- [x] Login Auth
- [x]  User-Account-Profile-Pic
- [x] Posts
- [x] Pagination
- [x] Password reset email
- [x] Error Pages
- [x] Deploy

## Did you like the project? Follow the instructions to run locally.

1. Create a virtual enviroment python in the root directory.
2. active your virtual enviroment.
3. Execute the command ```pip install -r requirements.txt``` for to install the necessary libraries and modules.
4. create a file called _**.secrets.toml**_ in the root directory. In this file, configure the following settings:
    ```
    [default]
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://your_postgres_username:your_password@your_host:port/your_postgres_database_name'
    MAIL_USERNAME = 'an_email@mail.com: this will be used for the link to change the password.'
    MAIL_PASSWORD = 'email_password'

    [development]

    [production]

    ```
5. Run the DB migrations with the follow commands in your virtual environment:
   * ```flask db init```
   * ```flask db migrate```
   * ```flask db upgrade```
6. Execute the command ```flask run``` for to start the Flask server.

## TODO:

- [ ] create interactions between users, so that it is possible to respond to posts, react, etc.
