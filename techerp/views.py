from django.shortcuts import render,redirect
from techerp.models import LOB,Manager,Employee,PCD_score
from techerp.forms import emp_login
from techerp.resources import MemberResource
from django.contrib.auth.models import User

# Create your views here.

# def meetings(request):
#     meetingData = Employee.objects.all()
#     return render(request, 'testapp/index.html', {'data': meetingData })

def export(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="member.csv"'
    #response = HttpResponse(dataset.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response




def empLogin(request):
	if request.method == 'POST':
		emp_id = request.POST['emp_id']
		epass =  request.POST['epass']
		post = Employee.objects.filter(emp_id=emp_id)
		if post:
			emp_id = request.POST['emp_id']
			request.session['emp_id'] = emp_id
			return redirect("profile")
		else:
			return render(request, 'testapp/empLogin.html', {})
	form=emp_login()
	return render(request, 'testapp/empLogin.html', {'form':form})

def profile(request):
	emp_id=request.session['emp_id']
	data1=Employee.objects.get(emp_id=emp_id)
	data=PCD_score.objects.get(emp_id=emp_id)
	# print(data)
	return render(request,'testapp/profile.html',{'data':data,'data1':data1})



def mlogin(request):
	return render(request,"testapp/manager.html")

def logout(request):
	try:
		del request.session['emp_id']
	except:
		pass 
	return render(request, 'testapp/logout.html', {})