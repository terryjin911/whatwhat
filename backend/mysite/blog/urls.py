from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    # Example: /blog/
    path('', views.PostLV.as_view(), name='index'),

    path('<int:pk>', views.PostDV.as_view(), name='post_detail'),

    path('archive/', views.PostAV.as_view(), name='post_archive'),

    path('archive/<int:year>/',
         views.PostYAV.as_view(), name='post_year_archive'),

    path('archive/<int:year>/<str:month>/',
         views.PostMAV.as_view(), name='post_month_archive'),


    # Example: /blog/post/파이썬의장점은/
    # 정규식.
    # PostDV 는 PostDetailView
    # 여기서 slug값을 쓸지 pk(123이런거)를 쓸지 정함
    # re_path(r'^post/(?P<slug>[-\w]+)/$',
    #         views.PostDV.as_view(), name='post_detail'),

]
