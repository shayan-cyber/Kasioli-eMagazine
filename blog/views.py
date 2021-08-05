from django.shortcuts import render, redirect, get_object_or_404
from .models import Author,CommentHome, Post, Comment,Gallery , NewsLater,Likepost,Xonkhya, Quiz, Commentquiz,Likecomquiz,Likequiz,Comic,ComicImage,Commentcomic,Likecomic,Likecomcomic
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from random import shuffle

from django.db.models import Count
# Create your views here.
def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message1 = request.POST['message1']
        dp = request.FILES.get('dphome')
        print(dp)

        time1 = request.POST['date']
        time = time1.rsplit('G', 1)[0]



        if len(name) <= 80 and len(email) <= 40 and len(message1) <= 200:
            #comment = CommentHome.objects.all()
            comment = CommentHome(name=name,comment=message1,image=dp,time= time)
            comment.save()
            print(comment)
        return HttpResponseRedirect('/')


    comments = CommentHome.objects.all().order_by('-created_at')
    posts = Post.objects.all().order_by('-time')
    postshuffle = posts #list(posts)
    #shuffle(postshuffle)
    interviews = Post.objects.filter(category__category = 'Interview').order_by('-time')

    poems = Post.objects.filter(category__category = 'Poem').order_by('-time')

    upanyax = Post.objects.filter(category__category = 'Upanyax').order_by('-time')
    science = Post.objects.filter(category__category = 'Comedy').order_by('-time')
    comics = Comic.objects.all().order_by('-time')
    sports = Post.objects.filter(category__category = 'Microstory').order_by('-time')
    stories = Post.objects.filter(category__category = 'Story').order_by('-time')

    bigyan = Post.objects.filter(category__category = 'Science').order_by('-time')
    medical = Post.objects.filter(category__category = 'Medical').order_by('-time')
    song = Post.objects.filter(category__category = 'Song').order_by('-time')
    history = Post.objects.filter(category__category = 'History').order_by('-time')
    education = Post.objects.filter(category__category = 'শিক্ষা').order_by('-time')
    awarness = Post.objects.filter(category__category = 'Awareness').order_by('-time')
    bhoutik = Post.objects.filter(category__category = 'Bhoutik').order_by('-time')
    best = Post.objects.filter(category__category='Best_of_xonkhya').order_by('-time')
    gallery = Gallery.objects.all()
    galleryShuffle = list(gallery)
    shuffle(galleryShuffle)


    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]



    postsliked = Post.objects.all().annotate(
           bar_count=Count('likepost')
      ).order_by('-bar_count')
    postscommented = Post.objects.all().annotate(
           bar_count=Count('comment')
      ).order_by('-bar_count')



    number = Xonkhya.objects.all().order_by('-time').first()
    context = {

        "comments":comments,
        "posts":posts,
        'number':number,
        "postsliked":postsliked,
        "postscommented":postscommented,
        "interviews":interviews,
        "poems":poems,
        "upanyax":upanyax,
        "science":science,
        "comics":comics,
        "sports":sports,
        "stories":stories,
        'editorial':editorial,
        "best":best,
        "postshuffle":postshuffle,
        "galleryShuffle":galleryShuffle,


        "bigyan":bigyan,
        "medical":medical,
        "song":song,
        "history":history,
        "education":education,
        "awarness":awarness,
        "bhoutik":bhoutik,





    }

    return render(request,'index.html', context)


def search(request):
    query = request.POST.get('query')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    if len(query)>140:
        allPosts = Post.objects.none()
    else:
        allPoststitle = Post.objects.filter(title__icontains=query)
        allPostscontent = Post.objects.filter(content__icontains=query)
        allComic = Comic.objects.filter(title__icontains=query)
        allPosts = allPoststitle.union(allPostscontent)


    params = {'allPosts':allPosts,'allComic':allComic, 'query': query, 'editorial':editorial}
    return render(request,'search.html',params)
    #return HttpResponse('this is search')
#sections


from  django.core.paginator import Paginator

def poems(request):
    posts = Post.objects.filter(category__category='Poem').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/poem.html', context)


from  django.core.paginator import Paginator
#comic Start
def comics(request):
    posts = Comic.objects.all().order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/comics.html', context)
def comic(request,slug):
    print(slug)
    post = get_object_or_404(Comic, slug=slug)
    photos = ComicImage.objects.filter(comic=post)
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    #author1 = post.author
    print(post)
    #likes = Likepost.objects.filter(post=)
    posts = Comic.objects.filter(author=post.author).annotate(
           bar_count=Count('likecomic')
      ).order_by('-bar_count')
    print(posts)
    #post1 = post.title

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message1 = request.POST['message1']
        dp = request.FILES.get('dphome')

        time1 = request.POST['date']
        time = time1.rsplit('G', 1)[0]


        print(time)
        print(message1)
        if len(name) <= 80 and len(email) <= 40 and len(message1) <= 200:
            #comment = CommentHome.objects.all()
            comment = Commentcomic(name=name,comment=message1,post=post,image=dp, time= time )
            comment.save()
        return HttpResponseRedirect(reverse('comic', args=[str(slug)]))

    comments = Commentcomic.objects.filter(post=post).order_by('-created_at')


    context = {

        "comments":comments,
        "post":post,
        'posts':posts,
        'editorial':editorial,
        'photos':photos

    }




    #context = {'post': post}

    return render(request,'topics/comic-single.html',context)


