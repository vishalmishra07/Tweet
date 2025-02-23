from django.shortcuts import render
from .models import Tweet
from .forms import Tweetform
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})
def tweet_create(request):
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES)
    else:
        form = Tweetform()
    return render(request,'tweet_form.html',{'form':form})
        