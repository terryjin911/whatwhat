from django.db import models

# Create your models here.

# 설문항목 관리 모델 정의
# models.Model 를 상속받아서 Question 클래스를 생성한다.
# Frimary Key컬럼은 id란 컬럼으로 자동 채번(Auto Increment)컬럼이 생성해준다.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# 설문항목 및 항목 선택 건수 저장 모델
# Choice 테이블도 id란 이름으로 FrimaryKey 컬럼이 자동생성(자동채번)
# Choice 테이블은 Question테이블의 PK인 id 컬럼을 참조한다.


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)  # Question 테이블에 PK ID 참조키
    choice_text = models.CharField(max_length=200)  # 설문 답변 항목 컬럼
    votes = models.IntegerField(default=0)  # 답변항목 선택건수 컬럼

    def __str__(self):
        return self.choice_text