def likecomic(request,slug):
    post = get_object_or_404(Comic, id = request.POST.get('com_id'))
    print(post)
    #like = Likepost.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likecomic(post=post, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('comic', args=[str(slug)]))


def likecomcomic(request, pk, slug):
    comm = get_object_or_404(Commentcomic, id = request.POST.get('com_id'))
    print(comm)
    like = Likecomcomic.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likecomcomic(comment=comm, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('comic', args=[str(slug)]))





#comic End
def founders(request):
    return render(request,'founders.html')

from  django.core.paginator import Paginator

def upanyax(request):
    posts = Post.objects.filter(category__category='Upanyax').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/upanyax.html', context)
from  django.core.paginator import Paginator

def songs(request):
    posts = Post.objects.filter(category__category='Song').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/songs.html', context)
from  django.core.paginator import Paginator

def interviews(request):
    posts = Post.objects.filter(category__category='Interview').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/interview.html', context)
from  django.core.paginator import Paginator

def stories(request):
    posts = Post.objects.filter(category__category='Story').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/story.html', context)
from  django.core.paginator import Paginator

def science(request):
    posts = Post.objects.filter(category__category='Science').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/science.html', context)
from  django.core.paginator import Paginator

def medical(request):
    posts = Post.objects.filter(category__category='Medical').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/medical.html', context)
from  django.core.paginator import Paginator

def history(request):
    posts = Post.objects.filter(category__category='History').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/history.html', context)
def awareness(request):
    posts = Post.objects.filter(category__category='Awareness').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/awareness.html', context)

def bhoutik(request):
    posts = Post.objects.filter(category__category='Bhoutik').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'about.html', context)



def sports(request):
    posts = Post.objects.filter(category__category='Sports').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/sports.html', context)

def education(request):
    posts = Post.objects.filter(category__category='শিক্ষা').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/education.html', context)

def more(request):
    posts1 = Post.objects.exclude(category__category__in=['Poem', 'Story','History', 'Sports','Best_of_xonkhya', 'Science','শিক্ষা','Medical', 'Upanyax','Awareness','Song','Interview','Comics','Comedy','Editorial','Microstory','Bhoutik']).order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts1, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts1)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/more.html', context)
def best_of_xonkhya(request):
    posts = Post.objects.filter(category__category='Best_of_xonkhya').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/best.html', context)
def microstories(request):
    posts = Post.objects.filter(category__category='Microstory').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/microstory.html', context)


def gallery(request):
    posts = Gallery.objects.all()
    editorial = Post.objects.filter(category__category = 'Editorial')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/gallery.html', context)



def comedy(request):
    posts = Post.objects.filter(category__category='Comedy').order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/comedy.html', context)


#sectionEnd

#quiz start
def quizes(request):
    posts = Quiz.objects.all().order_by('-time')
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(posts)
    context = {
        'posts':posts,
        'editorial':editorial
    }
    return render(request,'topics/quiz.html', context)


def question(request,slug):
    print(slug)
    post = get_object_or_404(Quiz, slug=slug)
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    #author1 = post.author
    print(post)
    #likes = Likepost.objects.filter(post=)
    posts = Quiz.objects.filter(author=post.author).annotate(
           bar_count=Count('likequiz')
      ).order_by('-bar_count')
    print(posts)
    #post1 = post.title

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message1 = request.POST['message1']
        dp = request.FILES.get('dphome')

        time1 = request.POST['date']
        time = time1.rsplit('G', 1)[0]


        print(time)
        print(message1)
        if len(name) <= 80 and len(email) <= 40 and len(message1) <= 200:
            #comment = CommentHome.objects.all()
            comment = Commentquiz(name=name,comment=message1,post=post,image=dp, time= time )
            comment.save()
        return HttpResponseRedirect(reverse('question', args=[str(slug)]))

    comments = Commentquiz.objects.filter(post=post).order_by('-created_at')


    context = {

        "comments":comments,
        "post":post,
        'posts':posts,
        'editorial':editorial

    }




    #context = {'post': post}

    return render(request,'topics/quiz-single.html',context)



def likequiz(request,slug):
    post = get_object_or_404(Quiz, id = request.POST.get('com_id'))
    print(post)
    #like = Likepost.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likequiz(post=post, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('question', args=[str(slug)]))


def likecomquiz(request, pk, slug):
    comm = get_object_or_404(Commentquiz, id = request.POST.get('com_id'))
    print(comm)
    like = Likecomquiz.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likecomquiz(comment=comm, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('question', args=[str(slug)]))


