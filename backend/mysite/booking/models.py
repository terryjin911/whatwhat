from django.db import models

# 장고 프레임워크 자체에서 설정 정보를 불러오는거
from django.conf import settings
# Create your models here.


class Booking(models.Model):
    # 예약 회원 고유번호 : 회원테이블의 id값 (FK)
    # 예약하는 당사자(구독자^ㅇ^)
    # related 관계를 맺게되면 relation이 생기는데 그것의 이름을 'booking'으로 지정한거임
    # 사용자의 고유번호 PK가 123456.. 사용자 고유번호로 찍히는거임
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='bookings')

    # 예약시작일과 종료일
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(null=True, blank=True)

    room = models.TextField(max_length=100)
    note = models.TextField()

    # 새로운 booking객체를 만들고 DB에 쏴줘야할때, 그 시간을 쏴주는거
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # self는 해당하는 클래스(booking)을 말함
    # 해당하는 row의 대표값을 출력해주는것
    # username과 이름을 같이 보여주면 어떤 사용자가 어떤 룸을 예약했는지 알 수 있음
    def __str__(self):
        return self.subscriber.username+""+self.room

    # 시스템 관리, 개발자를 위해 부수적으로 추가해놓은 정보를 제공해주는 Meta (다른 프로그래밍에서도 Meta는 그런 용도)
    # 목록형태의 데이터를 가져왔을 때 date_from이 내림차순으로 정렬되게 보여줌
    class Meta:
        ordering = ['-date_from']
