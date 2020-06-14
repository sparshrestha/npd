from django.urls import path
from posts import views
from .views import HomePageView, CreatePostView, process_image

urlpatterns = [
	path(
		'',
		HomePageView.as_view(),
		name='home'
	),
	path(
		'exams/',
		CreatePostView.as_view(),
		name='add_post'
	),
	path(
		'exams/process-images/<str:exam_name>/', views.process_image, name='process_images'
	)
]
