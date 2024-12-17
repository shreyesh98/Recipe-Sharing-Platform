from django.contrib import admin
from .models import *
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name', 'last_name', 'role')
    
admin.site.register(CustomUser, userAdmin)

class recAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ing', 'cook', 'cat')
    
admin.site.register(Recipe, recAdmin)

class favAdmin(admin.ModelAdmin):
    list_display = ('name','recname')
    
    def recname(self,obj):
        return obj.rec_fav.name
    
    recname.short_description = 'Recipe Name'
        

admin.site.register(fav, favAdmin)


class comAdmin(admin.ModelAdmin):
    list_display = ('rec_com','com','author')
    
    def rec_com(self,obj):
        return obj.rec_comment.name
    
    rec_com.short_description = 'Recipe Name'
    
admin.site.register(Comments, comAdmin)