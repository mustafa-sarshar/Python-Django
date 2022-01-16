from django.shortcuts import render

def home_page(request):
    return render(request, template_name="main/index.html")

def about_page(request):
    return render(request, template_name="main/about.html")

def results_page(request):
    name = request.GET["name"]
    birthdate = request.GET["birthdate"]
    print(name, birthdate)
    return render(request, template_name="main/results.html", context={"name": name, "birthdate": birthdate})