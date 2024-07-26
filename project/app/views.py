from django.shortcuts import render,redirect
from .models import CustomeUser,transaction
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth
# Create your views here.


def index(request):
    return render(request,'index.html')




def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        if CustomeUser.objects.filter(Phonenumber = phone).exists():
            return render(request,'registration.html',{'message':'phone number already exists'})
        address = request.POST['address']
        dob =request.POST['dob']
        initial_amount = request.POST['initial_amount']
        account_number = request.POST['account_number']
        if CustomeUser.objects.filter(Accountnumber = account_number).exists():
            return render(request,'registration.html',{'message':'account number already exists'})
        image = request.FILES['image']
        username = request.POST['username']
        password = request.POST['password']
        data = CustomeUser.objects.create_user(first_name = name,
                                               Age = age,
                                               email = email,
                                               Phonenumber = phone,
                                               Address = address,
                                               DOB = dob,
                                               Initialamount = initial_amount,
                                               Accountnumber = account_number,
                                               Image = image,
                                               username=username,
                                               password = password,
                                               usertype = 'user')
        data.save()
        return redirect(Login)
    else:
        return render(request,'registration.html')
    

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
         # Authenticate superusers (admins)
         
         
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request, admin_user)
            return redirect('admin:index')
        
        
        elif user is not None:
            
            login(request, user)
            if user.usertype == "user":     
                return redirect(userhome)
            elif user.usertype == "bank":  
                return redirect(bankhome)
            return render(request, 'login.html', context)
        else:
            context = {
                'message': "Invalid credentials"
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect(Login)




def userhome(request):
    user = CustomeUser.objects.get(id = request.user.id)
    return render(request,'userhome.html',{'data':user})



def userprofile(request):
    user = CustomeUser.objects.get(id=request.user.id)
    return render(request,'userprofile.html',{'data':user})


def useredit(request,id):
    user=CustomeUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.first_name=request.POST['Name']
        user.Age=request.POST['Age']
        user.Phonenumber=request.POST['Phonenumber']
        user.DOB=request.POST['DOB']
        user.Address=request.POST['Address']
        user.email=request.POST['Email']  
        user.username=request.POST['UserName']
        if 'Image' in request.FILES:
            user.Image = request.FILES['Image']
        user.save()
        return redirect(userprofile)
    else:
        return render(request,'userprofileedit.html',{'data':user})
    

def deposite(request):
    user = CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':
        amount =  int(request.POST['amount'])
        if amount<100:
            return render(request,'userdeposite.html',{'error':'amount required more than 100','data':user})
        else:
            user.Initialamount+=int(amount)
            user.save()
            a = transaction.objects.create(user_id=user,details='Deposit', amount=amount,balance=user.Initialamount)
            a.save()
            return render(request,'userdeposite.html',{'Deposited':'Amount Deposited','data':user})
    else:
        return render(request,'userdeposite.html',{'data':user})




def withdraw(request):
    data=CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':

        amount = int(request.POST.get('amount')) 
      
        if data.Initialamount <= amount or data.Initialamount-amount<1000:
            return render(request,'userwithdraw.html ',{'context':'insufficient balance','data':data})
        if amount < 100:
                return render(request,'userwithdraw.html ',{'error':"Can't withdraw money,minimum  100rs amount required",'data':data})
        
        else:
            data.Initialamount-=amount
            data.save()
            a=transaction.objects.create(user_id=data,details='Withdrawel',amount=amount,balance=data.Initialamount)
            a.save()
            return render(request,'userwithdraw.html ',{'Withdrawel':'Amount Withdrawed','data':data})
    else:
        return render(request,'userwithdraw.html',{'data':data})
    

def userhistory(request):
    data = transaction.objects.filter(user_id = request.user.id)
    return render(request,'userhistory.html',{'data':data})


# ..........................

def bankhome(request):
    user = CustomeUser.objects.get(id = request.user.id)
    return render(request,'bankhome.html',{'data':user})


def bankprofileedit(request):
    user = CustomeUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.first_name=request.POST['name']
        user.Ifsc=request.POST['ifsc']
        user.Address=request.POST['address']
        user.Branch=request.POST['branch']
        user.Pincode=request.POST['pincode']
        if 'Image' in request.FILES:
            user.Image = request.FILES['Image']
        user.save()
        return redirect(bankhome)
    else:
        return render(request,'bankprofileedit.html',{'data':user})
    


def viewusers(request):
    data = CustomeUser.objects.filter(usertype='user')
    return render(request,'banknviewuser.html',{'data':data})

def viewuserdetails(request,id):
    data = CustomeUser.objects.get(id=id)
    return render(request,'bankviewuserdetails.html',{'data':data})
    
def bankuserhistory(request,id):
    data = transaction.objects.filter(user_id=id)
    return render(request,'bankuserhistory.html',{'data':data})