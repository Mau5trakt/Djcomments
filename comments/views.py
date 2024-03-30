import json

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentPostForm
from .models import Comments
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

def post_comment(request):
    form = CommentPostForm(request.POST) #Way to simplify th next line
    #if request.method == 'POST':
    if request.POST:

        if form.is_valid():
            # Get the form cleaned data
            cd = form.cleaned_data
            # Create a new Comments instance  with the cleaned data

            new_comment = Comments.objects.create(
                username=cd['username'],
                email=cd['email'],
                comment_text=cd['comment_text'],
                timestamp=timezone.now()
            )

            new_comment.save()
            return redirect('index')

    else:
        form = CommentPostForm()

    return render(request, 'comments/addcomment.html', {'form': form})


def show_comments(request):
    comments = Comments.objects.all()

    return render(request, 'comments/allcomments.html', {'comments': comments})

@require_POST
def like_post(request):
    data_from_post = json.load(request)['id']

    data = {
        'id': int(data_from_post),
    }

    print(data['id'])

    """
    comment = Comments.objects.filter(id=data['id'])[0]
    likes = Comments.objects.filter(id=data['id'])[0].likes

    update_likes = Comments.objects.filter(id=data[id])[0]


    print(coment.username)
    print(likes)
    """

    comment = get_object_or_404(Comments, id=data['id'])
    comment.likes += 1
    comment.save()

    likes = Comments.objects.filter(id=data['id'])[0].likes
    post_id = data['id']

    return JsonResponse({'post_id': post_id, 'likes': likes})

