from django.urls import path
from posts import views

urlpatterns = [
    path(
        '',
        views.HomePage.as_view(),
        name='home'
    ),
    path(
        'process40/',
        views.HomePageView.as_view(),
        name='home40'
    ),
    path(
        'processed40/',
        views.HomePageProcessed.as_view(),
        name='processed40'
    ),
    path(
        'process100/',
        views.HomePageView100.as_view(),
        name='home100'
    ),
    path(
        'exams/',
        views.CreateExamView.as_view(),
        name='add_exam40'
    ),
    path(
        'exams100/',
        views.CreateExamView100.as_view(),
        name='add_exam100'
    ),
    path(
        'exams/process-images/<str:exam_name>/',
        views.process_image,
        name='process_images'
    ),
    path(
        'exams/process-all-exams/',
        views.process_all_exam,
        name='process_all_exams'
    ),
    path(
        'exams/process-images100/<str:exam_name>/',
        views.process_image100,
        name='process_images100'
    ),
    path(
        'exams/process-all-exams100/',
        views.process_all_exam100,
        name='process_all_exams100'
    )
    ,
    # path(
    #     'exam/feedback/<str:processed_id>/', views.feedback_exams, name='feedback_exams'
    # )
    # ,
    path(
        'exam/feedback_all/',
        views.feedback_exams_all,
        name='feedback_exams_all'
    ),
    # path('feedback_exams', feedback_exams, name='feedback_exams'),

    # retotal
    path(
        'processed40/<int:id>/retotal',
        views.retotal_processed40,
        name='posts_processedmarks_retotal'
    ),
    # process exam
    path(
        'exam/<int:exam_id>/process',
        views.process_exam,
        name='process_exam'
    ),
    # process exam100
    path(
        'exam100/<int:exam_id>/process',
        views.process_exam100,
        name='process_exam100'
    ),
    # send feedback for exam
    path(
        'exam/<int:exam_id>/feedback',
        views.SendExamFeedbackView.as_view(),
        name='exam_feedback'
    ),
    # send feedback for exam
    path(
        'exam100/<int:exam_id>/feedback',
        views.SendExam100FeedbackView.as_view(),
        name='exam100_feedback'
    )
]
