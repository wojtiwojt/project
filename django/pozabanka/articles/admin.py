from django.contrib import admin
from pozabanka.articles.models import Article, Source


admin.site.register([Article, Source])
