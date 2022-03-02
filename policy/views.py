from .models import insuranceData
from .forms import updateForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from django.db.models import Q , Count
from django.http import JsonResponse , HttpResponse
from django.contrib import messages


# class homepage(TemplateView):
#     template_name = 'policy/home.html'


def homepage(request):
    template_name = 'policy/home.html'
    regions = insuranceData.objects.order_by().values_list('customer_region', flat=True).distinct()
    return render(request,"policy/home.html",{"regions":regions})


class searchPolicies(ListView):
    model = insuranceData
    template_name = 'policy/searchPolicies.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = insuranceData.objects.filter(
            Q(policy_id=query) | Q(customer_id=query)
        )
        return object_list

def editPolicy(request,id):
    policy=insuranceData.objects.get(policy_id=id)
    return render(request,"policy/updatePolicy.html",{"insuranceData":policy})

def updatePolicy(request,id):
    policy=insuranceData.objects.get(policy_id=id)
    form=updateForm(request.POST, instance=policy)
    # print(form)
    if form.is_valid():
        form.save()
        messages.success(request,"Policy updated successfully")
        return render(request,"policy/updatePolicy.html",{"insuranceData":policy})
  

def policySales(request):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    salesPerMonth = []
    # region='North'
    if request.method == 'GET':  
        region=request.GET.get('region')
        print(region)
        for month in range(13):
            salesPerMonth.append(insuranceData.objects.filter(date_of_purchase__month = month).filter(customer_region = region).aggregate(Count('date_of_purchase'))['date_of_purchase__count'])
    else:
        for month in range(13):
            salesPerMonth.append(insuranceData.objects.filter(date_of_purchase__month = month).filter(customer_region = region).aggregate(Count('date_of_purchase'))['date_of_purchase__count'])
            
    return JsonResponse(data={
        'labels': months,
        'data': salesPerMonth
    })

    