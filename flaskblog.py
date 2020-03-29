from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='aab17fddf3a164d1073b5042acfbace4'

posts = [
    {
        'author': 'UncleBen',
        'title': 'Blog post 1',
        'content': 'First blog content.',
        'date_posted': 'March 28, 2020'
    },
    {
        'author': 'Erick',
        'title': 'Blog post 2',
        'content': 'Second blog content.',
        'date_posted': 'March 26, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)