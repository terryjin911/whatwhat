from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView

from blog.models import Post


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 지정하지 않으면 'blog/post_list.html'
    context_object_name = 'posts'  # 전달되는 context
    paginate_by = 2


class PostDV(DetailView):
    # model만 지정. 나머지는 자동임!!
    # 디폴트 템플릿 'blog/post_detail.html'
    # 기본전달 고유값은 pk(123) or slug 값
    # 전달되는 context이름은 object로 전달됨
    model = Post


#   ArchiveView
# 연도별 아카이브제공
# object_list, date_list 2개를 던져줌
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


# /blog/archive/2020
class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
