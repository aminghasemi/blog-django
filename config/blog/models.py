from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# my managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.
class Category(models.Model):
    parent=models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    status=models.BooleanField(default=True)
    position=models.IntegerField()
    

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")
        ordering=['parent__id','position']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

    objects=CategoryManager()    



class Article(models.Model):
    STATUS_CHOICES= (
        ('d','Draft'),
        ('p', 'Published')
    )
    author=models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles')
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=100, unique=True)
    category=models.ManyToManyField(Category, related_name="articles")
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="images")
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title  


    objects=ArticleManager()

