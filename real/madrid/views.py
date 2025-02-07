from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics, status, permissions
from .serializers import *
from .models import *
from .filters import CategoryFilter,ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

from .permissioms import CheckOrderingClient,CheckCourier


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class =UserProfileSerializers




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers




class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category .objects.all()
    serializer_class = CategorySerializers



class CategoryEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['store_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]







class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StoreCreateAPIView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class =StoreSerializers



class StoreEDITAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers



class StoreImageAPIView(generics.RetrieveAPIView):
    queryset = StoreImage.objects.all()
    serializer_class = StoreImageSerializers


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['price']


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers




class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



class ProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class  ProductImageListAAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers



class ProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers


class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [CheckOrderingClient,]


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated, CheckCourier]





class ReviewListAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers



class ComboProductListAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductCreateAPIView(generics.ListCreateAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = CategorySerializers



class ComboProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = CategorySerializers


class ComboProductImageProductListAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CourierListViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class =CourierSerializers


class CourierDetailViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class =CourierSerializers


class CartListViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializers

    def get_queryset(self):
        return Cart.objects.filter(client_cart=self.request.user)


class CartDetailViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializers

    def get_queryset(self):
        return Cart.objects.filter(client_cart=self.request.user)



class CartItemListViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializers


class CartItemDetailViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializers





class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer



class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializer
