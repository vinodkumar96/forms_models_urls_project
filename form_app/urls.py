from django.conf.urls import url
from . import views
app_name="Form_app"
urlpatterns = [
    url(r'^$',views.get_name)
]