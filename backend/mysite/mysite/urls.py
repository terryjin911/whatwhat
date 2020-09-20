"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 사용자가 호출하는 URL주소와 맵핑되는 View(Controller)의 해당 액션 메소드와 1:1로 맵핑정의한다.
# 사용자 라우팅 맵핑처리 영역
# polls어플리케이션의 view 기능이 정의된 views.py 파일을 참조한다.
from django.contrib import admin
from django.urls import path, include, re_path
# URL 최상위 라우팅 테이블 정의
from polls.views import IndexView


# 장고 swagger를 위한 참조
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authtoken import views


schema_view = get_schema_view(
    openapi.Info(
        title="My site OPEN API 명세서",
        default_version='v1',
        description="설문조사, 블로그, 예약 어플리케이션 관리 OPEN API입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# http://localhost:8000/swagger/
urlpatterns = [
    path('admin/', admin.site.urls),

    # 사용자 아이디와 암호를 전달받아 토큰을 발급해주는 rest framework 기능
    path('api/get_token/', views.obtain_auth_token),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),

    # polls어플리케이션의 IndexView를 메인페이지로 설정 #하위에 있는 어플리케이션은 메인으로 잡아줌
    path('', IndexView.as_view(), name="main"),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    # 이건 api다 라는걸 보여주기위해.. 여기에 api 안 넣어도 되긴함 ㅋ
    path('api/booking/', include('booking.urls')),
]
