from django.urls import path
from posts import views
from .views import HomePageView, CreatePostView, process_image, process_all_exam

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
	),
	path(
		'exams/process-all-exams/', views.process_all_exam, name='process_all_exams')
]
