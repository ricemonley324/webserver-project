from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    """
    pybo 목록 출력
    """

    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(subject__icontains=kw)

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj,
        'kw': kw
    }

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)

    question.view_count += 1
    question.save()

    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)