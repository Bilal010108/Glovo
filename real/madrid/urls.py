from .views import *
from rest_framework import routers
from django.urls import path,include



router = routers.SimpleRouter()

router.register(r'courier', CourierListViewSet,  basename='courier'),
router.register(r'cart', CartListViewSet,  basename='cart'),
router.register(r'cart-item', CartItemListViewSet,  basename='cart_item'),
router.register(r'store-review', StoreReviewViewSet,  basename='store-review'),
router.register(r'courier-review', CourierReviewViewSet,  basename='courier-review'),


urlpatterns = [

  path('', include(router.urls)),
  path('user/', UserProfileAPIView.as_view(), name='user'),
  path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user'),
  path('category/', CategoryListAPIView.as_view(), name='category'),
  path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category'),
  path('category_create/', CategoryCreateAPIView.as_view(), name='category_create'),

 path('store/', StoreListAPIView.as_view(), name='store'),
 path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store'),
 path('store_create', StoreCreateAPIView.as_view(), name='store_create'),
 path('store_create/<int:pk>/', StoreEDITAPIview.as_view(), name='store_create'),
 path('store-image/', StoreImageAPIView.as_view(), name='product-image'),

 path('product/', ProductListAPIView.as_view(), name='product'),
 path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product'),
 path('product_create/', ProductCreateAPIView.as_view(), name='product_create'),
 path('product_create/<int:pk>/', ProductEditAPIView.as_view(), name='product_create'),

 path('product-image/', ProductImageListAAPIView.as_view(), name='product-image'),
 path('product-image/<int:pk>/', ProductImageDetailAPIView.as_view(), name='product-image'),

 path('order/', OrderListAPIView.as_view(), name='order'),
 path('order/<int:pk>/', OrderDetailAPIView.as_view(), name='order'),

 path('review/', ReviewDetailAPIView.as_view(), name='review'),
 path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review'),

 path('combo-product/', ComboProductListAPIView.as_view(), name='combo-product'),
 path('combo-product/<int:pk>/', ComboProductDetailAPIView.as_view(), name='combo-product'),
 path('comboproduct_create/', ComboProductCreateAPIView.as_view(), name='comboproduct_create'),
 path('comboproduct_create/<int:pk>/', ComboProductEditAPIView.as_view(), name='comboproduct_create'),

 path('comboproduct_image/', ComboProductImageProductListAPIView.as_view(), name='comboproduct_image'),
 path('comboproduct_image/<int:pk>/', ComboProductImageDetailAPIView.as_view(), name='comboproduct_image'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]