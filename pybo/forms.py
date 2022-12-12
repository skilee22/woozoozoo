from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목',validators=[DataRequired()])
    content = TextAreaField('내용',validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름',validators=[DataRequired(),Length(min=3,max=20)])
    password1 = PasswordField('비밀번호',validators=[DataRequired(), EqualTo('password2','비밀번호가 다릅니다.'),Length(min=6,max=30)])
    password2 = PasswordField('비밀번호확인',validators=[DataRequired()])
    email = EmailField('이메일',validators=[DataRequired(),Email()])
    phone = StringField('전화번호',validators=[DataRequired()])