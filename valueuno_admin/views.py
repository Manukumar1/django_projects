from django.shortcuts import render


def admin(request):
    return render(request, 'valueuno_admin/home.html')
