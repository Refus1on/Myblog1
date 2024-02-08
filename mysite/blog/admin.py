from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Настройка внешнего вида на сайте админки
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Появится боковая панель по которой можно проводить фильтры
    list_filter = ['status', 'created', 'publish', 'author']
    # Появится строка поиска
    search_fields = ['title', 'body']
    # нужно для автозаполнения поле slug
    prepopulated_fields = {'slug': ('title',)}
    # при добавлении поста вместо выпадающего списка будет поиск по юзерам
    raw_id_fields = ['author']
    # Навигация по датам
    date_hierarchy = 'publish'
    # Порядок постов
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
