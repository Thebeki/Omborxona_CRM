from django.urls import path
from .views import *

urlpatterns = [
    path("", BolimlarView.as_view(), name='bolim'),
    path("mahsulotlar/", MahsulotView.as_view(), name='mahsulotlar'),
    path("mahsulotlar/<int:son>/", MahsulotEditView.as_view(), name='product-update'),
    path("clientlar/", ClientView.as_view(), name='clientlar'),
    path("clientlar//<int:son>/", ClientEditView.as_view(), name='client-update'),
]


