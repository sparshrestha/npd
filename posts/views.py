from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
	model = Post
	template_name = 'posts.html'


def process_image(req):
	form = PostForm(req.POST or None)
	if form.is_valid():
		form.save()
		form = PostForm()
	context = {
		'fm': fm
	}
	return render(req, 'posts.html', context)


class CreatePostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post.html'
	success_url = reverse_lazy('home')