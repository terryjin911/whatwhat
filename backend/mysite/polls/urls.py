# polls 어플리케이션 전용 라우팅 정의 파일
from django.contrib import admin
from django.urls import path
from polls import views

# 패스의 개별 name값 앞에 어플리케이션을 구분해주는 구분자로 작용
# url,reverse 등에서 name값을 통해 접근시 반드시 app_name:name 형식으로 name값을 호출해줘야함.

# View.as_view()는 클래스 초기화함수 위에 view.py를 불러오는 거

app_name = 'polls'

# <int:pk> 설정으로 변경
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
