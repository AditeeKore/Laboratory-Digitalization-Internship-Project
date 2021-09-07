from typing import Tuple
from django.db import models

# Create your models here.

class AllLabinfo(models.Model):
    Lab = models.CharField(max_length=20, unique=True, )
    NumberofPCs = models.IntegerField()
    BasicConfig = models.CharField(max_length=150, null = True)
    PCspurchasedinYr =models.CharField(max_length=30, null = True)
    OS = models.CharField(max_length=75, null = True)
    SpecialSoftware=models.CharField(max_length=100, null = True)
    # def __str__(self):
    #     return self.cod+" "+self.nume
    # class Meta:
    #     ordering = ["cod"]
    #     verbose_name_plural = "uploads"

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