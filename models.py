import mysql.connector
import hashlib
from pprint import pprint


DBCONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'admin',
    'database': 'myappDB'
}


class DbManager:
    def __init__(self, **DBCONFIG):
        self.config = DBCONFIG

    def __enter__(self):
        self.conn = mysql.connector.connect(**DBCONFIG)
        self.cursor = self.conn.cursor(buffered=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close


class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return self.username

    def log_in(self, password):
        with DbManager(**DBCONFIG) as cursor:
            USERS_SQL = '''SELECT username, password, userid FROM users;'''
            cursor.execute(USERS_SQL)
            all_users_data = cursor.fetchall()
            encrypt_password = hashlib.sha256(password.encode()).hexdigest()

            for i in range(len(all_users_data)):
                if self.username in all_users_data[i]:
                    if all_users_data[i][1] == encrypt_password:
                        return [True, 'Successful Log In', all_users_data[i][2]]
                    else:
                        return [False, 'Wrong Password']
            else:
                return [False, self.username + ' ' + 'Username not found']
        
    def signup(self, fname, lname, email,  username, password,):
        with DbManager(**DBCONFIG ) as cursor:
            encrypt_password = hashlib.sha256(password.encode()).hexdigest()

            SIGNUP_SQL = '''INSERT INTO users (first_name, last_name, email, username, password) VALUES
            (%s, %s, %s, %s, %s )'''
            # cursor.execute(SIGNUP_SQL, (fname, lname, email, username, encrypt_password))
            print(fname, lname, email, username, encrypt_password)
            print('SUCCESFULL SIGN UP')
            return True

    def edit_settings(self, **user):
        with DbManager(**DBCONFIG) as cursor:
            SETTINGS_SQL = '''UPDATE user SET () VALUES ()'''
            return cursor.execute(SETTINGS_SQL, ())


    def create_post(self, title, content, privacy='yes'):
        with DbManager(**DBCONFIG) as cursor:
            CREATE_POST_SQL = '''INSERT INTO post (author, title, content, privacy) VALUES (%s, %s, %s, %s)'''
            if cursor.execute(CREATE_POST_SQL, (self.username, title, content, privacy)):
                return True
            else:
                return False

    def edit_post(self, post_id):
        with DbManager(**DBCONFIG) as cursor:
            EDIT_POST_SQL = '''UPDATE TABLE post SET (title, content) VALUES (%s, %s) WHERE post_id = %s'''
            return cursor.execute(EDIT_POST_SQL, ())





class Admin(User):
    def _init__(self, userid):
        self.userid = userid

    def view_user(self):
        with DbManager(**DBCONFIG) as cursor:
            USER_DETAILS = '''SELECT * FROM users WHERE username = %s'''
            cursor.execute(USER_DETAILS, (self.username,))
            user_details = cursor.fetchall()
            return user_details
        
    def create_user(self, first_name: str, last_name: str, username: str, password: str, email: str):
        pass

    def delete_user(self, userid):
        pass

    def view_tables(self):
        with DbManager(**DBCONFIG) as cursor:
            TABLES_SQL = '''SHOW TABLES'''
            cursor.execute(TABLES_SQL)
            tables = cursor.fetchall()
            return tables

    def view_users(self):
        with DbManager(**DBCONFIG) as cursor:
            USERS_SQL = '''SELECT * FROM users'''
            cursor.execute(USERS_SQL)
            users = cursor.fetchall()
            return users

    def get_all_post(self, privacy_status=''):     # POSTS
        with DbManager(**DBCONFIG) as cursor:
            if privacy_status == 'all':
                POSTS_SQL = '''SELECT * FROM post'''
                cursor.execute(POSTS_SQL)
                return cursor.fetchall()
            elif privacy_status == 'no' or privacy_status == 'yes':
                POSTS_SQL = '''SELECT * FROM post WHERE privacy = %s'''
                cursor.execute(POSTS_SQL, (privacy_status,))
                return cursor.fetchall()


    def get_post_by_post_id(self, post_id):
        with DbManager(**DBCONFIG) as cursor:
            POST_ID_SQL = '''SELECT * FROM post WHERE post_id = %s'''
            cursor.execute(POST_ID_SQL, (post_id,))
            post = cursor.fetchall()
            COMMENTS_SQL = '''SELECT * FROM comments WHERE post_id = %s'''
            cursor.execute(COMMENTS_SQL, (post_id,))
            comments = cursor.fetchall()
            return [post, comments]

    def get_post_by_user_id(self, user_id):
        with DbManager(**DBCONFIG) as cursor:
            USER_ID_SQL = '''SELECT * FROM post WHERE user_id = %s'''
            cursor.execute(USER_ID_SQL, (user_id,))
            all_user_posts = cursor.fetchall()
            return all_user_posts






# # User('shammah').singup('Steve', 'Shammah',' shammah@gmail', 'shammah', '1234')
# from pprint import pprint
# pprint(Admin('Admin').get_all_post('all'))