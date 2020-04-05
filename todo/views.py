from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'todo/index.html')

@csrf_exempt
def add_todo(request):
    added_date = timezone.now()
    content = request.POST["content"]
    print(request.POST)
    print(added_date)
    print(content)
    return render(request, 'todo/index.html')