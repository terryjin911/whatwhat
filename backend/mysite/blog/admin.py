from django.contrib import admin

from blog.models import Post


# Register your models here.

# 어드민 사이트에 개발자가 추가한 모델을 등록해준다.
# admin.site.register(Post)

# 위와 동일한 문법이지만 @(데코레이터) 코드 재사용하거나 코드량을 줄이기 위해 사용
# @데코레이터는 짧게 구현하기 위한거

@admin.register(Post)
# admin 사이트에서 보여질 모습을 정의, 보여질 모습을 바꿀 수도 있음
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')  # 출력항목
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # 슬러그 필드는 제목 입력시 자동채우기
