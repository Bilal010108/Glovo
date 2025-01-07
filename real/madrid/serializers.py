from .models import *
from rest_framework import serializers


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number','user_role','age']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['category_name']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','description','price','quantity','store']


class CategoryDetailSerializers(serializers.ModelSerializer):
    category_product = ProductSerializers(many=True,read_only=True)

    class Meta:
        model = Category
        fields =['category_name', 'category_product']




class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product','product_image']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client','products','status_order','delivery_address','courier','created_at']


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields =['user','status_courier','current_orders']



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =['client_review','store_review','rating','comment','created_at']



class ComboProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComboProduct
        fields =['combo_name','combo_description','combo_price','combo_quantity','store']



class ComboImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComboImage
        fields =['combo','combo_image']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =['client_cart']

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE, )
        fields =['cart','product_cart','quantity_cart']

class StoreReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')


    class Meta:
        model = StoreReview
        fields = ['client', 'rating', 'comment', 'created_date']


class CourierReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierReview
        fields = ['client', 'rating', 'comment_courier', 'created_date']





class StoreImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreImage
        fields = ['store','store_image']


class StoreSerializers(serializers.ModelSerializer):
    store_category = CategorySerializers(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    total_good = serializers.SerializerMethodField()
    storr_images = StoreImageSerializers(read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['store_name','store_description','contact_info','address','owner','storr_images','total_good',
                  'store_category','contact_info','avg_rating','total_people']

    def get_avg_rating(self, obj):
       return obj.get_avg_rating()

    def get_total_people(self, obj):
       return obj.get_total_people()

    def get_total_good(self, obj):
       return obj.get_total_good()

class StoreDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    owner = UserProfileSerializers(read_only=True, )
    products = ProductSerializers(read_only=True, many=True)
    combo_products = ComboProductSerializers(read_only=True, many=True)
    store_review = StoreReviewSerializer(read_only=True, many=True)

    class Meta:
        model =Store
        fields =['store_name','store_description','contact_info','address','owner']
