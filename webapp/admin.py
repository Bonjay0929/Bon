from django.contrib import admin
from .models import Author, Books, Genre, Organizer, Contract, AuthorContractStatus

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Organizer)
admin.site.register(Contract)
admin.site.register(AuthorContractStatus)