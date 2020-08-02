from django.contrib import admin
from techerp.models import LOB,Manager,Employee,PCD_score,CSAT_RR_score,supervisor_audit_score,audit_score_manager,ata_emp_report,ata_mngr_report,calibration_report_emp,calibration_report_mngr
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.site_header='Tech Mahindra'
admin.site.site_title='Employee Audit Management'
admin.site.index_title='Tech Manhindra'
class LOBAdmin(admin.ModelAdmin):
	list_display=['lob_name']
	# pass

class ManagerAdmin(ImportExportModelAdmin):
	list_display=['mname','elob_name','mphone','memail']
	pass

class EmployeeAdmin(ImportExportModelAdmin):
	list_display=['emp_id','ename','ephone','eemail']
	list_editable=['ename']

# class PCDAdmin(admin.ModelAdmin):
# 	list_display =

class PCDSCOREAdmin(ImportExportModelAdmin):
	list_display=['emp_id','team_leader','am','pcd','compss','compo','cc','cp']
	search_fields=['emp_id']


admin.site.register(LOB,LOBAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(PCD_score,PCDSCOREAdmin)
admin.site.register(CSAT_RR_score)
admin.site.register(supervisor_audit_score)
admin.site.register(audit_score_manager)
admin.site.register(ata_emp_report)
admin.site.register(ata_mngr_report)
admin.site.register(calibration_report_emp)
admin.site.register(calibration_report_mngr)
