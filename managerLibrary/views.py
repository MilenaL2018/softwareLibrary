from django.shortcuts import render, redirect
from .forms import CommentForm

# Create your views here.




def historialnotas(request):
    if request.method == 'POST':
        print(request.POST)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.save()
            return redirect()