from django.shortcuts import render
from django.core.paginator import Paginator
from appLcdi.forms import FormTweet
from appLcdi.models import Tweet
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    if request.method == 'POST':
        form = FormTweet(request.POST)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Disimpan"
    else:
        pesan = None
    
    tweets = Tweet.objects.all()
    paginator = Paginator(tweets, 3)
    form = FormTweet()

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'form': form,
        'pesan': pesan
    }
    return render(request, 'dashboard.html', context)
