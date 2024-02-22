from django.contrib import admin
from appLcdi.models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display    = ['postTweet']
    search_fields   = ['postTweet']
    list_filter     = ['postTweet']
    list_per_page   = 3

admin.site.register(Tweet, TweetAdmin)