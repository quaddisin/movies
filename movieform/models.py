from django.db import models

# Create your models here.

class AddMovieModel(models.Model):

    m_name = models.CharField(verbose_name="Movie Name",max_length=50)
    m_kind = models.CharField(verbose_name="Movie Kind",max_length=20)
    m_year = models.CharField(verbose_name="Movie Year",max_length=10)
    m_actors = models.CharField(verbose_name="Movie Actors",max_length=100)
    m_rank = models.CharField(verbose_name="Movie Rank Point",max_length=3)
    m_content = models.TextField(verbose_name="Movie Content",max_length=1000)
    m_image = models.FileField(verbose_name="Movie Image",blank=True,null=True)

    def __str__(self):
        return self.m_name
    
