from django.db import models

class Author(models.Model):
    pen_name = models.CharField(max_length=50, null=True)
    full_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    date_created = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True)


    def __str__(self):
        return self.pen_name


class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    photo_book = models.ImageField(upload_to='books/', blank=True)
    release_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(auto_now=True)
    photo_genre = models.ImageField(upload_to='genre_photo/', blank=True)


    def __str__(self):
        return self.title


class Organizer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    terms = models.TextField(blank=True)
    payment = models.PositiveIntegerField(null=True)
    books = models.OneToOneField(Books, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contract for {self.books.author}"


class AuthorContractStatus(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    contract = models.OneToOneField(Contract, on_delete=models.SET_NULL, null=True)
    STATUS = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('D', 'Denied'),
    )
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return f"{self.author}'s Status for Contract {self.contract.books.title}"

