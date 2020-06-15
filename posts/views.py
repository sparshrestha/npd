from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy, reverse

from GFoody.settings import BASE_DIR
from OMRchecker import OMRChecker
from .forms import ExamsForm
from .models import Exams


class HomePageView(ListView):
    model = Exams
    template_name = 'posts.html'


def process_image(request, exam_name):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/' + exam_name]).execute()
    return HttpResponseRedirect(reverse('home'))


def process_all_exam(request):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/']).execute()
    return HttpResponseRedirect(reverse('home'))


class CreatePostView(CreateView):
    model = Exams
    form_class = ExamsForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
