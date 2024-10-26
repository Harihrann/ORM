from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
    Name = models.CharField(Max_Length=100)
    Account_No = models.IntegerField(primary_key="Account_No")
    IFSC_Code = models.CharField(Max_Length=20)
    Branch = models.CharField(Max_Length=30)
    Phone_Number = models.IntegerField()
    Loan_Type = models.CharField(Max_Length=40)
    Aadhar_No = models.IntegerField()
    Loan_amount = models.FloatField()
    Time_Period = models.IntegerField()
    Rate_of_Interest = models.FloatField()
     
class BankAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Account_No', 'IFSC_Code', 'Branch', 'Phone_Number', 'Loan_Type', 'Aadhar_no', ' Loan_amount', 'Time_Period', 'Rate_of_Interest')
