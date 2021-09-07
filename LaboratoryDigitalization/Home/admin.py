from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AllLabinfo, Lab7A, Lab7A_SW_Inst, Lab7B_SW_Inst, Lab7C_SW_Inst, Lab7D_SW_Inst, Lab7E_SW_Inst, Lab7B, Lab7C, Lab7D, Lab7E, tt_file, lab_ready_cert

# Register your models here.

@admin.register(AllLabinfo)
class uploadadmin(ImportExportModelAdmin):
    list_display = ('Lab', 'NumberofPCs', 'BasicConfig', 'PCspurchasedinYr', 'OS', 'SpecialSoftware')

@admin.register(Lab7A)
class Lab7Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab7B)
class Lab7Binfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab7C)
class Lab7Cinfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab7D)
class Lab7Dinfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab7E)
class Lab7Einfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab7A_SW_Inst)
class Lab7Aswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab7B_SW_Inst)
class Lab7Bswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab7C_SW_Inst)
class Lab7Cswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab7D_SW_Inst)
class Lab7Dswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab7E_SW_Inst)
class Lab7Eswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

admin.site.register(tt_file)

admin.site.register(lab_ready_cert)