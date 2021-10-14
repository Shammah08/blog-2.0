from flask import Flask, render_template, url_for, redirect, request, session, abort
from models import User, Admin
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'myverysecretkey'


@app.route('/')
@app.route('/home')
def home():
    username = session
    # print('Username', username)
    all_posts = Admin(username).get_all_post('no')
    recent_posts = [post for count, post in enumerate(all_posts[::-1]) if count < 6]
    return render_template('home.html', title='Home', username=username, recent_posts=recent_posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        session.pop('username', None)
        session.pop('userid', None)
        return render_template('login.html', title='Login')
    else:
        username = request.form['username']
        password = request.form['password']
        user = User(username)
        if user.log_in(password)[0]:
            session['username'] = username
            session['userid'] = user.log_in(password)[2]
            # print(f'Username {session["username"]} and User ID: {session["userid"]}')
            return redirect(url_for('profile'))
        else:
            response = user.log_in(password)[1]
            return render_template('login.html', response=response, username=username, title='Login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='GET':
        return render_template('signup.html', title='Sign Up')
    else:
        fname = request.form['first-name']
        lname = request.form['last-name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        if password == confirm_password:
            new_user = User(username)
            print(fname, lname, email, username, password)
            new_user.signup(fname, lname, email, username, password)
        else:
            return ''



@app.route('/profile')
def profile():
    try:
        username = session['username']
        userid = session['userid']
        user = Admin(username).view_user()
        users = Admin(user).view_users()
        all_posts = Admin(username).get_all_post('no')
        print(all_posts)
        recent_posts = [post for count, post in enumerate(all_posts[::-1]) if count < 10]
        return render_template('profile.html', title='Profile', username=username, user=user, userid=userid, users=users, recent_posts=recent_posts)
    except KeyError:
        return redirect(url_for('login'))

@app.route('/profile/guest/<string:username>')
def guest_profile(username):
    try:
        active_user = session['username']
        active_userid = session['userid']
        guest_username = username
        guest_user = User(guest_username)
        user = Admin(username).view_user()
        users = Admin(guest_user).view_users()
        all_posts = Admin(guest_username).get_all_post('no')
        recent_posts = [post for count, post in enumerate(all_posts[::-1]) if count < 10]
        return render_template('profile.html', title='Profile', username=active_user, userid=active_userid,
                               guest_username=guest_username, user=user, users=users, recent_posts=recent_posts)
    except KeyError:
        return redirect(url_for('login'))


@app.route('/blog')
def blog():
    try:
        username = session['username']
        userid = session['userid']
        user = Admin(username).view_user()
        all_user_post = Admin(username).get_post_by_user_id(userid)[::-1]
        return render_template('blog.html', title='Blog', all_user_post=all_user_post, user=user)
    except KeyError:
        return redirect(url_for('login'))


@app.route('/post/<int:id>')
def get_post(id):
    try:
        username = session['username']
        post_details = Admin(username).get_post_by_post_id(id)
        post = post_details[0][0]
        comments = [len(post_details[1]), post_details[1]]
        return render_template('post.html', post=post, title=post[2], comments=comments)
    except KeyError:
        return redirect(url_for('login'))


@app.route('/post/<string:username>', methods=['POST'])
def create_post(username):
    # username = session['username']
    user = User(username)
    title = request.form['title']
    content = request.form['content']
    privacy = request.form['privacy']
    print(privacy)
    if privacy:
        # user.create_post(title, content, privacy)
        return redirect(url_for('blog'))




@app.route('/admin/<string:username>')
def admin(username):
    if username == 'Admin':
        admin = Admin(username)
        posts = admin.get_all_post('all')
        users = admin.view_users()
        tables = admin.view_tables()
        return render_template('admin.html', title='Admin Panel', users=users, posts=posts, tables=tables)
    else:
        return abort(401)


@app.route('/settings/<string:section>', methods=['GET', 'POST'])
def settings(section):
    try:
        if request.method == 'GET':
            username = session['username']
            user_details = Admin(username).view_user()
            return render_template('settings.html', title='Settings', user_details=user_details)
        else:
            if section =='personal':
                user = {
                    'first_name': request.form['first-name'],
                    'last_name': request.form['last-name'],
                    'email': request.form['email'],
                    'username': request.form['username'],
                    'about': request.form['about'],
                }
                print(user)
            elif section == 'social':
                social = {
                    'instagram': request.form['instagram'],
                    'twitter': request.form['twitter'],
                    'facebook': request.form['facebook'],
                }
            elif section == 'delete':
                userid = session['userid']
                status = True
                if Admin('Admin').delete_user(userid, status):
                    return redirect('signup')
            else:
                return render_template('settings.html')
    except KeyError:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=7070)
