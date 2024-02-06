from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from django.contrib import messages



def signup_view(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Your account has been created successfully.')
                return redirect('accounts:login')
        else:
            form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
    except Exception as e:
        messages.error(request, f'Something went wrong: {e}')
        return redirect('accounts:signup')
    

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        try:
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('articles:list')
            else:
                raise Exception("Invalid form data.")
        except Exception as e:
            messages.error(request, str(e))
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
        # return redirect('articles:list')





# def signup_view(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             # log user in
#             return redirect('articles:list')
#     else:
#         form = UserCreationForm()
#     return render(request,'accounts/signup.html',{'form':form})


# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             try:
#                 user = form.save()
#                 login(request, user)
#                 return redirect('accounts:login')
#             # log user in
#             except Exception as e:
#                 return redirect('accounts:signup')
#             # return redirect('articles:list')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})


# def login_view(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('articles:list')

#     else:
#         form = AuthenticationForm()
#     return render(request,'accounts/login.html',{'form':form})
