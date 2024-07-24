from django.shortcuts import render

# Create your views here.
def login_page(request):
    pass

def sign_up(request):
    pass

def overview_msg(request):
    return render(request, 'view_pages/overview_msg.html')

def grp(request):
    return render(request, 'view_pages/grp.html')

def theme(request):
    return render(request, 'view_pages/theme.html')