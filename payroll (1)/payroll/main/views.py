from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from main.models import EmployeeDetail , SalaryDetail
from .models import *

# Create your views here.


def index(response):
	return HttpResponse("<H1>Home page</H1>")


#employees
def employee(request):
	error =""
	if request.method == "POST":
		fn = request.POST['firstName']
		ln = request.POST['lastName']
		em = request.POST['email']
		ph = request.POST['phone']
		ad1 = request.POST['addressLine1']
		ad2 = request.POST['addressLine2']
		ad3 = request.POST['addressLine3']
		
		

		e=EmployeeDetail(fname=fn,lname=ln,email=em,phone=ph,address1=ad1 ,address2=ad2,address3=ad3)
		e.save()
	return render(request, "main/employee.html", {'firstname': 'Linus'})


#hrs
def hr(request, employee_id):
	
	if request.method == "POST":
		bp = request.POST['basicPay']
		dg = request.POST['designation']
		jd = request.POST.get('joiningDate', '2024-10-01')
		pk = employee_id
		instance=get_object_or_404(EmployeeDetail,pk=pk)
		instance.basicpay=bp
		instance.designation=dg
		instance.joiningdate=jd
		instance.save()
		return redirect('/hrlist')
	instance=get_object_or_404(EmployeeDetail,pk=employee_id)
	return render(request, "main/hr.html", {'employee': instance})



def hrlist(request):
	employees = EmployeeDetail.objects.all()  # Fetch all employee data
	return render(request, "main/hrlist.html", {'employees': employees})


#clearks
def clerk(request, employee_id):
	if request.method == "POST":
		empid = float(employee_id)
		hra = float(request.POST['hra'])
		da = float(request.POST['da'])
		com = float(request.POST['commission'])
		ma = float(request.POST['ma'])
		gt = float(request.POST['gratuity'])
		it = float(request.POST['it'])
		pt = float(request.POST['pt'])
		ins = float(request.POST['insurance'])
		wk = float(request.POST['working'])
		p = float(request.POST['present'])
		instance=get_object_or_404(EmployeeDetail,pk=empid)
		
		Basicpay = float(instance.basicpay)

		if(request.POST['hraType'] == "Percent"):
			hra = Basicpay/100 * hra

		if(request.POST['daType'] == "Percent"):
			da = Basicpay/100 * da

		if(request.POST['commissionType'] == "Percent"):
			com = Basicpay/100 * com

		if(request.POST['maType'] == "Percent"):
			ma = Basicpay/100 * ma

		if(request.POST['gratuityType'] == "Percent"):
			gt = Basicpay/100 * gt

		if(request.POST['itType'] == "Percent"):
			it = Basicpay/100 * it

		if(request.POST['ptType'] == "Percent"):
			pt = Basicpay/100 * pt

		if(request.POST['insuranceType'] == "Percent"):
			ins = Basicpay/100 * ins

		attendanceDed = float(Basicpay/wk) * float(wk-p)
		
		net = Basicpay + hra + da + com + ma + gt - it - pt - ins - attendanceDed
		s=SalaryDetail(empid=instance,hra=hra,da=da,com=com,ma=ma,gt=gt,it=it,pt=pt,ins=ins,work=attendanceDed,present=p,net= net)
		s.save()

		return redirect(f'/payslip/{s.salid}')





	instance=get_object_or_404(EmployeeDetail,pk=employee_id)

	return render(request, "main/clerk.html", {'employee': instance})




def clerklist(request):
	employees = EmployeeDetail.objects.exclude(designation__exact='').exclude(designation__isnull=True)
	return render(request, "main/clerklist.html", {'employees': employees})


def payslip(request,salid):
	salary = SalaryDetail.objects.get(salid=salid)  
	employee = salary.empid
	return render(request, 'main/payslip.html', {'pay_slip': salary, 'emp_details': employee})