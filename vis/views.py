from django.shortcuts import render

# Create your views here.
def get_vis(request):
    return render(request, "visualisations.html")
