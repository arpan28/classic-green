#gg = shopDetails.objects.__getitem__("date")
    #print(gg)
    #tt = queryset.update({})
    
    def dispatch(self,request,*args, **kwargs):
            latestDate = datetime.datetime.now()
            latestDate = latestDate.strftime("%Y-%m-%d") 
            #serializer = shopSerializer(self.queryset, many=True)
            if request.method == 'GET':
                #snippets = shopDetails.objects.all()
                serializer = shopSerializer(self.queryset, many=True)
                return JsonResponse(serializer.data, safe=False)

            if request.method == 'POST':
                serializer = shopSerializer(self.queryset, many=True)
                latestDate = datetime.datetime.now()
                latestDate = latestDate.strftime("%Y-%m-%d")               
                data = JSONParser().parse(request)
                
                data["date"] = latestDate
                serializer = shopSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            elif request.method == 'PUT':
                data = JSONParser().parse(request)
                data["date"] = latestDate
                serializer = shopSerializer(self.queryset, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=400)

            elif request.method == 'DELETE':
                shopDetails.delete()
                return HttpResponse(status=204)      