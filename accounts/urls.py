from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Server Based OMR System Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'Manage Users|Groups|Exams'                 # default: "Site administration"
admin.site.site_title = 'Admin Panel'  # default: "Django site admin"
urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup')
]
