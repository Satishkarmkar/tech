from django.db import models
from datetime import datetime


# Create your models here.
class LOB(models.Model):
	lob_name=models.CharField(max_length=30,verbose_name='LOB')

	def  __str__(self):
		return self.lob_name
class Manager(models.Model):
	emp_id=models.IntegerField(verbose_name='ID')
	mname=models.CharField(max_length=30,verbose_name='Manager name')
	elob_name=models.ForeignKey(LOB,on_delete=models.CASCADE,verbose_name='LOB',null=True,default=None)
	mphone=models.CharField(max_length=30,verbose_name='Manager Phone Number')
	memail=models.EmailField(verbose_name='Manager Email Id')
	mpass=models.CharField(max_length=30)

	def __str__(self):
		return self.mname

	class Meta:
		managed = True
		db_table = 'Manager'


class Employee(models.Model):
	emp_id=models.IntegerField(verbose_name='Employee Id')
	ename=models.CharField(max_length=30,verbose_name='Employee Name')
	lob_name=models.ForeignKey(LOB,on_delete=models.CASCADE,verbose_name='LOB',null=True,default=None)
	ephone=models.CharField(max_length=30,verbose_name='Employee Phone')
	eemail=models.EmailField(verbose_name='Employee Email Id')
	epass=models.CharField(max_length=30)

	def __str__(self):
		return self.ename

	class Meta:
		managed = True
		db_table = 'Employee'

class PCD_score(models.Model):
    emp_id=models.IntegerField(default=True,null=True)
    team_leader=models.CharField(max_length=30)
    am=models.IntegerField()
    pcd=models.IntegerField()
    compss=models.IntegerField()
    compo=models.IntegerField()
    cc=models.IntegerField()
    cp=models.IntegerField()
    date_time=models.DateTimeField()

    def _str_(self):
        return self.emp_id

    class Meta:
        verbose_name='PCD SCORE'
        verbose_name_plural='PCD SCORE'

class CSAT_RR_score(models.Model):
    agent_id = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    team_leader = models.CharField(max_length=30)
    csat_score = models.IntegerField()
    rr_score = models.IntegerField()

    def _str_(self):
        return self.agent_id
    class Meta:
        verbose_name='CSAT RR SCORE'
        verbose_name_plural='CSAT RR SCORE'

class supervisor_audit_score(models.Model):
    month=models.DateField()
    emp_id=models.IntegerField()
    name=models.CharField(max_length=30)
    score=models.IntegerField()
    cop=models.IntegerField()
    com=models.IntegerField()
    cs=models.IntegerField()
    cp=models.IntegerField()

    def _str_(self):
        return self.emp_id
    class Meta:
        verbose_name='SUPERVISOR AUDIT SCORE'
        verbose_name_plural='SUPERVISOR AUDIT SCORE'

class audit_score_manager(models.Model):
    month = models.DateField()
    emp_id = models.IntegerField()
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    cop = models.IntegerField()
    com = models.IntegerField()
    cs = models.IntegerField()
    cp = models.IntegerField()

    def _str_(self):
        return self.name
    class Meta:
        verbose_name='MANAGER AUDIT SCORE'
        verbose_name_plural='MANAGER AUDIT SCORE'

class ata_emp_report(models.Model):
    month = models.DateField()
    variance = models.IntegerField()

    def _str_(self):
        return None
    class Meta:
        verbose_name='ATA REPORT FOR EMPLOYEE'
        verbose_name_plural='ATA REPORT FOR EMPLOYEE'

class ata_mngr_report(models.Model):
    month=models.DateField()
    emp_code=models.IntegerField()
    ename = models.CharField(max_length=30)
    ata_variance=models.IntegerField()

    def _str_(self):
        return self.emp_code
    class Meta:
        verbose_name='ATA REPORT FOR MANAGER'
        verbose_name_plural='ATA REPORT FOR MANAGER'

class calibration_report_emp(models.Model):
    month=models.DateField()
    report=models.CharField(max_length=30)

    def _str_(self):
        return None
    class Meta:
        verbose_name='Calibrations Report for Employee'
        verbose_name_plural='calibration Report For Employee'

class calibration_report_mngr(models.Model):
    month=models.DateField()
    emp_code=models.IntegerField()
    ename=models.CharField(max_length=30)
    score=models.IntegerField()

    def _str_(self):
        return self.emp_code

    class Meta:
        verbose_name='Calibrations Report for Manager'
        verbose_name_plural='calibration Report For Manger'
