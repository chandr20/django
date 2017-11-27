from django.conf.urls import url

from .views import (
    # restaurant_listview,
    RestaurantListview,
    RestaurantDetailedView,
    RestaurantCreateView,
    RestaurantUpdateView)


urlpatterns = [
    url(r'^$', RestaurantListview.as_view(),name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(),name='create'),
    # url(r'^(?P<slug>[\w-]+)/edit$',RestaurantUpdateView.as_view(),name='edit'),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantUpdateView.as_view(),name='detail'),
   ]