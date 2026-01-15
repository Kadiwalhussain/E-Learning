from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Text(BaseContent):
    body = models.TextField()

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(
        Course, related_name='modules', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in':('text', 'video', 'image', 'file')
        }
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('text', 'textitem', 'file', 'image', 'video')}
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


# Proxy model example
# A concrete BaseContent model for proxy inheritance demonstration
# Note: This is separate from the abstract BaseContent above
class ContentBase(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'courses_contentbase'

    def __str__(self):
        return self.title


class OrderedContent(ContentBase):
    class Meta:
        proxy = True
        ordering = ['created']

    def created_delta(self):
        return timezone.now() - self.created


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class TextItem(ItemBase):
    content = models.TextField()

    def __str__(self):
        return self.title


class File(ItemBase):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title


class Image(ItemBase):
    file = models.FileField(upload_to='images')

    def __str__(self):
        return self.title


class Video(ItemBase):
    url = models.URLField()

    def __str__(self):
        return self.title