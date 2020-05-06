from django.urls import path
from .views import HomePageView, CreatePostView, process_image

urlpatterns = [
	path(
		'',
		HomePageView.as_view(),
		name='home'
	),
	path(
		'post/',
		CreatePostView.as_view(),
		name='add_post'
	),
	path(
		'post/process-images/',
		process_image,
		name='process_images'
	)
]
