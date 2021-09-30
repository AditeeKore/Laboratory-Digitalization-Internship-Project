from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
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

@admin.register(Lab5A)
class Lab5Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab5B)
class Lab5Binfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab5C)
class Lab5Cinfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab5D)
class Lab5Dinfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab5E)
class Lab5Einfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab5A_SW_Inst)
class Lab5Aswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab5B_SW_Inst)
class Lab5Bswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab5C_SW_Inst)
class Lab5Cswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab5D_SW_Inst)
class Lab5Dswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab5E_SW_Inst)
class Lab5Eswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab11A)
class Lab11Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab11B)
class Lab11Binfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(Lab11A_SW_Inst)
class Lab11Aswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab11B_SW_Inst)
class Lab11Bswinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(LabCC1)
class Lab11Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(LabCC2)
class Lab11Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(LabCC3)
class Lab11Ainfo(ImportExportModelAdmin):
    list_display = ('ComputerName', 'Processor', 'RAM', 'HardDisk', 'MotherBoard', 'Basic_OS', 'SpecialPurpose', 'DateOfPurchase', 'WorkingStatus')

@admin.register(LabCC1_SW_Inst)
class LabCC1swinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(LabCC2_SW_Inst)
class LabCC2swinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(LabCC3_SW_Inst)
class LabCC3swinfo(ImportExportModelAdmin):
    list_display = ('SoftwareInstalled', 'Version')

@admin.register(Lab5A_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab5B_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab5D_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab5E_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab7A_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab7B_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab7C_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab7D_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab7E_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab11A_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(Lab11B_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(LabCC1_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(LabCC2_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

@admin.register(LabCC3_tt_booking)
class Lab5A_tt_booking(ImportExportModelAdmin):
    list_display = ('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

admin.site.register(tt_file)

admin.site.register(lab_ready_cert)

admin.site.register(Slot_Booking)

admin.site.register(Booking_Labs)

admin.site.register(Lab5_Miscellaneous)

admin.site.register(Lab7_Miscellaneous)

admin.site.register(Lab11_Miscellaneous)

admin.site.register(LabCC_Miscellaneous)