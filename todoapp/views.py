from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from todoapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todoapp.models import Todos
from django.contrib import messages
from todoapp.decorators import signin_required
from django.utils.decorators import method_decorator

# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account hasbeen created")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm()
    #     return render(request,"registration.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     # print(request.POST.get("firstname"))
    #     # print(request.POST.get("lastname"))
    #
    #     form=forms.RegistrationForm(request.POST)
    #     if form.is_valid():
    #         #form.save()
    #         User.objects.create_user(**form.cleaned_data)
    #         #print("saved")
    #         messages.success(request,"your account has been created")
    #         return redirect("signin")
    #     else:
    #         messages.error(request,"registration failed")
    #         return render(request,"registration.html",{"form":form})

#@method_decorator(signin_required,name="dispatch")
class LoginView(View):

    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        # print(request.POST.get("username"))
        # print(request.POST.get("password"))
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request, "successfully login")
                print("login success")
                return redirect("index")
            else:
                messages.error(request, "invalid username or password")
                print("invalid credentials")
                return render(request,"login.html",{"form":form})

        return render(request,"login.html")




@method_decorator(signin_required,name="dispatch")

class IndexView(TemplateView):
    template_name = "home.html"
    #to print the uncompleted todos list on home/index page
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["todos"]=Todos.objects.filter(user=self.request.user,status=False)
        return context
    # def get(self, request, *args, **kwargs):
    #     return render(request, "home.html")



class SignOutView(View):

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



@method_decorator(signin_required,name="dispatch")

class TodoAddView(CreateView):
    model=Todos
    form_class=forms.TodoForm
    template_name="add-todo.html"
    success_url=reverse_lazy("todos-list")

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo hasbeen added")
        return super().form_valid(form)


    # def get(self,request,*args,**kwargs):
    #     form=forms.TodoForm()
    #     return render(request,"add-todo.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     form=forms.TodoForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"todo has been added")
    #         return redirect("index")
    #     else:
    #         messages.error(request,"failed")
    #         return render(request,"add-todo.html",{"form":form})



@method_decorator(signin_required,name="dispatch")

class TodoListView(ListView):
    model = Todos
    context_object_name = "todos"
    template_name = "todolist.html"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

    # def get(self,request,*args,**kwargs):
    #     all_todos=Todos.objects.filter(user=request.user)
    #     return render(request,"todolist.html",{"todos":all_todos})


@signin_required
def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    Todos.objects.get(id=id).delete()
    messages.success(request,"deleted")
    return redirect("todos-list")




@method_decorator(signin_required,name="dispatch")

class TodoDetailView(DetailView):
    model=Todos
    context_object_name = "todo"
    template_name = "todo-detail.html"
    pk_url_kwarg = "id"

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     return render(request,"todo-detail.html",{"todo":todo})


@method_decorator(signin_required,name="dispatch")

class TodoEditView(UpdateView):
    model = Todos
    form_class = forms.TodoForm
    template_name = "todo_edit.html"
    success_url = reverse_lazy("todos-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,"todo hasbeen upadated")
        return super().form_valid(form)


    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=forms.TodoChangeForm(instance=todo)
    #     return render(request,"todo_edit.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=forms.TodoChangeForm(request.POST,instance=todo)
    #
    #     if form.is_valid():
    #         form.save()
    #         #msg="Todo has been changed"
    #         messages.success(request,"Todo hasbeen changed")
    #         return redirect("todos-list")
    #     else:
    #         #msg="todo update failed"
    #         messages.error(request,"todo update failed")
    #         return redirect(request,"todo_edit.html",{"form":form})