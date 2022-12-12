from flask import Blueprint
from pybo.models import Question
from datetime import datetime
from pybo import db

bp = Blueprint('news',__name__,url_prefix='/news')

@bp.route('/top/<int:newsno>')
def news_top(newsno):
    print(newsno)
    return('top 뉴스입니다.')

@bp.route('/week')
def news_week():
    return '주간 뉴스입니다.'

# @bp.route('login/<id>/<pw>')
# def login(id,pw):
#     print(id)
#     print(pw)
#     return 'login'

@bp.route('/insert_qa')
def insert_qa():

    for temp in range(10):
        q = Question(subject='질문 {}'.format(temp),content='내용 {}'.format(temp),create_date=datetime.now())
        db.session.add(q) #db 세션에 올림
    db.session.commit() #db에 적용

    return '데이터 입력 완료!'

@bp.route('/get_qa_all')
def get_qa_all():
    result = Question.query.all()
    for temp in result:
        print(temp.id)
        print(temp.subject)
        print(temp.content)
        print(temp.create_date)
    return '총 게시글 : {} 개'.format(len(result))

@bp.route('get_qa_pk/<int:pk>')
def get_qa_pk(pk):
    try:
        result = Question.query.get(pk)
        print(result.subject)
        print(result.content)
        print(result.create_date)
        return '가져오기 완료!'
    except:
        return '없는 PK번호입니다.'

@bp.route('get_qa_title/<title>')
def get_qa_title(title):
    result = Question.query.filter(Question.subject == title).all()
    content_list = []
    for temp in result:
        content_list.append(temp.content)
        print(temp.id)
        print(temp.subject)
        print(temp.content)
        print(temp.create_date)
    return content_list