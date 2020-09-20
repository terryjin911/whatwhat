from django.shortcuts import render

# DRF (Django Rest Framework)에서 제공해주는 API 제너릭 뷰 참조. api서비스를 할때 기본적으로 제공해주는거
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# 전체 예약목록 데이터 제공 API 서비스 뷰
# generics 안에 ListCreateAPIView는 get방식으로 여러 건 조회 API 및 post api 2개의 오픈api를 동시에 제공한다
# api/bookings-get방식 조회리턴(여러개의 데이터베이스를 get방식으로 처리.), api/booking -post
# view를 만들었으면 라우팅하러가자 urls
class BookingList(generics.ListCreateAPIView):
    # ORM을 이용해 데이터를 모델에 담아 조회한다.
    # 직접 ORM을 짜서 제어하고 데이터를 전달해주고싶을때
    queryset = Booking.objects.all()

    # 모델에 담긴 조회결과를 하기 설정한 직렬화 클래스를 통해 JSON포멧으로 변환한다.
    serializer_class = BookingSerializer


# 단일 예약저옵 조회/수정/삭제 OPEN API 서비스 제공 API
# 업데이트하고 삭제하고. 이 디테일뷰는 단일건 조회하고 업데이트하고 삭제함
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):

    # 인증방식을 결정한다 - 토큰인증방식 적용(class명은 예약어)
    # authenticatioin_classes = (TokenAuthentication,)

    # 인증방식 적용여부 - 인증된 사용자만이 API를 호출할 수 있게 한다.
    # permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()

    # 시리얼라이저 클래스 is BookingSerializer
    serializer_class = BookingSerializer
