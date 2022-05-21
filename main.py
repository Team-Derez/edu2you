from flask import Flask, render_template, request, url_for, flash, redirect
import random
import user


def add_user(first, last, username, password, type):
    if type == 'Admin':
        return user.Admin(first, last, username, password, "77777", type)
    elif type == 'Volunteer':
        return user.Provider(first, last, username, password, "78758", type, "license_num", "verifcode", "specialties",
                             True)
    elif type == 'Student':
        return user.Student(first, last, username, password, '78757', type, "school_code", "disabilities",
                            "specific_needs")


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '263f8f7c32590d5bd91db8cb4864cdde9f83ec03171daf89'

admin_user = add_user("alpha", "echo", "admin", "ZGVyZXo=", 'Admin')
test_student = add_user("Test", "Student", "student", "password", 'Student')
test_volunteer = add_user("Test", "Volunteer", "volunteer", "password", "Volunteer")
users = [admin_user, test_student, test_volunteer]


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        u_name = request.form['uname']
        password = request.form['password']

        if not u_name:
            flash('Username field is empty')

        else:
            flash('Password field is empty')

        for user_obj in users:
            if user_obj.get_user() == u_name and user_obj.get_pass() == password:
                if user_obj.get_type() == 'Admin':
                    return redirect('/admin')
                elif user_obj.get_type() == 'Student':
                    return redirect('/student')
                elif user_obj.get_type() == 'Volunteer':
                    return redirect('/volunteer')
            else:
                flash('User not found, Do you want to sign up?')

    return render_template('login.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':


        f_name = request.form['fname']
        l_name = request.form['lname']
        u_name = request.form['uname']
        p_word = request.form['pass']
        type = request.form['user_type']
        if not f_name:
            flash('First name is required!')
        elif not l_name:
            flash('Last name is required!')
        elif not u_name:
            flash('Username is required!')
        elif not p_word:
            flash('Password is required!')
        else:
          new_user = add_user(f_name, l_name, u_name, p_word, 'Student')
          users.append(new_user)
          print(users)
          return redirect('/')
          
    return render_template('signup.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')


@app.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')


@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    return render_template('volunteer.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
    )
