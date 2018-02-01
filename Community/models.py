from django.db import models

# Create your models here.
class Apartment(models.Model):
    Apt_Name = models.CharField(max_length=200)
    Apt_Address = models.CharField(max_length=200)


class Category(models.Model):
    Username = models.ForeignKey('auth.User')
    Apartment_Name = models.ForeignKey('Apartment')
    Board_Kind = models.ForeignKey('Category')

class Image(models.Model):
    Picture = models.ImageField(upload_to='pictures/%Y/%m/%d')

# 4 Main Boards
class Selling(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)

class Rent(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)

class Community(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)

class Apartment_info(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)

# 4 Comments
class Selling_Comment(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)


class Rent_Comment(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)


class Community_Comment(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)


class Apartment_info_Comment(models.Model):
    Category = models.ForeignKey('Category')
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Image = models.ForeignKey('Image', null=True)
