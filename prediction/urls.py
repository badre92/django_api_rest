

from django.conf.urls   import url
from prediction         import views

urlpatterns = [
    url(r'^predict/$'              , views.predict),
    url(r'^houses/$'               , views.house_list  ),
    url(r'^house/(?P<pk>[0-9]+)/$' , views.house_detail),
]