from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from demo.models import Todo
from django.contrib.auth.models import User

# SHow index function
def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('index.html',
                              {'todolist':todolist, 'finishtodos':finishtodos},
                              context_instance=RequestContext(request))

# Make this event unfinished
def todorestore(request, id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = 1
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('index.html',
                              {'todolist':todolist, 'finishtodos':finishtodos},
                              context_instance=RequestContext(request))
                                                        
# Add new event big button                                                                                                                                                                                                              
def addtodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        return HttpResponseRedirect('/')
    else:
        return render_to_response('addTodo.html',context_instance=RequestContext(request))

# Finish event: Job done
def todofinish(request, id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == "1":
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('index.html',
                              {'todolist':todolist, 'finishtodos':finishtodos},
                              context_instance=RequestContext(request))

# Delete new event 
def tododelete(request, id=""):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise  Http404
                                                        
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response('index.html',
                              {'todolist':todolist, 'finishtodos':finishtodos},
                              context_instance=RequestContext(request))

# Edit the content of todo event
def updatetodo(request, id=''):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo = Todo.objects.filter(id=id).update(todo=atodo,priority=priority)
        return HttpResponseRedirect('/')
    else:
        mytodo = Todo.objects.get(id=id)
        return render_to_response("addTodo.html",{'todo':mytodo},context_instance=RequestContext(request))