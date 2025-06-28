from django.shortcuts import get_object_or_404, redirect, render
from .models import CreateTodoModel
from .forms import createTodoForm

def home(request):
    all_todos = CreateTodoModel.objects.all()
    context = {
        "all_todos": all_todos,
    }
    return render(request, "home/home.html", context)


def statusUpdate(request, pk):
    item = CreateTodoModel.objects.get(pk=pk)
    item.isCompleted = not item.isCompleted
    item.save()
    return redirect("home")


def deleteTodo(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(CreateTodoModel,pk=pk)
        todo.delete()
    return redirect("home")


def create_todo(request):
    form = createTodoForm()
    if request.method == "POST":
        form = createTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = createTodoForm()
    return render (request, "home/createtodo.html", {"form": form})
        
def update_todo(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(CreateTodoModel, pk = pk)
    pass