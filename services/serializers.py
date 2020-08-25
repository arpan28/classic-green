from rest_framework import serializers
from .models import Item, ItemCat, Offer, Variant

class ItemSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=None, use_url=True)
    Category = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ('id','Name','ScintificName' ,'Category','Description' ,'Height' ,'Girth') 
        lookup_field = 'Category'


class ItemCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCat
        fields = ('id','CatName','CatImg') 
     
class OfferSerializer(serializers.ModelSerializer):
    # offerItemCategory = serializers.StringRelatedField()
    # offerItem = serializers.StringRelatedField()
    class Meta:
        model = Offer
        fields = ('offerName','offerDescription','offerImage', 'offerItemCategory', 'offerItem','offerDiscount','showOnCarousel','offerVarient')

class VariantSerializer(serializers.ModelSerializer):
    VarientItemName = serializers.StringRelatedField()
    VarientItemImage = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Variant
        fields = ('id','Variant','VarientStockCount','VarientItemImage','VarientItemName','VarientItemDiscount','VarientItemPrice')
        lookup_field = 'VarientItemName'

# class QuerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemCat
#         fields = ('id','Variant','VarientStockCount','VarientItemImage','VarientItemName','VarientItemDiscount','VarientItemPrice')
#         lookup_field = 'VarientItemName'
