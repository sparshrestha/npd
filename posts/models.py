from django.db import models
from django.conf import settings
import os


def sheet_upload_location(instance, filename):
    file_path = 'images/{exam_name}/sheets/{filename}'.format(exam_name=str(instance.title), filename=filename
                                                              )
    return file_path


def template_upload_location(instance, filename):  # removing empty media folders and get upload location
    file_path = 'images/{exam_name}/{filename}'.format(exam_name=str(instance.title), filename=filename
                                                       )
    media_root = getattr(settings, 'MEDIA_ROOT', None)
    for relative_root, dirs, files in os.walk(media_root, topdown=False):
        for dir_ in dirs:
            if not os.listdir(os.path.join(relative_root, dir_)):
                os.rmdir(os.path.join(relative_root, dir_))
    return file_path


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to=sheet_upload_location)
    template = models.FileField(upload_to=template_upload_location, default=None)
    marker = models.ImageField(upload_to=template_upload_location, null=True, blank=True)

    def __str__(self):
        return self.title
