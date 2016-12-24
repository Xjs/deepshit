from django.http import HttpResponse

def index(request):
    return HttpResponse("Dies ist ein Blog from hell.")

# Create your views here.
