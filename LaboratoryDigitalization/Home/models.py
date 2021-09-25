from typing import Tuple
from django.db import models

# Create your models here.

#lab timetables
class Lab5A_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab5B_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab5C_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab5D_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab5E_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab7A_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab7B_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab7C_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab7D_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab7E_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab11A_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Lab11B_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class LabCC1_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class LabCC2_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class LabCC3_tt_booking(models.Model):
    TIME = models.CharField(max_length=20)
    MONDAY = models.CharField(max_length=20)
    TUESDAY = models.CharField(max_length=20)
    WEDNESDAY = models.CharField(max_length=20)
    THURSDAY = models.CharField(max_length=20)
    FRIDAY = models.CharField(max_length=20)
    SATURDAY = models.CharField(max_length=20)

class Booking_Labs(models.Model):
    main_lab_name = models.CharField(max_length=20)
    sub_lab_name = models.CharField(max_length=10)

class Slot_Booking(models.Model):
    event_name = models.CharField(max_length=100)
    lab_no = models.CharField(max_length=10)
    slot_time = models.CharField(max_length=100)
    slot_date = models.DateField()
    booked_by = models.CharField(max_length=100)
    def __str__(self):
        return self.event_name

class AllLabinfo(models.Model):
    Lab = models.CharField(max_length=20, unique=True, )
    NumberofPCs = models.IntegerField()
    BasicConfig = models.CharField(max_length=150, null = True)
    PCspurchasedinYr =models.CharField(max_length=30, null = True)
    OS = models.CharField(max_length=75, null = True)
    SpecialSoftware=models.CharField(max_length=100, null = True)

#LAB 7
class Lab7A(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab7B(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab7C(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab7D(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab7E(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab7A_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab7B_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab7C_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab7D_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab7E_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

#LAB 5
class Lab5A(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab5B(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab5C(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab5D(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab5E(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab5A_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab5B_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab5C_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab5D_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab5E_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

#LAB 11
class Lab11A(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab11B(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class Lab11A_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class Lab11B_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

#LAB CC
class LabCC1(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class LabCC2(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class LabCC3(models.Model):
    ComputerName = models.CharField(max_length=20, unique=True)
    Processor = models.CharField(max_length=200)
    RAM = models.CharField(max_length=10)
    HardDisk = models.CharField(max_length=10)
    MotherBoard = models.CharField(max_length=20)
    Basic_OS = models.CharField(max_length=50)
    SpecialPurpose = models.CharField(max_length=150)
    DateOfPurchase = models.CharField(max_length=30)
    WorkingStatus = models.CharField(max_length=30)

class LabCC1_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class LabCC2_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class LabCC3_SW_Inst(models.Model):
    SoftwareInstalled = models.CharField(max_length=50)
    Version = models.CharField(max_length=20, null=True)

class tt_file(models.Model):
    lab_no = models.CharField(max_length=10, unique=True)
    tt_pdf = models.FileField(upload_to='uploads/timetable')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.lab_no

class lab_ready_cert(models.Model):
    lab_no = models.CharField(max_length=10, unique=True)
    cert_pdf = models.FileField(upload_to='uploads/lab_ready_cert')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.lab_no