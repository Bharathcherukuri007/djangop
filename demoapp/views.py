from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from .models import Employee

# Create your views here.
def hello(request):
    forms=EmpForm()
    return render(request,"index.html",{'form':forms})
def emp(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():

            form.save()

        else:
            return  HttpResponse("invalid")

    else:
        form = EmpForm()
    return render(request, 'index.html', {'form': form})
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [ ]
        chartLabel = "my data"
        chartdata = []
        emp= Employee.objects.raw('SELECT * FROM employee GROUP BY name')
        for i in emp:
            labels.append(i.name)
            emp1=Employee.objects.filter(name=i.name)

            chartdata.append(emp1.count())

        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)

def coursera(request):

    resp.set_cookie('dj4e_cookie', '3bd80cc7', max_age=1000)

    return HttpResponse("Hello, world. 78573683 is the polls index.")

