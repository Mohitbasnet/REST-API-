from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page response")
    friends = [
        'mohit',
        'rohit',
        'skgk'
    ]
    return JsonResponse(friends,safe = False)