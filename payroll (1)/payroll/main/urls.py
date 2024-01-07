from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
	path("", views.index, name="index"),
	path("employee/", views.employee, name="employee"),
	path("hr/<int:employee_id>/", views.hr, name="hr"),
	path("hrlist/", views.hrlist, name="hrlist"),
	path("clerk/<int:employee_id>/", views.clerk, name="clerk"),
	path("clerklist/", views.clerklist, name="clerklist"),
	path("payslip/<int:salid>/", views.payslip, name ="payslip"),
]


