from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

def home(request):

    records = Record.objects.all()
   
    # Check if the user is authenticated
    if request.method =="POST":
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password. Please try again.')
            return redirect('home')
    return render(request, 'home.html', {'records': records})
 

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        
        return render(request, 'website/record.html',{'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In To View That Page...')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You Must Log In To Do That...')
        return redirect('home')

    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added ...")
                return redirect('home')

        return render(request, 'website/add_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be Log In ...")
        return redirect('home')



def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated !")
            return redirect('home')
        return render(request, 'website/update_record.html',{'form':form})
    
    else:
        messages.success(request, "You Must Be Log In ...")
        return redirect('home')



