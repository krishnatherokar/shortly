from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortUrl
import random, string

def generate_unique_code(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortUrl.objects.filter(short_code=code).exists():
            return code

def index(request):
    short_url = None
    
    if request.method == 'POST':
        original_url = request.POST['original_url']

        code = generate_unique_code()
        ShortUrl.objects.create(original_url=original_url, short_code=code)

        short_url = request.build_absolute_uri(f'/{code}')
    return render(request, 'index.html', {'short_url': short_url})

def redirectPage(request, code):
    storedObject = get_object_or_404(ShortUrl, short_code=code)
    return redirect(storedObject.original_url)