from django import forms
from techerp.models import Employee

class emp_login(forms.ModelForm):
	class Meta:
		model=Employee
		fields=['emp_id','epass']