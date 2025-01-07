from .models import Product,Store
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_description',)