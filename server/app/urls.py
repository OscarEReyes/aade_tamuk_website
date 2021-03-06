from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^partners/', views.Partners.as_view(), name= 'partners'),
	url(r'^about_us/', views.AboutUs.as_view(), name= 'about_us'),
	url(r'^donate/', views.Donations.as_view(), name= 'donate'),
	url(r'^leadership/', views.Leadership.as_view(), name= 'leadership'),
	url(r'^contact_us/', views.contact_us, name= 'contact_us'),
	url(r'^join_us/', views.join_us, name= 'join_us'),
	url(r'^calendar/', views.Calendar.as_view(), name= 'calendar'),
	url(r'^gallery/meetings/?', views.MeetingsGallery.as_view(), name= 'meetings'),
	url(r'^gallery/field_trips/?', views.FieldTripGallery.as_view(), name= 'field_trips'),
	url(r'^gallery/training/?', views.TrainingGallery.as_view(), name= 'taining'),
	url(r'^gallery/social/?', views.SocialGallery.as_view(), name= 'social'),
	url(r'^gallery/pictures/', views.Album.as_view(), name= 'album'),
	url(r'^news/', views.News.as_view(), name= 'news'),
	url(r'^news/(?P<selected>\d+)/', views.News.as_view(), name= 'newspost'),
	url(r'^$', views.Home.as_view(), name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
