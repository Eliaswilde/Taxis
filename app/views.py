from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mezzanine.pages.views import page

# Create your views here.
@login_required()
def regional_interstate(request):
    return render(request, 'pages/regional_interstate.html')