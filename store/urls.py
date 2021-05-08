from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url

    path('about/', views.about, name="about"),
    path('bill/', views.bill, name="bill"),

	path('blog_rightsidebar/', views.blog_rightsidebar, name="blog_rightsidebar"),
    path('blog/', views.blog, name="blog"),
    path('brand_product/', views.brand_product, name="brand_product"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('index/', views.home_default, name="home_default"),
    path('home_search/', views.home_search, name="home_search"),
    path('home_slider/', views.home_slider, name="home_slider"),
    path('home_slider2/', views.home_slider2, name="home_slider2"),
    path('index_icon/', views.index_icon, name="index_icon"),
	path('index/', views.index, name="index"),
    path('order_details/', views.order_details, name="order_details"),
    path('product_detail/', views.product_detail, name="product_detail"),
    path('', views.product_fullwidth, name="product_fullwidth"),
    path('product_leftsidebar/', views.product_leftsidebar, name="product_leftsidebar"),
	path('product_list/', views.product_list, name="product_list"),
    path('profile/', views.profile, name="profile"),
    path('single/', views.single, name="single"),
    path('track_order_single/', views.track_order_single, name="track_order_single"),
	path('track_order/', views.track_order, name="track_order"),
    path('user_dashbord/', views.user_dashbord, name="user_dashbord"),
    path('wishlist/', views.wishlist, name="wishlist"),

    path('update_item/',views.updateItem,name="update_item"),


    path('process_order/',views.processOrder,name="process_order")




]