"""magazineweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
# debug



urlpatterns = [

    path('',views.home,name="home" ),
    path('founders/',views.founders,name="founders" ),

    path('blog/<str:slug>',views.blogPost,name='blogPost'),
    path('quiz/<str:slug>',views.question,name='question'),
    path('comic/<str:slug>',views.comic,name='comic'),
    path('profile/<str:slug>',views.profile,name='profile'),

    path('apply/',views.apply,name="apply" ),
    #path('authorized_only/',views.authorized_only,name="authorized_only" ),
    path('accounts/profile/', views.adminlog, name = "adminlog"),
    path('newsletter/',views.newsletter,name="newsletter" ),
    path('likehome/<int:pk>',views.likehome,name="like_home" ),
    path('likecom/<int:pk>/<str:slug>',views.likecom,name="like_com" ),
    path('likepost/<str:slug>',views.likepost,name="like_post" ),

    path('likecomquiz/<int:pk>/<str:slug>',views.likecomquiz,name="like_comquiz" ),
    path('likequiz/<str:slug>',views.likequiz,name="like_quiz" ),
    path('likecomcomic/<int:pk>/<str:slug>',views.likecomcomic,name="like_comcomic" ),
    path('likecomic/<str:slug>',views.likecomic,name="like_comic" ),

    path('contact/',views.contact,name="contact" ),

    path('comics/',views.comics,name="comics" ),
    path('upanyax/',views.upanyax,name="upanyax" ),
    path('songs/',views.songs,name="songs" ),
    path('interviews/',views.interviews,name="interviews" ),
    path('stories/',views.stories,name="stories" ),
    path('science/',views.science,name="science" ),
    path('medical/',views.medical,name="medical" ),
    path('best_of_xonkhya/',views.best_of_xonkhya,name="best_of_xonkhya" ),
    path('history/',views.history,name="history" ),
    path('awareness/',views.awareness,name="awareness" ),
    path('bhoutik/',views.bhoutik,name="bhoutik" ),
    path('sports/',views.sports,name="sports" ),
    path('poems/',views.poems,name="poems" ),
    path('education/',views.education,name="education" ),

    path('more/',views.more,name="more" ),
    path('microstories/',views.microstories,name="microstories" ),
    path('gallery/',views.gallery,name="gallery" ),
    path('comedy/',views.comedy,name="comedy" ),

    path('quizes/',views.quizes,name="quizes" ),
    path('search/',views.search,name="search")





]



#debug



