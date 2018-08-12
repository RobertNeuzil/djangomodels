from django.db import models


class Programmer (models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Company (models.Model):
	name = models.CharField(max_length=20)
	programmers = models.ForeignKey(Programmer, on_delete=models.CASCADE)
	languages = models.ManyToManyField(Language)

	def __str__(self):
		return self.name

