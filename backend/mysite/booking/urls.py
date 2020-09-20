
# path('booking/', include('booking.urls'))
from django.urls import path
from booking import views

app_name = 'booking'

# / 를 안 넣는 경우
# /api/booking/     /api/booking/1   /api/booking/5
urlpatterns = [
    # /api/booking/ 전체 데이터를 가져오고 얘가 등록처리를 함
    path('', views.BookingList.as_view()),

    # /api/booking/5
    path('<int:pk>/', views.BookingDetail.as_view()),
]
