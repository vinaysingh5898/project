from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'mainApp.views.home', name='home'),
    url(r'^add-author$', 'mainApp.views.addAuthor', name='add-author'),
    # url(r'^add-item/$', 'newsletter.views.addItem', name='add-item'),
    url(r'^delete-author/(?P<id>\w{1,50})$', 'mainApp.views.deleteAuthor', name='delete-author/id'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^customer-login/','mainApp.views.customerLoginView',name='customer-login'), 
    url(r'^customer-register/','mainApp.views.customerRegisterView',name='customer-register'), 
    url(r'^seller-login/','mainApp.views.sellerLoginView',name='seller-login'), 
    url(r'^seller-register/','mainApp.views.sellerRegisterView',name='seller-register'), 
    url(r'^admin-login/','mainApp.views.adminLoginView',name='admin-login'), 
    url(r'^admin-register/','mainApp.views.adminRegisterView',name='admin-register'),
    url(r'^get-books-by-category/(?P<id>\d+)$', 'mainApp.views.getBooksByCategory', name='get_books_by_category'), 
    url(r'^get-single-book/(?P<id>\d+)$', 'mainApp.views.getSingleBook', name='get_single_book'), 
    url(r'^post-review/','mainApp.views.postReview',name='post-review'), 

    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
