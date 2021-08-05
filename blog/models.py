from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.conf import settings
# Create your models here.
class Xonkhya(models.Model):
    title = models.CharField(max_length=400)
    xonkhya = models.CharField(max_length=150)
    description = HTMLField()
    time = models.DateTimeField()

    def __str__(self):
        return self.xonkhya


class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default="")
    Profile_Picture = models.ImageField(upload_to='dp')
    social_media_link = models.CharField(max_length=120)



    def __str__(self):
        return self.name


   # user =
class Comic(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    xonkhya = models.ForeignKey(Xonkhya,on_delete=models.CASCADE, default="")

    slug = models.CharField(max_length=200)

    time = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='posts',default="20192537-hand-drawn-ink-quill-and-bottle-vector.jpg", blank=True)
    def __str__(self):
        return  self.title  + '  from '  + self.author.name
class ComicImage(models.Model):
    comic = models.ForeignKey(Comic, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    def __str__(self):
        return self.comic.title





class Commentcomic(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Comic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment', blank=True)

    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.comment + ' from ' + self.post.title

class Likecomcomic(models.Model):
    comment = models.ForeignKey(Commentcomic, on_delete=models.CASCADE)
    prk = models.IntegerField(null=True)

    def __str__(self):
        return self.comment.comment
class Likecomic(models.Model):
    prk = models.IntegerField(null=True)
    post = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + ' Likes'
"""
#Poem:
class Poem(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentPoem(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)





#microstory:
class Microstory(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentMicrostory(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#Articles
class Other(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentOther(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#Story
class Story(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentStory(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#Facts:
class Gyan_Bigyan(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentGyan_Bigyan(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)


#Humour:

class Rakh_Rachana(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentRakh_Rachana(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)


#Comics:

class Comic(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentComic(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#Upanyax

class Dharavahik_Upanyax(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentDharavahik_Upanyax(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#critics

class Critic(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentCritic(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

#Photograph

class Photograph(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    background_image_optional = models.ImageField(upload_to='posts', blank=True)
    ImageTop_optional = models.ImageField(upload_to='posts', blank=True)
    ImageBottom_optional = models.ImageField(upload_to='posts', blank=True)


    content = HTMLField()
    time = models.DateTimeField()
class CommentPhotograph(models.Model):
    comment = models.TextField()
    Post = models.ForeignKey(Poem,on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)


"""
#comment home:
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/comment')
class CommentHome(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comment', blank=True)

    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.comment

class Like(models.Model):
    #count = models.IntegerField(blank=False, null=False, default=0)
    comment = models.ForeignKey(CommentHome, on_delete=models.CASCADE)
    prk = models.IntegerField(null=True)

    def __str__(self):
        return self.comment.comment

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
class NewsLater(models.Model):
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.email
class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    xonkhya = models.ForeignKey(Xonkhya,on_delete=models.CASCADE, default="")

    ImageTop_optional = models.ImageField(upload_to='posts', default="20192537-hand-drawn-ink-quill-and-bottle-vector.jpg", blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100)
    content = HTMLField()
    time = models.DateTimeField()
    def __str__(self):
        return  self.title  + '  from '  + self.author.name + ' of ' + self.category.category


class Likepost(models.Model):
    prk = models.IntegerField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + ' Likes'


#sending mail
from django.contrib.auth.models import User


import html2text
users = User.objects.filter(is_staff=True)
users2 = NewsLater.objects.all()
@receiver(post_save, sender=Post, dispatch_uid="update_stock_count")
def first_mail(sender, instance, **kwargs):
    from django.contrib.auth.models import User

    list1=[]
    for user1 in users:


        emails1 = user1.email

        #print(emails1)
        list1.append(user1.email)
    list2 = []
    for user2 in users2:


        emails2 = user2.email

        print(emails2)
        list2.append(user2.email)

    print(list2)
    if kwargs['created']:
        #print("email sent")
        #user_email = instance.client.email
        emails = emails1
        #print('list')
        #print(emails)
        postname = instance.title
        postauthor = instance.author
        postcategory = instance.category
        postslug = instance.slug
        h = html2text.HTML2Text()
        postcontent = h.handle(instance.content)
        #print(postname,postcontent)
        #print(postauthor)

         #email to Admin
        print(list2)
        print(list1)
        template = render_to_string('apply3.html', {'postname':postname,  "postauthor":postauthor, "postcontent":postcontent, "postcategory":postcategory})
        email1 = EmailMessage(
            'New Content Has Been Posted By ' + str(postauthor) ,
            template,
            settings.EMAIL_HOST_USER,
            list1,

            )
        email1.fail_silently = False
        email1.send()
        print('sent')






        template2 = render_to_string('apply4.html', {'postname':postname,  "postauthor":postauthor, "postcontent":postcontent, "postcategory":postcategory, "postslug":postslug})
        email2 = EmailMessage(
            str(postauthor) + ' Has Posted New Content In Kasioli' ,
            template2,
            settings.EMAIL_HOST_USER,
            list2,
            )
        email2.fail_silently = False
        email2.send()
        print('sent successfully')




#Quiz
class Quiz(models.Model):
    title = models.CharField(max_length=400)
    content = HTMLField()
    thumbnail = models.ImageField(upload_to='posts',default="20192537-hand-drawn-ink-quill-and-bottle-vector.jpg", blank=True)
    xonkhya = models.ForeignKey(Xonkhya,on_delete=models.CASCADE, default="")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField()
    answer = models.CharField(max_length= 400, default = "")
    def __str__(self):
        return  self.title  + '  from '  + self.author.name



class Commentquiz(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment', blank=True)

    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.comment + ' from ' + self.post.title

class Likecomquiz(models.Model):
    comment = models.ForeignKey(Commentquiz, on_delete=models.CASCADE)
    prk = models.IntegerField(null=True)

    def __str__(self):
        return self.comment.comment
class Likequiz(models.Model):
    prk = models.IntegerField(null=True)
    post = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + ' Likes'
#quizEND






class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment', blank=True)

    time = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.comment + ' from ' + self.post.title
class Likecom(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    prk = models.IntegerField(null=True)

    def __str__(self):
        return self.comment.comment


class Gallery(models.Model):
    ImageTop_optional = models.ImageField(upload_to='posts')
    PC = models.ForeignKey(Author,on_delete=models.CASCADE)
    Short_Description = models.CharField(max_length = 150)
    def __str__(self):
        return self.Short_Description + ' from ' + self.PC.name



"""
#sending mail
from django.contrib.auth.models import User

import html2text
users2 = NewsLater.objects.all()
@receiver(post_save, sender=Post, dispatch_uid="update_stock_count")
def first_mail(sender, instance, **kwargs):
    from django.contrib.auth.models import User

    list1=[]
    for user1 in users:


        emails1 = user1.email

        #print(emails1)
        list1.append(user1.email)
    #print(list1)
    if kwargs['created']:
        #print("email sent")
        #user_email = instance.client.email
        emails = emails1
        #print('list')
        #print(emails)
        postname = instance.title
        postauthor = instance.author
        postcategory = instance.category
        postslug = instance.slug
        h = html2text.HTML2Text()
        postcontent = h.handle(instance.content)
        #print(postname,postcontent)
        #print(postauthor)

         #email to Admi
        template = render_to_string('apply4.html', {'postname':postname,  "postauthor":postauthor, "postcontent":postcontent, "postcategory":postcategory, "postslug":postslug})
        email1 = EmailMessage(
            'New Content Has Been Posted By ' + str(postauthor) ,
            template,
            settings.EMAIL_HOST_USER,
            list1,

            )
        email1.fail_silently = False
        email1.send()
        print('sent')
        print(list1)
"""
