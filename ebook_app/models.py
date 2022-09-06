from django.db import models

class UserRole(models.Model):
    Role = models.CharField(max_length=10)

    class Meta:
        db_table = 'userrole'

    def __str__(self) -> str:
        return self.Role

class Master(models.Model):
    UserRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)
    RegDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)
class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to='profiles/', default='avatar.png')
    FullName = models.CharField(max_length=25, default='', blank=True)
    Gender = models.CharField(max_length=5, choices=gender_choices)
    BirthDate = models.DateField(auto_created=True, default='1991-01-01')
    Mobile = models.CharField(max_length=10, default='', blank=True)
    Country = models.CharField(max_length=25, default='', blank=True)
    State = models.CharField(max_length=25, default='', blank=True)
    City = models.CharField(max_length=25, default='', blank=True)
    Pincode = models.CharField(max_length=6, default='', blank=True)
    Address = models.TextField(max_length=150, default='', blank=True)

    class Meta:
        db_table = 'profile'

    def __str__(self) -> str:
        return self.FullName if len(self.FullName) else 'No Name'
    
class Category(models.Model):
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.Name

class Book(models.Model):
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=16)
    Content = models.TextField(max_length=5000)
    PublishDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'

    def __str__(self) -> str:
        return self.Title

class Chapter(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ChapterName = models.CharField(max_length=100)
    ChapterNumber = models.IntegerField()
    Content = models.FileField(upload_to="book_chapters/")
    UpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chapter'

    def __str__(self) -> str:
        return f"Chapter {self.ChapterNumber}"