from django.contrib import admin

# Register your models here.
from .models import * 
from .forms import *
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display= ["id","Name","StartYear","EndYear","Ratings","Updated_at","Created_at"] #Author._meta.get_all_field_names()
	form=AddAuthorForm
	class Meta:
		model = Author

class PublisherAdmin(admin.ModelAdmin):
	list_display=["id","Name","Publication","Address","email","Phone","Updated_at","Created_at"]# Publisher._meta.get_all_field_names()#["id","Name","Ratings","Updated_at","Created_at"]
	form=PublisherForm
	class Meta:
		model = Publisher

class BookAdmin(admin.ModelAdmin):
	list_display= ["id","Title","Publisher","Updated_at","Created_at"]
	# form=AddAuthorForm
	class Meta:
		model = Book
class BookAuthorAdmin(admin.ModelAdmin):
	list_display= ["id","Author_id","Book_id"]#BookAuthor._meta.get_all_field_names()#["id","Name","Ratings","Updated_at","Created_at"]
	class Meta:
		model = BookAuthor

class BookAuthorAdmin(admin.ModelAdmin):
	list_display=["id","Book","Author","Updated_at","Created_at"]
	class Meta:
		model = BookAuthor

class CategoryAdmin(admin.ModelAdmin):
	list_display=["id","Name","Updated_at","Created_at"]
	form=CategoryForm
	class Meta:
		model = Category

class BookCategoryAdmin(admin.ModelAdmin):
	list_display=["id","Category","Book","Updated_at","Created_at"]
	class Meta:
		model = BookCategory

class AdminAdmin(admin.ModelAdmin):
	list_display=["id","User","Address","Phone","Updated_at","Created_at"]
	form=AdminForm
	class Meta:
		model = Admin


class SellerAdmin(admin.ModelAdmin):
	list_display=["id","User","PriPhone","SecPhone","LandMark","City","State","Country","PinCode","AddressLine","ProfileImg","Remark","AdharNo",
	"VerificationStatus","AdminVerified","AdminBlocked","BlockStatus","Ratings","Updated_at","Created_at"]
	form=SellerForm
	class Meta:
		model = Seller

class BookEditionAdmin(admin.ModelAdmin):
	list_display=["id","Book","Edition","YearOfPublication","Price","CoverImage","PageCount","Discount","AvailableNoOfCopies","Seller","Updated_at","Created_at"]
	form=BookEditionForm
	class Meta:
		model=BookEdition

class CustomerAdmin(admin.ModelAdmin):
	list_display=["id","user","PriPhone","SecPhone","LandMark","City","State","Country","PinCode","AddressLine","ProfileImg","Updated_at","Created_at"]
	form=CustomerForm
	class Meta:
		model = Customer


class NotificationAdmin(admin.ModelAdmin):
	list_display=["id","Content","CustomerReadStatus","SellerReadStatus","AdminReadStatus","Customer_id","Seller_id","Admin_id","Created_at"]
	class Meta:
		model = Notification

class OrderAdmin(admin.ModelAdmin):
	list_display=["id","DateOfPurchase","DateOfShipment","DateOfDelivary","Tag","Book","Customer",	"Updated_at","Created_at"]
	# form=AdminForm
	class Meta:
		model = Order
class KartAdmin(admin.ModelAdmin):
	list_display=["id","Book","Customer","Updated_at","Created_at"]
	# form=AdminForm
	class Meta:
		model = Kart		
class ReviewAdmin(admin.ModelAdmin):
	list_display=["id","Content","Ratings","Book","Customer","Updated_at","Created_at"]
	# form=ReviewForm
	class Meta:
		model =Review

admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookAuthor,BookAuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(BookCategory,BookCategoryAdmin)

admin.site.register(Admin,AdminAdmin)


admin.site.register(Seller,SellerAdmin)
admin.site.register(BookEdition,BookEditionAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Kart,KartAdmin)

