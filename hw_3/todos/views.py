from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodoForm

def index_page(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        todos = Todo.objects.all()
        return render(request, 'todos/todo_list.html', {'todos': todos, 'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_page')

def todo_details(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todos/todo_details.html', {'todo': todo})

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('index_page')
    except Todo.DoesNotExist:
        todos = Todo.objects.all()
        form = CreateTodoForm()
        return render(request, 'todos/todo_list.html', {
            'todos': todos,
            'form': form,
            'error': 'Could not delete todo since it does not exist'
        })