from rest_framework import serializers

from .models import Booking


# Booking 모델에 대한 직렬화 클래스 정의
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # 젠부구다사이 ^^,,,
        fields = '__all__'
