from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial
    path('chars/<int:page_num>',views.chars1,name='chars1'),
    path('char_unico/<str:id>', views.one_char,name='one_char')
]
