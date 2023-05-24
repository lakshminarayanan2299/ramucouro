from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'quora1/home.html', {'questions': questions})


@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'quora1/post_question.html', {'form': form})


@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'quora1/answer_question.html', {'form': form, 'question': question})


@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'quora1/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'quora1/register.html', {'form': form})
