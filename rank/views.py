from django.shortcuts import render

# Create your views here.
def get_rank(request):
    return render(request, "rank.html")