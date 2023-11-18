from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from data.models import user,homephoto,textile,jewellery,vegetable,other

def home(request):
	photos = homephoto.objects.all()
	context = {'photos': photos}	
	return render(request,'home.html',context)

def about(request):
	return render(request,'about.html')	

def process(request):
	return render(request,'process.html')	

def contact(request):
	return render(request,'contact.html')

def textileview(request):
	textile1 = textile.objects.all()
	context = {'text': textile1}
	return render(request,'text.html',context)

def jewelryview(request):
	jewellery1 = jewellery.objects.all()
	context = {'jewe': jewellery1}
	return render(request,'jewelry.html',context)	

def Vegitableview(request):
	vegetable1 = vegetable.objects.all()
	context = {'vege': vegetable1}
	return render(request,'Vegitable.html',context)	

def otherview(request):
	other1 = other.objects.all()
	context = {'text': other1}
	return render(request,'text.html',context)					

def utilities(request):
	return render(request,'utilities.html')

def Investment(request):
	return render(request,'Investment.html')

def realEstate(request):
	return render(request,'realEstate.html')

def accounts(request):
	return render(request,'accounts.html')		

def insurance(request):
	return render(request,'insurance.html')

def indpostcode(request):
	return render(request,'indpost.html')

def measurement(request):
	return render(request,'measurement.html')

def tdschart(request):
	return render(request,'tdschart.html')

def isdcode(request):
	return render(request,'isdcode.html')

def loaneligible(request):
	return render(request,'loaneligible.html')

def emicalculator(request):
	return render(request,'emicalculator.html')

def timezone(request):
	return render(request,'timezone.html')	

def login(request):
	if request.method == "POST":
		fn = request.POST['name']
		nm = request.POST['number']
		em = request.POST['email']
		ps = request.POST['password']
		ms = request.POST['message']
		password = make_password(ps)
		data = user(name=fn,mobile=nm,email=em,password=password,message=ms)
		data.save()
		return redirect('/contact/')
	return render(request,'login.html')	