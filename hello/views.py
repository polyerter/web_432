from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    context = {
        "phone": "+7-999-999-9999"
    }

    return render(request, "about.html", context=context)


def math(request):
    return render(request, "math.html")


def tasks(request):
    return render(request, "tasks.html")


def disc_page(request):
    return render(request, "index.html")


def calc_discriminant(request):
    if request.method == "POST":
        a = float(request.POST.get("a", 0))
        b = float(request.POST.get("b", 0))
        c = float(request.POST.get("c", 0))
        d = b**2 - 4*a*c

        return HttpResponse(f"<h2>D = {d}</h2><a href='/discriminant/'>Назад</a>")

    return HttpResponse("Ошибка")


def sum_page(request):
    return render(request, "sum.html")


def calc_sum(request):
    if request.method == "POST":
        num1 = float(request.POST.get("num1", 0))
        num2 = float(request.POST.get("num2", 0))
        result = num1 + num2

        return HttpResponse(f"<h2>{num1} + {num2} = {result}</h2><a href='/sum/'>Назад</a>")

    return HttpResponse("Ошибка")

def probability(request):
    return render(request, 'probability.html')


def percent(request):
    return render(request, 'percent.html')