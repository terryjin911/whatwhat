# polls 어플리케이션관련 view함수 정의영역
# View 함수는 urlConf에 의해 맵핑된 사용자 url주소 호출시 실행됨
# View함수의 목적은 비지니스 로직을 구현하거나
# Model을 통해 데이터를 처리하거나 조회하거나
# Template 파일에 데이터를 전달하고 최종 템플릿 결과물을 브라우저에게 반환한다.
# 브라우저 반환결과값으로 html+data or json 데이터를 반환할수 있다.

# Qestion 모델객체를 참조하여 ORM기반 데이터 조회 기능구현
# get_object_or_404()메소드는 ORM제공메소드로 단일건 데이터를 조회제공함
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

# 클래스 뷰 상속을 위한 제너릭 뷰 참조.
from django.views import generic
from polls.models import Question, Choice


# Create your views here.


# http://localhost:8000/polls 주소 호출시 실행되는 View함수 정의
# 최종 전체 설문항목을 DB 조회해서 Template에 전달하여
# 최종 template 결과물(html)을 브라우저로 반환하는 기능을 제공함


class IndexView(generic.ListView):
    # template_name을 통해 템플릿명을 직접 지정할 수 있다(규칙)
    # 직접 지정하지 않으면 해당 모델(소문자)명_list.html (지정하지 않으면 자동지정)
    template_name = 'polls/index.html'

    # 템플릿에 전달 context데이터 속성명을 지정한다.
    # 지정하지 않으면 object로 전달됨
    context_object_name = 'lastest_question_list'

    # 해당 리스트 뷰에서 사용할 모델은 지정한다.
    # get_queryset()함수를 사용하지 않으면 지정된 모델의 모든 목록을 반환한다.
    # model = Question #어떤 모델의 데이터를 가져올지 설정해주는거니까 이거나 밑이나 하나는 써야..?

    # 특정조건의 데이터셋을 조회시에는 get_queryset 함수(정해져있는 기본개념)를 이용해 ORM 쿼리를 만든다
    # 만약 get_queryset을 사용하지 않으면 관련 모델이 모든 데이터를 반환한다
    # (=이걸 안 쓰면 indexview에서 사용하는 모든 객체가 전달이 됨)
    # 이 클래스 자체를 말함
    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]

# 설문 상세보기 및 설문처리 뷰함수정의
# polls/5 5번에 대한 고유번호는 url라우팅에서 pk파라메터로 전달해줌
# 자동클래스뷰로 전달된pk값 번호를 기준으로 단일정보를 조회해context값을 채워
# template에 소문자 모델명 context데이터 값으로 전달


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# 설문 상세페이지에서 보내온 사용자 설문정보를 저장하고 결과 페이지로 바로 이동시키는 뷰함수

# 단일 설문항목에 대한 결과 확인 페이지 반환 뷰함수
# generic.View들의 특징 : 다 정해져있는 규칙을 사용함


class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    # 전달된 설문고유번호를 이용해 단일 설문정보를 조회한다.
    question = get_object_or_404(Question, pk=question_id)

    try:
        # 사용자가 선택한 단일설문항목(빨강or노랑)정보를 조회한다.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "에러발생:데이터가 존재하지 않습니다."})
    else:
        # 조회된 설문항목의 votes 카운팅을 1더한다
        selected_choice.votes += 1

        # ORM save메소드를 통해 데이터를 업데이트한다.
        # save()메소드는 신규등록/수정할떄 사용한다.
        selected_choice.save()

        # reserve()메소드는 urlConf파일에서 name값이 results인 라우팅 주소정보를 가져와서
        # 해당 주소체계내에 파라메터값을 세팅해준다.
        # 이동할 주소를 reserse 메소들를 통해 출력 : polls/5/results
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
