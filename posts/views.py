from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy, reverse

from GFoody.settings import BASE_DIR
from OMRchecker import OMRChecker
from .forms import PostForm
from .models import Post


class HomePageView(ListView):
	model = Post
	template_name = 'posts.html'


def process_image(request):
	print('----------called-------')
	OMRChecker(input_dir=['{}/media/images'.format(BASE_DIR)]).execute()
	return HttpResponseRedirect(reverse('home'))


class CreatePostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post.html'
	success_url = reverse_lazy('home')
