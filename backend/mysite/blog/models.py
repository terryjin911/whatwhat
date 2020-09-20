# 파이썬 파란책 74 page
from django.db import models
from django.urls import reverse

# 설문항목 관리 모델 정의
# models.Model 를 상속받아서 Question 클래스를 생성한다.
# Frimary Key컬럼은 id란 컬럼으로 자동 채번(Auto Increment)컬럼이 생성해준다.

# 게시글 모델 정의 : Post
# Post는 models의 Model을 상속받음


class Post(models.Model):
    # models.CharField 문자열 컬럼을 만든다는 뜻. verbose_name(별칭)는 text필드 앞에 라벨명으로 붙는 그거임
    title = models.CharField(verbose_name='TITLE', max_length=50)

    # 글 고유번호를 대체하는 텍스트형태의 고유값,
    # slug는 id값으로 쓰기 위한것. 이름은 slug 유니크하게, 중복된 값이 들어가지않게 설정해주는 unique=True
    # allow_unicode는 한글지원을 하기위해서 True로 설정해줬음(/blog/파이썬이란), helptext는 설명문구 /admin에서 확인ㄱㄴ
    slug = models.SlugField(
        'SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')

    # 한줄요약같은거, 안 써도 되는 부분이라서 blank값을 true줬음(null허용)
    description = models.CharField(
        'DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')

    # 많은양의 데이터를 입력할떄는 textField를 꼭 넣어준다
    content = models.TextField('CONTEXT')

    # auto_now_add 기본적으로 날짜가 들어감. 신규게시글 객체가 만들어진 시점의 날짜, 해당하는 객체 (Post)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)

    # auto_now 신규 Post객체에서 date객체(db)로 들어가는 시점의 시간 저장
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    # Post 테이블 컬럼의 부수적인 정보 정의시 사용

    class meta:

        # 단수형 별칭과 복수형 별칭 정의
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # 기본테이블명 구조: 앱명_모델클래스명-> blog_posts로 만들어짐
        db_table = 'blog_posts'

        # 기본 내림차순 컬럼정의: 최신 게시글부터 내림차순으로 가져온다
        ordering = ('-modify_dt',)

    # 객체의 문자열 표현 메소드
    def __str__(self):
        return self.title

    # url 조회 리턴/reverse를 호출함
    # 현재 보고있는 것이 /blog/5 라면
    # def get_absolute_url(self):
    #     return reverse('blog:post_detail', args=(self.slug,))

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.pk,))

    # 장고 프레임워크 ORM에서 기본적으로 제공해주는것
    # 현재 보고있는 게시글의 이전 게시글 조회

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    # 현재 보고있는 게시글의 다음 게시글 조회
    def get_next(self):
        return self.get_next_by_modify_dt()

    # 기본적으로 slug 기반이기 때문에

# 설문항목 및 항목 선택 건수 저장 모델
# Choice 테이블도 id란 이름으로 FrimaryKey 컬럼이 자동생성(자동채번)
# Choice 테이블은 Question테이블의 PK인 id 컬럼을 참조한다.
