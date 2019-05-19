from django.shortcuts import render


# Create your views here.




def historialnotas(request):
    return render(request, 'comments_history.html', {})
