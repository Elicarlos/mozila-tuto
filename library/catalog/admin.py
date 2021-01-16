from django.contrib import admin
from . models import Book, Author, Genre, BookInstance, Language




class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
  


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class GenreAdmin(admin.ModelAdmin):
    pass

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    ) 

class LanguageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language, LanguageAdmin)