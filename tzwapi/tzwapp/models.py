from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = CloudinaryField()

    class Meta:
        unique_together = ('subject', 'category')

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = CloudinaryField()
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.CharField(max_length=255)


class Like(Interaction):
    class Meta:
        unique_together = ('user', 'lesson')
