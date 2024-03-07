from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
<<<<<<< HEAD
=======
from flask_wtf.file import FileField, FileAllowed, FileRequired
>>>>>>> 79519a6 (updated files)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
<<<<<<< HEAD
    password = PasswordField('Password', validators=[InputRequired()])
=======
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file_upload = FileField('File_upload', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    
>>>>>>> 79519a6 (updated files)
