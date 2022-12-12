# url 생성 및 기능구현

from flask import Blueprint, render_template, request, jsonify
from pybo.models import Question

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list = question_list,id='홍길동')

@bp.route('/test')
def test():
    return render_template('index.html')

@bp.route('/chatbot',methods=['POST'])
def chatbot():
    # print('채팅중')
    result = request.get_json()
    print(result)
    print('영화제목 : {}'.format(result['queryResult']['parameters']['movie']))
    r = jsonify(
        fulfillment_text="영화는 다음과 같습니다",
        fulfillment_messages=[
            {
                "payload":{
                    "richContent":[
                        [
                            {
                                "type": "image",
                                "rawUrl": "https://img1.daumcdn.net/thumb/C300x430/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4899f10a714f3b1cb5bf9569f84e96df0020d414",
                                "accessibilityText": "example logo"
                            }
                        ]

                    ]
                }
            }
        ]
    )
    return r