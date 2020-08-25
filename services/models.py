from django.db import models

# Create your models here.
class ItemCat(models.Model):
    DEFAULT_PK=1
    CatName = models.CharField(max_length=30,blank=True,null=True)
    CatImg = models.ImageField(upload_to ='', null=True)
    def __str__(self):
        return self.CatName

    # This is the database for plants 
class Item(models.Model):
    DEFAULT_PK = 1
    Name = models.CharField(max_length=30)
    ScintificName = models.CharField(max_length=30,blank=True,null=True)
    Description = models.CharField(max_length=1000,blank=True,null=True)
    Height = models.FloatField(max_length=1000,blank=True,null=True)
    Girth = models.FloatField(max_length=1000,blank=True,null=True)
    Category = models.ForeignKey(ItemCat, on_delete=models.PROTECT,default=ItemCat.DEFAULT_PK)
    
    #colorVariantSelected = models.ForeignKey(Colorsvar,on_delete=models.PROTECT,default=Colorsvar.DEFAULT_PK)
    def __str__(self):
        return self.Name

class Variant(models.Model):
    DEFAULT_PK = 1
    # To allow different colors to be chosen by the user
    class Meta:
            verbose_name_plural = 'Variants'

    Variant = models.CharField(max_length = 20)
    VarientStockCount = models.IntegerField(max_length=10)
    VarientItemImage = models.ImageField(upload_to ='', null=True)
    VarientItemPrice = models.FloatField(max_length=30,blank=True,null=True)
    VarientItemName = models.ForeignKey(Item,on_delete=models.PROTECT,default=Item.DEFAULT_PK)
    VarientItemDiscount = models.FloatField(max_length=30,blank=True,null=True)
    def __str__(self):
        return self.Variant


class Offer(models.Model):
    offerName = models.CharField(max_length = 100)
    offerDescription = models.CharField(max_length = 1000)
    offerImage = models.ImageField(upload_to='offerImg')
    offerItemCategory = models.ManyToManyField(ItemCat, blank=True,null=True)
    offerVarient = models.ManyToManyField(Variant,blank=True,null=True)
    offerItem = models.ManyToManyField(Item,blank=True,null=True)
    offerDiscount = models.CharField(max_length=15,blank=True,null=True)
    # offerCategsory = models.ForeignKey(OfferCategory, on_delete=models.PROTECT,default=OfferCategory.DEFAULT_PK)
    showOnCarousel = models.BooleanField(blank=False,null=False,default=False)
    #liv = models.CharField(max_length = 100,blank=False,null=False)



