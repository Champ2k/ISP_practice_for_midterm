from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('display/', views.DisplayView.as_view(), name='display'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('product/', views.ProductView.as_view(), name='product_index'),
    path('product/buy/<int:product_id>', views.buy, name='buy_product'),
    path('<int:pk>/result/', views.CompletedView.as_view(), name='product_result'),
    path('get/', views.get_reply, name='get'),

]