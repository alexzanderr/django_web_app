
from django.db import models


# one to many relationship
"""
	basic idea:
	one reporter can write multiple articles
	one article is written by 1 reporter max
		meaning that the author is unique per article


"""
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    # linked to Reporter
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline