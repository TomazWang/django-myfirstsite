# trips/models.py

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add=True)

	# Model fields
	# CharField - chars
	# TextField - massive text
	# URLField  - for urls
	# DateTimeField - for times


	# 更改顯示方式
	def __str__(self):
		return self.title