#quizend



#profile

def profile(request,slug):
    profiledetail = get_object_or_404(Author, name = slug)
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    posts = Post.objects.filter(author__name=slug).order_by('-time')
    pics = Gallery.objects.filter(PC__name=slug)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    paginatorPics = Paginator(pics, 3)
    pagePics = request.GET.get('pagePics')
    pics = paginatorPics.get_page(pagePics)

    print(posts)
    context = {
        'posts':posts,
        'pics':pics,

        "profile":profiledetail,
        'editorial':editorial
    }
    return render(request,'author-detail.html', context)


#profile






def blogPost(request,slug):
    print(slug)
    post = get_object_or_404(Post, slug=slug)
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    #author1 = post.author
    print(post)
    #likes = Likepost.objects.filter(post=)
    posts = Post.objects.filter(author=post.author).annotate(
           bar_count=Count('likepost')
      ).order_by('-bar_count')
    print(posts)
    #post1 = post.title

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message1 = request.POST['message1']
        dp = request.FILES.get('dphome')

        time1 = request.POST['date']
        time = time1.rsplit('G', 1)[0]


        print(time)
        print(message1)
        if len(name) <= 80 and len(email) <= 40 and len(message1) <= 200:
            #comment = CommentHome.objects.all()
            comment = Comment(name=name,comment=message1,post=post,image=dp, time= time )
            comment.save()
        return HttpResponseRedirect(reverse('blogPost', args=[str(slug)]))

    comments = Comment.objects.filter(post=post).order_by('-created_at')


    context = {

        "comments":comments,
        "post":post,
        'posts':posts,
        'editorial':editorial

    }




    #context = {'post': post}

    return render(request,'blog-single.html',context)
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def apply(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']

        #email to Admin
        template = render_to_string('apply1.html', {'name':name, 'email': email, "message":message, "phone":phone})
        email1 = EmailMessage(
            name + ' Has Apllied For Admin',
            template,
            settings.EMAIL_HOST_USER,
            ['debroyshayan@gmail.com'],

            )
        email1.fail_silently = False
        email1.send()
        context ={'name':name}


        #email to user

        template2 = render_to_string('apply2.html', {'name':name, 'email': email, "message":message, "phone":phone})
        email2 = EmailMessage(
            name + ' , Your application is accepted',
            template2,
            settings.EMAIL_HOST_USER,
            [email],

            )
        email2.fail_silently = False
        email2.send()





    return render(request,'account/login.html',context)

def adminlog(request):
    return render(request, 'authorized_only.html')
#def adminlog(request):
    #pass
def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('nlemail')
        print(email)

        nl = NewsLater(email = email)
        nl.save()
    return redirect('/')

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .models import Like
def likehome(request, pk):
    comm = get_object_or_404(CommentHome, id = request.POST.get('com_id'))
    print(comm)
    like = Like.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Like(comment=comm, prk = i)

    like1.save()
    return HttpResponseRedirect('/')
from .models import Likecom
def likecom(request, pk, slug):
    comm = get_object_or_404(Comment, id = request.POST.get('com_id'))
    print(comm)
    like = Likecom.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likecom(comment=comm, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('blogPost', args=[str(slug)]))



    #comm.
def likepost(request,slug):
    post = get_object_or_404(Post, id = request.POST.get('com_id'))
    print(post)
    #like = Likepost.objects.filter(comment=comm)
    #print(like.count)

    i =+1
    like1 = Likepost(post=post, prk = i)

    like1.save()
    return HttpResponseRedirect(reverse('blogPost', args=[str(slug)]))


def contact(request):
    editorial = Post.objects.filter(category__category = 'Editorial').order_by('-time')[0]
    if request.method == 'POST':

        name = request.POST['fname']
        #name2 = request.POST['fname']
        email = request.POST['eaddress']
        message = request.POST['message']
        phone = request.POST['tel']


        #email to Admin
        template1 = render_to_string('con1.html', {'name':name, 'email': email, "message":message, "phone":phone})
        email1 = EmailMessage(
            name + ' Has Gave Us Feedback',
            template1,
            settings.EMAIL_HOST_USER,
            ['debroyshayan@gmail.com'],

            )
        email1.fail_silently = False
        email1.send()

        context ={'name':name, 'editorial':editorial}

        #email to user

        template2 = render_to_string('con2.html', {'name':name, 'email': email, "message":message, "phone":phone})
        email2 = EmailMessage(
            name + ' , We Received You Feedback',
            template2,
            settings.EMAIL_HOST_USER,
            [email],

            )
        email2.fail_silently = False
        email2.send()
        name2 ="shayan"
        return render(request,'contact.html',context)







    else:
        return render(request, 'contact.html')
















#Debug
from django.http import HttpResponseNotFound
from sentry_sdk import capture_message


def my_custom_page_not_found_view(*args, **kwargs):
    capture_message("Page not found!", level="error")

    # return any response here, e.g.:
    return HttpResponseNotFound("Not found")