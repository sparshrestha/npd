from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy, reverse

from OMRchecker import OMRChecker
from .forms import PostForm
from .models import Post


class HomePageView(ListView):
	model = Post
	template_name = 'posts.html'


def process_image(request):
	print('----------called-------')
	OMRChecker(input_dir=['/home/xzibit/Documents/Practice/npd/media/images']).execute()
	return HttpResponseRedirect(reverse('home'))


class CreatePostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post.html'
	success_url = reverse_lazy('home')
