

from flask import Blueprint, render_template, request, url_for
from pybo.models import Question
from pybo.forms import QuestionForm
from datetime import datetime
from .. import db
from werkzeug.utils import redirect


bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/create', methods=('POST','GET'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html',form=form)

