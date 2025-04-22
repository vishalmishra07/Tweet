from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import Tweetform, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Home page
def index(request):
    return render(request, 'index.html')

# Tweet listing
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# Create a new tweet
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES)  
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetform()
    return render(request, 'tweet_forms.html', {'form': form})

# Edit an existing tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetform(instance=tweet)  # ← this is the fix
    return render(request, 'tweet_forms.html', {'form': form})
# Delete tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

