from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(default=" ",max_length=50,null=False,blank=False)
    image = models.ImageField(null=False,blank=False,upload_to='images/')
    blog_text = models.TextField(default=" ",max_length=100000,null=False,blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey('Category',null=False,blank=False , on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)


    def like_count(self):
        return self.like_set.count()


    def save(self, *args, **kwargs):
        if self.status == 'published' and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) :
        return self.name
    


class Category(models.Model):

    name = models.CharField(default=" ",max_length=50,null=False,blank=False)
    description = models.TextField(default=" ")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name

    def get_children(self):
        return self.children.all()


class Comment (models.Model):

    CHOICES = [
        ('1', ' 1'),
        ('2', ' 2'),
        ('3', ' 3'),
        ('4', ' 4'),
        ('5', ' 5'),
    ]

    

    comment_name = models.CharField(default=" ",max_length=50,null=False,blank=False)
    post = models.ForeignKey('Post', null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    Comment_text = models.TextField(default=" ",max_length=100000,null=False,blank=False)
    uplod_at = models.DateTimeField(auto_now_add=True)
    star = models.CharField(max_length=1, choices=CHOICES, default='3')
    replay_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')


    def __str__(self):
        return self.comment_name

    def get_children(self):
        return self.children.all()


class like(models.Model):


    post_name = models.ForeignKey('Post',null=False,blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)

class pin(models.Model):


    post_name = models.ForeignKey('Post',null=False,blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)




    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Package(models.Model):

#     name = models.CharField(max_length=50,null=False,blank=False)
#     description = models.TextField(default="this is a student")

#     def __str__(self) :
#         return self.name
    

# class Lesson(models.Model):

#     name = models.CharField(max_length=50,null=False,blank=False)
#     description = models.TextField(default="this is a student")
#     crip = models.DateField()

#     def __str__(self) :
#         return self.name
     

# class course (models.Model):
#     package=models.ForeignKey(Package,on_delete=models.CASCADE)
#     lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
#     # student=models.ManyToManyField(students)
#     name = models.CharField(max_length=50,null=False,blank=False)
#     description = models.TextField(default="this is a course")

#     def __str__(self) :
#         return self.name
    


# class member (models.Model):

#     name = models.CharField(max_length=50,null=False,blank=False)
#     phone_number= models.CharField(default='+98',max_length=13,null=False,blank=False)
#     email = models.EmailField(null=False,blank=True)
#     my_booled = models.BooleanField(blank=False)
#     data = models.DateTimeField()
#     file = models.FileField()
#     text = models.TextField(default='')
#     url = models.URLField(default='')

#     def __str__(self) :
#         return self.name
    
#     def clean(self):
#         if not self.my_booled:
#             raise ValidationError('You must check the my_booled box to continue.')

    