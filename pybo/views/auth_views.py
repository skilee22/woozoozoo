
from flask import Blueprint, render_template, request, url_for, flash
from pybo.models import Question, User
from pybo.forms import QuestionForm, UserCreateForm
from datetime import datetime
from .. import db
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/signup',methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        print('------2')
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                        email = form.email.data, phone=form.phone.data
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 유저입니다.')
    return render_template('auth/signup.html',form=form)

