from django.db import models


class Post(models.Model):
	title = models.TextField()
	cover = models.ImageField(upload_to = 'images/sheet/')
	template = models.FileField(upload_to='images/', default=None)
	marker = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.title
