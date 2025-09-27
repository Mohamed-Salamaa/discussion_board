from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from .forms import NewTopicForm
from django.contrib.auth.models import User


def home(request):
    context = {}
    boards = Board.objects.all()
    context["boards"] = boards
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def board_topics(request, board_id):
    context = {"board": Board.objects.get(pk=board_id)}
    return render(request, 'topics.html', context)


def new_topic(request, board_id):
    form = NewTopicForm()
    board = Board.objects.get(pk=board_id)
    user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()

            Post.objects.create(
                message=form.cleaned_data.get("message"),
                created_by=user,
                topic=topic
            )
            return redirect('board_topics', board_id=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {"board": board, 'form': form})
