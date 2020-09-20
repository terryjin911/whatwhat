# 개발자 정의 모델 클래스를 Admin웹사이트에 반영되게 처리한다.

from django.contrib import admin

# polls 어플리케이션의 models.py파일에서 정의한 모델 클래스를 참조한다.
from polls.models import Question, Choice


# Register your models here.

# 어드민 사이트에 개발자가 추가한 모델을 등록해준다.
admin.site.register(Question)
admin.site.register(Choice)
