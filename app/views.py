import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
<<<<<<< HEAD
from app.models import UserProfile
from app.forms import LoginForm
=======
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import UserProfile
from app.forms import LoginForm
from app.forms import UploadForm
>>>>>>> 79519a6 (updated files)


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/upload', methods=['POST', 'GET'])
<<<<<<< HEAD
def upload():
    # Instantiate your form class

    # Validate file upload on submit
    if form.validate_on_submit():
        # Get file data and save to your uploads folder

        flash('File Saved', 'success')
        return redirect(url_for('home')) # Update this to redirect the user to a route that displays all uploaded image files

    return render_template('upload.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    # change this to actually validate the entire form submission
    # and not just one field
    if form.username.data:
        # Get the username and password values from the form.

=======
@login_required
def upload():
    # Instantiate your form class
    form = UploadForm()
    # Validate file upload on submit
    if request.method == 'POST':
        if form.validate_on_submit():
            # Get file data and save to your uploads folder

            f = form.file_upload.data
            filename = secure_filename(f.filename)
            file_path = os.path.join(os.path.dirname(app.instance_path), 'uploads', filename)
            print(file_path)
            f.save(file_path)
            flash('File Uploaded!')
            return redirect(url_for('upload')) # Update this to redirect the user to a routethat displays all uploaded image files
        else:
            flash('Allowed image types are - png, jpg')
            return redirect(url_for('upload'))
    return render_template('upload.html', form=form)


def get_uploaded_file(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('app', filename='uploads/' + filename), code=301)

#def get_uploaded_file(filename):
   # rootdir = os.getcwd()
   # print (rootdir)
    
    #for subdir, dirs, files in os.walk(rootdir + os.path.join(os.path.dirname(app.instance_path), 'uploads', filename)):
     #   for file in files:
      #      print (os.path.join(subdir, file))

@app.route('/uploads/<filename>')
def get_image(filename)
    send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

@app.route('/files')
def files()
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    # change this to actually validate the entire form submission
    # and not just one field
    if form.validate_on_submit():
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data
>>>>>>> 79519a6 (updated files)
        # Using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        # Then store the result of that query to a `user` variable so it can be
        # passed to the login_user() method below.
<<<<<<< HEAD

        # Gets user id, load into session
        login_user(user)

        # Remember to flash a message to the user
        return redirect(url_for("home"))  # The user should be redirected to the upload form instead
    return render_template("login.html", form=form)
=======
        user = db.session.execute(db.select(UserProfile).filter_by(username=username)).scalar()

        if user is not None and check_password_hash(user.password, password):
        # Gets user id, load into session
            login_user(user)

        # Remember to flash a message to the user
            flash('You have successfully logged in!')

            # is_safe_url should check if the url is safe
            # for use in redirects, meaning it matches the request host.
            

            return redirect(url_for('upload'))
        else:
            flash('Username or Password is incorrect.', 'danger')
    flash_errors(form)
    return render_template('login.html', form=form)
       # return redirect(url_for("upload"))  # The user should be redirected to the upload form instead
   # return render_template("login.html", form=form)
>>>>>>> 79519a6 (updated files)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()

###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
