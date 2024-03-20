import os
from app import app, db, login_manager
from flask import render_template, request, redirect, send_from_directory, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.models import UserProfile
from app.forms import LoginForm, UploadForm
from werkzeug.security import  check_password_hash

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
@login_required
def upload():
    # Instantiate your form class
    form=UploadForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Get file data and save to your uploads folder
            photo = form.photo.data
            filename = secure_filename(photo.filename) 
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File Saved', 'success')
            return redirect(url_for('files')) # Update this to redirect the user to a route that displays all uploaded image files
        flash("failed")
    return render_template('upload.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
             # process the data
            username = form.username.data
            password = form.password.data 
            user =db.one_or_404(db.select(UserProfile).filter_by(username=username))
            if check_password_hash(user.password, password):
                

        # Get the username and password values from the form.

        # Using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        # Then store the result of that query to a `user` variable so it can be
        # passed to the login_user() method below.

        # Gets user id, load into session
                login_user(user)

        # Remember to flash a message to the user
                flash('Login was successful', 'success')
                return redirect(url_for("upload"))  # The user should be redirected to the upload form instead
    return render_template("login.html", form=form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()

@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for("home"))


@app.route("/uploads/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

def get_uploaded_images():
    rootdir = os.getcwd()
    filepaths=[]
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
      for file in files:
        print (os.path.join(subdir, file))
        filepaths.append(os.path.join(file))
    return filepaths


@app.route('/files')
@login_required
def files():
    filenames=get_uploaded_images()
    return render_template('files.html', filenames=filenames)



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
