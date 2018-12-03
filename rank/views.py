from django.shortcuts import render
from todo.models import Item

# Create your views here.
def get_rank(request):
    results = Item.objects.all()
    return render(request, "rank.html", {
        'items': results
    })