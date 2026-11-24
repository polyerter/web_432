from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def discriminant(a, b, c): 
    D = b**2 - 4*a*c 
    if D < 0:
        return ("действительных корней нет")  # действительных корней нет
    elif D == 0:
        x = -b / (2*a)
        return (x)
    else:
        sqrt_D = D**0.5
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        return (x1, x2)

def index(request):

    result = discriminant(2, -4, 2)
    print("=" * 50)
    print(result)
    print("=" * 50)

    return JsonResponse(
        {
            "name": "Bob",
        }
    )

def calc(request):
    return render(request, "calc_form.html")

def home(request):
    return render(request, "home.html")
