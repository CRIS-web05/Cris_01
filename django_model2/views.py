from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola MI MUNDO ES SIOMEY (no es copia XD) <3")

def mostrar_nombre(request):
    return HttpResponse(" Christofher Andre Chicaiza Nuñez ") 
def home_page(request):  
    return HttpResponse("¡welcome homework:3!")