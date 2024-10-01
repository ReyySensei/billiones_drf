from django.contrib import admin
from .models import Book, Author, Category

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

# Register the Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date', 'gender']
    search_fields = ['name']
    list_filter = ['gender']

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'author', 'category', 'created_at']
    search_fields = ['name', 'isbn']
    list_filter = ['author', 'category']
