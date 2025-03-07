from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Record
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from .models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['first_name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in')
            return redirect(reverse('home'))
        else:
            messages.warning(request,'Invalid name or password. Please try again')
            return redirect(reverse('home'))
    return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect(reverse('home'))


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit='False')
            user.role='viewer'
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('home'))
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')

    else:
        form = SignUpForm()  # This must be outside the `if request.method == 'POST'` block

    return render(request, 'register.html', {'form': form})  # Always return an HttpResponse

class ListRecords(UserPassesTestMixin,LoginRequiredMixin,ListView):
    model = Record
    template_name = 'records.html'
    context_object_name = 'records'
    login_url=reverse_lazy('home')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Record.objects.filter(first_name__icontains=query) | Record.objects.filter(last_name__icontains=query) | Record.objects.filter(email__icontains=query) | Record.objects.filter(phone__icontains=query) | Record.objects.filter(address__icontains=query) | Record.objects.filter(city__icontains=query) | Record.objects.filter(zip_code__icontains=query)
        return Record.objects.all()
    def test_func(self):
        return self.request.user.role == 'viewer' or self.request.user.role == 'editor' or self.request.role == 'admin'

class GetRecord(UserPassesTestMixin,LoginRequiredMixin,DetailView):
    model = Record
    template_name = 'record.html'
    context_object_name = 'record'
    login_url=reverse_lazy('home')
    def test_func(self):
        return self.request.user.role == 'viewer' or self.request.user.role == 'editor' or self.request.user.role == 'admin'


class DeleteRecord(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Record
    template_name='record.html'
    context_object_name='record'    
    success_url=reverse_lazy('records')
    
    def test_func(self):
        return self.request.user.role == 'editor' or self.request.user.role == 'admin'


class UpdateRecord(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Record
    fields=['first_name','last_name','email','phone','address','city','zip_code']
    
    template_name='update.html'
    context_object_name='record'
    success_url=reverse_lazy('records')

    def test_func(self):
        return self.request.user.role == 'editor' or self.request.user.role == 'admin'


class CreateRecord(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model=Record
    fields=['first_name','last_name','email','phone','address','city','zip_code']
    template_name='create.html'
    success_url=reverse_lazy('records')
    permission_required = 'add_record'
    
    def test_func(self):
        return self.request.user.role == 'editor' or self.request.user.role == 'admin'