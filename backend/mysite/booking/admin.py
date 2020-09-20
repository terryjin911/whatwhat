from django.contrib import admin

# 현재 models.py 안에 있는 Booking을 참조함
from .models import Booking

# Register your models here.


@admin.register(Booking)
# 레지스터 안에 있는 booking을 제어
# 굳이 안 해줘도 되는데(?)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscriber', 'room',
                    'date_from', 'date_to', 'created', 'updated']
    list_editable = ['room', 'date_from', 'date_to']
    # 참조하는 컬럼, 다른 곳의 id를 참조한다
    raw_id_fields = ['subscriber']
