from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/')

def index():
    name = None
    nameForm = NameForm()
    if nameForm.validate_on_submit():
        name = nameForm.name.data
        nameForm.name.data = ''

    return render_template('index.html', form=nameForm, name=name)

if __name__ == '__main__':
    app.run(debug=True)