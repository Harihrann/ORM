from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
    Name = models.CharField(max_length=100)
    Account_No = models.IntegerField(primary_key="Account_No")
    Phone_Number = models.IntegerField()
    Aadhar_No = models.IntegerField()
    Loan_amount = models.FloatField()
    Time_Period = models.IntegerField()
     
class BankAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Account_No', 'Phone_Number','Aadhar_No', 'Loan_amount', 'Time_Period',)
