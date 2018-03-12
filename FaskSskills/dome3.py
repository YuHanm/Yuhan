from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])

def index():
    nameForm = NameForm()
    if nameForm.validate_on_submit():
        newname = session.get('name')
        if newname is not None and newname != nameForm.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = nameForm.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=nameForm, name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True)