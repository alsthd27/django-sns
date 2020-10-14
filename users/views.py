from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from posts.models import Post

@login_required
def follow_toggle(request, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)
    is_follower = user.profile in followed_user.profile.followers.all()
    
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
        
    return redirect('home')


def mypage(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    context = {
        'posts' : Post.objects.filter(user=user),
        'followings' : user.profile.followings.all(),
        'followers' : user.profile.followers.all(),
    }
    
    return render(request, 'users/mypage.html', context)