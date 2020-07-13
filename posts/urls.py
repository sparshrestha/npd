from django.urls import path
from posts import views
from .views import feedback_exams
from .views import HomePage, HomePageView, HomePageProcessed, HomePageView100, CreateExamView, CreateExamView100, process_image, process_all_exam

urlpatterns = [
    path(
        '',
        HomePage.as_view(),
        name='home'
    ),
    path(
        'process40/',
        HomePageView.as_view(),
        name='home40'
    ),
    path(
        'processed40/',
        HomePageProcessed.as_view(),
        name='processed40'
    ),
    path(
        'process100/',
        HomePageView100.as_view(),
        name='home100'
    ),
    path(
        'exams/',
        CreateExamView.as_view(),
        name='add_exam40'
    ),
    path(
        'exams100/',
        CreateExamView100.as_view(),
        name='add_exam100'
    ),
    path(
        'exams/process-images/<str:exam_name>/', views.process_image, name='process_images'
    ),
    path(
        'exams/process-all-exams/', views.process_all_exam, name='process_all_exams'
    ),
    path(
        'exams/process-images100/<str:exam_name>/', views.process_image100, name='process_images100'
    ),
    path(
        'exams/process-all-exams100/', views.process_all_exam100, name='process_all_exams100')
    ,
    path(
        'exam/feedback/<str:processed_id>/', views.feedback_exams, name='feedback_exams'
    )
    ,
    path(
        'exam/feedback_all/', views.feedback_exams_all, name='feedback_exams_all'
    ),
    path('feedback_exams', feedback_exams, name='feedback_exams')
]
