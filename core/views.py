from django.shortcuts import render,redirect,HttpResponse
from .models import Tribe,Village,TribalMember,TribeUser,MangementRoles,MangementUser
from django.contrib.auth import get_user_model
from .ml_utils import predict_sentiment
User=get_user_model()
# Create your views here.
# from .models import TribeUser, TribalMember

# def tribe_member_context(request):
#     tribeMember = None
#     user_id = request.session.get('user_id')
#     if user_id:
#         try:
#             user = TribeUser.objects.get(id=user_id)
#             tribeMember = TribalMember.objects.get(phno=user.phno)
#         except (TribeUser.DoesNotExist, TribalMember.DoesNotExist):
#             pass
#     return {'tribeMember': tribeMember}

def tribe(request):
    if request.method=='POST':
        tribe_name=request.POST.get('tribe')
        if tribe_name:
            MangementRoles.objects.create(role=tribe_name)
            return HttpResponse('<p>created</p>')
        else:
            return HttpResponse('<p>Tribe name is required</p>', status=400)
        
    elif  request.method=='GET':
        return render(request, 'tribe.html')
def signup(request):
    if request.method=="POST":
        phno=request.POST.get('phno')
        if TribalMember.objects.filter(phno=phno).exists() or TribeUser.objects.filter(phno=phno).exists():
            return HttpResponse('<p>Phone Taken Pls try another </p>')
        name=request.POST.get('name')
        tribe_id=request.POST.get('tribe_name')
        village_id=request.POST.get('village_name')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        village_name=Village.objects.get(id=village_id)
        tribe_name=Tribe.objects.get(id=tribe_id)
        TribalMember.objects.create(phno=phno,name=name,village=village_name,tribe=tribe_name,gender=gender)
        TribeUser.objects.create(phno=phno,password=password)
        request.session['user_id']=TribeUser.objects.get(phno=phno).id
        return redirect('home')
        # return HttpResponse('<p>Success<p>')

    elif request.method=='GET':
        tribe=Tribe.objects.all()
        village=Village.objects.all()
        return render(request,'sigup.html',{'tribe':tribe , 'village':village})
    
def login(request):
    if request.method=='POST':
        phno=request.POST.get('phno')
        password=request.POST.get('password')
        if TribeUser.objects.filter(phno=phno).exists():
            user = TribeUser.objects.get(phno=phno)
        else:
            return render(request, 'login.html', {'error': True, 'msg': 'Incorrect User'})
        
            
        if password!=user.password :
            return redirect('login',{'error':True,'msg':'Incorrect Password'})
        request.session['user_id']=user.id
        return redirect('home')
        # return HttpResponse('<p>Successsfull login</p>')
    elif request.method=='GET':
        return render(request,'login.html',{'error':False,'msg':''})
def home(request):
    # user_id=request.session.get('user_id')
    # user=TribeUser.objects.get(id=user_id)
    # tribeMember=TribalMember.objects.get(phno=user.phno)
    return render(request,'home.html')
def base(request):
    # user_id=request.session.get('user_id')
    # user=TribeUser.objects.get(id=user_id)
    # tribeMember=TribalMember.objects.get(phno=user.phno)
    return render(request,'base.html')
def logout(request):
    request.session.flush()
    return redirect('')

def temp(request):
    label, score = predict_sentiment("I love this product!")
    print(label, score)
    return render(request,'temp.html',{'label':label})
def adddata(request):
    if request.method=='POST':
        phno=request.POST.get('phno')
        name=request.POST.get('name')
        village_id=request.POST.get('village_name')
        role_id=request.POST.get('role')
        village_name=Village.objects.get(id=village_id)
        role=MangementRoles.objects.get(id=role_id)
        village=Village.objects.all()
        roles=MangementRoles.objects.all()
        if TribeUser.objects.filter(phno=phno).exists():
            return render(request, 'adddata.html', {'village':village,'roles':roles,'error': True, 'success':False,'msg': 'Incorrect User'})
        if MangementUser.objects.filter(phno=phno).exists():
            return render(request, 'adddata.html', {'village':village,'roles':roles,'error': True, 'success':False,'msg': 'Incorrect User'})
        MangementUser.objects.create(phno=phno,name=name,village=village_name,role=role)
        return render(request,'adddata.html',{'village':village,'roles':roles,'error':False,'success':True,'msg':'Created succesfully'})
    village=Village.objects.all()
    roles=MangementRoles.objects.all()
    return render(request,'adddata.html',{'village':village,'roles':roles,'error':False,'success':False,'msg':''})


            

