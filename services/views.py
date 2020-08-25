from django.shortcuts import render,redirect, get_object_or_404
from rest_framework import viewsets ,generics        # add this
from .serializers import ItemSerializer, ItemCatSerializer,  VariantSerializer,OfferSerializer    # add this
from .models import Item, ItemCat, Offer, Variant     
from django.http import HttpResponse          # add this
from .forms import loginForm
from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend


class item_view(viewsets.ModelViewSet):       # add this
    serializer_class = ItemSerializer          # add this
    queryset = Item.objects.all()              # add this


class itemcat_view(viewsets.ModelViewSet):      # add this
    serializer_class = ItemCatSerializer          # add this
    queryset = ItemCat.objects.all()  
# *******************************************************/variant?
    # def test(self, **kwargs):
    #     # user = User.objects.get(id=kwargs['user_id'])
    #     queryset = ItemCat.objects.get(Category = kwargs['itemCategory'])  
        
# *********************************************************************


class OfferView(viewsets.ModelViewSet):      # add this
    serializer_class = OfferSerializer          # add this
    queryset = Offer.objects.all()   

class variant_view(viewsets.ModelViewSet):      # add this
    serializer_class = VariantSerializer          # add this
    queryset = Variant.objects.all()  


    # def index(self,request):
    #     if request.method == 'POST':
    #         form = loginForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('https://localhost:3000')
    #         return render(request, 'services/loginForm.html', {'form': form})
                    
        
    #     else:
    #         form = loginForm()
    #         context = {
    #             'form':form
    #         }
    #         return render(request,'services/loginForm.html',context)

def get_foreign_keys(self):
        foreign_keys = []
        for field in self._meta.fields:
            if isinstance(self._meta.get_field_by_name(field.name)[0], models.ForeignKey):
                foreign_keys.append(field.name)

# This is basically a Item query class , which will get us filtered Item data from based on a ItemCat
class ItemCatQueryView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Category__CatName',)
    #def get_queryset(self, *args, **kwargs):        
        # item = self.request.query_params.get('dataDict','')
        # item = eval(item)
        # print(item)
        # dictMap = {"Item":ItemSerializer,"ItemCat":ItemCatSerializer,"Offer":OfferSerializer,"Variant":VariantSerializer}
        # dbDict ={"Item":Item,"ItemCat":ItemCat}
        # querySet = dbDict[item["db"]].objects.all()
        # if item:        
        #     aaa = item["key"]
        #     print(aaa)
        #     print(str(querySet.filter(**{aaa: item["query"]})))
        #     return querySet.filter(**{aaa: item["query"]})
        #     # return "Hi"

        # return querySet

        ######################################################


# This is basically a variant query class , which will get us filtered "Variant" data from based on a Item
class variantQueryView(generics.ListAPIView):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('VarientItemName__Name',)
  