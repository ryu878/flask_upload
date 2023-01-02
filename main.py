import os
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from flask import Flask, render_template, send_from_directory



app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['UPLOAD_FOLDER'] = 'static/files'
folder = 'static/files'

class UploadfileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
    submit = SubmitField('Upload')


@app.route('/', methods=['GET','POST'])


def home():
    form = UploadfileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return 'File has been uploaded - <a href=/>back</a>'
    return render_template('index.html', form=form)


def list_dir(dir):
    file_names = os.listdir(dir)

    for file_name in file_names:
        print(file_name)


list_dir(folder)



if __name__ == '__main__':
    app.run(debug=True)
