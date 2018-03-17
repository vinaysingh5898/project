from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.utils import timezone
from datetime import datetime

# Create your models here.

class Author(models.Model):
	Ratings=models.IntegerField(default=0)
	StartYear=models.PositiveIntegerField(blank=False,
		validators=[
		MinValueValidator(1000),
		MaxValueValidator(datetime.now().year)],
		help_text="Use the following format: <YYYY>")
	EndYear=models.PositiveIntegerField(blank=True,null=True,
		validators=[
		MinValueValidator(1000),
		MaxValueValidator(datetime.now().year)],
		help_text="Use the following format: <YYYY>")
	Name=models.CharField(max_length=120)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__ (self): #	python 3.3 is __str__
		return self.Name

class Publisher(models.Model):
	Name=models.CharField(max_length=120,blank=True,null=True)
	Publication=models.CharField(max_length=120,blank=True,null=True)
	Address=models.TextField(max_length=500,blank=True,null=True)
	email=models.EmailField()
	Phone=models.DecimalField(max_digits=10, decimal_places=False,blank=True,null=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__ (self): #	python 3.3 is __str__
		return self.Name

class Book(models.Model):
	Title=models.CharField(max_length=120,blank=True,null=True)
	Publisher=models.ForeignKey(Publisher)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__ (self): #	python 3.3 is __str__
		return self.Title


class BookAuthor(models.Model):
	Author=models.ForeignKey(Author)
	Book=models.ForeignKey(Book)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return str(self.Book)

class Category(models.Model):
	Name=models.CharField(max_length=120,blank=False,null=False)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.Name

class BookCategory(models.Model):
	Category=models.ForeignKey(Category,default=0, related_name='Category_id')
	Book=models.ForeignKey(Book,default=0, blank=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return str(self.Book)

class Admin(models.Model):
	User=models.OneToOneField(User)
	Address=models.TextField(max_length=500,blank=True,null=True)
	Phone=models.DecimalField(max_digits=10, decimal_places=False,blank=True,null=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.User.username

class Seller(models.Model):
	User=models.ForeignKey(User)
	PriPhone=models.DecimalField(max_digits=10, decimal_places=False,blank=False)
	SecPhone=models.DecimalField(max_digits=10, decimal_places=False,blank=True,null=True)
	VerificationStatus=models.IntegerField(default=0)
	
	AdminBlocked=models.ForeignKey(Admin, blank=True,null=True, related_name='AdminBlocked_id')
	AdminVerified=models.ForeignKey(Admin,blank=True,null=True, related_name='AdminVerified_id')
	
	BlockStatus=models.IntegerField(default=0)
	Ratings=models.IntegerField(default=0)
	LandMark=models.CharField(max_length=500,blank=True,null=True)
	City=models.CharField(max_length=500, default='')
	State=models.CharField(max_length=500, default='')
	Country=models.CharField(max_length=500,default='')
	PinCode=models.DecimalField(max_digits=6, decimal_places=False,blank=False)
	AddressLine=models.CharField(max_length=500,blank=True,null=True)
	ProfileImg=models.ImageField(upload_to = 'img/SellerPic/', default = 'img/SellerPic/no-img.jpg')
	Remark=models.CharField(max_length=500,blank=True,null=True)
	AdharNo=models.DecimalField(max_digits=12, decimal_places=False,blank=True,null=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.User.username

class BookEdition(models.Model):
	Book=models.ForeignKey(Book)
	Edition=models.CharField(max_length=20,default='1')
	YearOfPublication=models.PositiveIntegerField(
		validators=[
		MinValueValidator(1000), 
		MaxValueValidator(datetime.now().year)],
		help_text="Use the following format: <YYYY>")
	Price=models.IntegerField(default=0)
	CoverImage=models.ImageField(upload_to = 'img/BookCvr/', default = 'img/BookCvr/no-img.jpg')
	PageCount=models.IntegerField(default=0)
	Discount=models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],help_text="Discount should be between 0% to 100%")
	AvailableNoOfCopies=models.PositiveIntegerField(validators=[MinValueValidator(0)])
	Seller=models.ForeignKey(Seller)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return str(self.Book.Title)


class Customer(models.Model):
	user=models.ForeignKey(User)
	PriPhone=models.DecimalField(max_digits=10, decimal_places=False,blank=False)
	SecPhone=models.DecimalField(max_digits=10, decimal_places=False,blank=True,null=True)
	LandMark=models.CharField(max_length=500,blank=True,null=True)
	City=models.CharField(max_length=500, default='')
	State=models.CharField(max_length=500, default='')
	Country=models.CharField(max_length=500,default='')
	PinCode=models.DecimalField(max_digits=6, decimal_places=False,blank=False)
	AddressLine=models.CharField(max_length=500,blank=True,null=True)
	ProfileImg=models.ImageField(upload_to = 'img/Customer/', default = 'img/CustomerPic/no-img.jpg')
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.user.username

class Notification(models.Model):
	Content=models.TextField(max_length=500, default='')
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	CustomerReadStatus=models.NullBooleanField()
	SellerReadStatus=models.NullBooleanField()
	AdminReadStatus=models.NullBooleanField()
	Customer_id=models.IntegerField(default=0)
	Seller_id=models.IntegerField(default=0)
	Admin_id=models.IntegerField(default=0)
	def __str__(self):
		return self.Content

class Order(models.Model):
	DateOfPurchase=models.DateTimeField(auto_now_add=True,auto_now=False)
	DateOfShipment=models.DateTimeField(blank=True)
	DateOfDelivary=models.DateTimeField(blank=True)
	Tag=models.CharField(max_length=500,blank=True,null=True)
	Book=models.ForeignKey(BookEdition)
	Customer=models.ForeignKey(Customer)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return str(self.Book)

class Review(models.Model):
	Content=models.TextField(max_length=500,blank=True,null=True)
	Ratings=models.IntegerField(default=0)
	Book=models.ForeignKey(BookEdition)
	Customer=models.ForeignKey(Customer)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.Content		
class Kart(models.Model):
	Book=models.ForeignKey(BookEdition)
	Customer=models.ForeignKey(Customer)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return str(self.Book)