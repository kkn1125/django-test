from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .forms import BoardForm
from .models import Board
from django.core.paginator import Paginator

# Create your views here.
@api_view(['GET'])
def post_list(request):
    page = request.GET.get('page', '1')
    
    board = Board.objects.order_by('regdate')
    
    paginator = Paginator(board, 3)
    page_obj = paginator.get_page(page)
    
    context = {
        'board': page_obj
    }
    
    return render(request, 'blog/post_list.html', context)

@api_view(['GET', 'POST'])
def post_control(request, num):
    if request.method == 'GET':
        board = Board.objects.get(num=num)
        context = {
            'board': board
        }
        return render(request, 'blog/post_detail.html', context)
    
    elif request.method == 'POST':
        return redirect('post_list')

@api_view(['GET', 'POST'])
def post_form(request):
    if request.method == 'GET':
        context = {
            'boardForm': BoardForm
        }
        return render(request, 'blog/post_form.html', context)
    
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        
        board = Board(
                title=title,
                content=content,
                author=author,
            )
        
        board.save()
        
        return redirect('post_list')
