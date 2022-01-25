from django.conf.urls import url
from . import views

app_name='contacts'
urlpatterns = [
url(r'^$',views.Index.as_view(), name='index'),
url(r'^contacts/$', views.ContactListView.as_view(), name='contacts'),
url(r'^contact/(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='contact-detail'),
]
