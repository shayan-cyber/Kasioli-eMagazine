from django.contrib import admin
from .models import Comic,ComicImage,Likecomic,Likecomcomic,Commentcomic, Author,CommentHome, Post, Comment , Category , NewsLater , Likecom,Like,Likepost,Xonkhya,Quiz,Likequiz,Likecomquiz,Commentquiz,Gallery
# Register your models here.




admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentHome)
#admin.site.register(NewsLater)

admin.site.register(Xonkhya)
admin.site.register(Quiz)
admin.site.register(Commentquiz)
admin.site.register(Commentcomic)
admin.site.register(Category)
admin.site.register(Gallery)



#for Comics:
class ComicImageAdmin(admin.StackedInline):
    model = ComicImage

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    inlines = [ComicImageAdmin]
    class Meta:
        model = Comic
@admin.register(ComicImage)

class ComicImageAdmin(admin.ModelAdmin):
    pass






#class CommentCritic(admin.ModelAdmin):
 # def has_module_permission(self, request):
   # return False
"""
class CommentCritic(admin.ModelAdmin):
    def get_model_perms(self, request):

        Return empty perms dict thus hiding the model from admin index.

        return {}
admin.site.register(CommentCritic)
"""


def register_hidden_models(*model_names):
    for m in model_names:
        ma = type(
            str(m)+'Admin',
            (admin.ModelAdmin,),
            {
                'get_model_perms': lambda self, request: {}
            })
        admin.site.register(m, ma)

register_hidden_models(Likepost,Like,Likecom,Likecomquiz,Likequiz,Likecomcomic,Likecomic,NewsLater)


