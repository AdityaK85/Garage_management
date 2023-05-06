from django.db import models
from datetime import date, timezone,datetime

today = date.today()
# datet = datetime.strftime("%y-%m-%d")
# Create your models here.
# user name : vehicles
# user pass : 123

class user_login(models.Model):
    user_name = models.CharField(("User name"), max_length=50)
    user_email = models.CharField(("User Email"), max_length=50)
    user_password = models.CharField(("Password"), max_length=50)
    user_conf_pass = models.CharField(("Confirm Password"), max_length=50)
    
    def __str__(self) -> str:
        return self.user_name


class add_new_cust(models.Model):
    # contact details
    cust_name = models.CharField(max_length=50, null=True, blank=True)
    cust_phone = models.CharField(max_length=15, null=True, blank=True)
    cust_mobile = models.CharField(max_length=15, null=True, blank=True)
    cust_email = models.CharField(max_length=50, null=True, blank=True)
    cust_skype = models.CharField(max_length=50, null=True, blank=True)
    cust_addr = models.CharField(max_length=100, null=True, blank=True)
    # company Details
    comp_name = models.CharField(max_length=50, null=True, blank=True)
    comp_no = models.CharField(max_length=15, null=True, blank=True)
    gst_vat_no = models.CharField(max_length=15, null=True, blank=True)
    comp_type = models.CharField(max_length=50, null=True, blank=True)
    postal_addr = models.CharField(max_length=100, null=True, blank=True)
    phy_addr = models.CharField(max_length=100, null=True, blank=True)
    comp_web = models.CharField(max_length=100, null=True, blank=True)
    # AC details
    dir_name = models.CharField(max_length=50, null=True, blank=True)
    dir_mobile = models.CharField(max_length=15, null=True, blank=True)
    dir_phone = models.CharField(max_length=15, null=True, blank=True)
    dir_addr = models.CharField(max_length=50, null=True, blank=True)
    trade_ref_1 = models.CharField(max_length=50, null=True, blank=True)
    trade_ref_2 = models.CharField(max_length=50, null=True, blank=True)
    trade_ref_3 = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=50, null=True, blank=True)
    # Financial Details
    notif = models.CharField(max_length=50, null=True, blank=True)
    pay_met = models.CharField(max_length=50, null=True, blank=True)
    pay_period = models.CharField(max_length=50, null=True, blank=True)
    comp_sal_disc = models.CharField(max_length=50, null=True, blank=True)
    # Login Details
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_pass = models.CharField(max_length=50, null=True, blank=True)
    role_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id )+ " " + self.cust_name 


class vehicle_details(models.Model):
    fk_user = models.ForeignKey(add_new_cust,null=True, verbose_name=("Vehicle Holding Name"), on_delete=models.CASCADE)
    veh_name = models.CharField(max_length=50, null=True, blank=True)
    veh_year = models.IntegerField(null=True, blank=True)
    veh_reg_date = models.DateField()
    veh_reg_no = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now(),null=True, blank=True)

    def __str__(self) -> str:
        return self.veh_name

class quotations(models.Model):
    cust_name = models.CharField(max_length=500,null=True, blank=True)
    quotation_no= models.CharField(max_length=500,null=True, blank=True)
    cust_addr = models.CharField(max_length=500,null=True, blank=True)
    quot_date = models.DateField()
    cust_phone = models.CharField(max_length=50,null=True, blank=True)
    veh_reg_no = models.CharField(max_length=500,null=True, blank=True)
    notes = models.CharField(max_length=500,null=True, blank=True)
    # job Card
    job_name = models.CharField(max_length=50,null=True, blank=True)
    rates = models.CharField(max_length=500,null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    # veh_parts
    items = models.CharField( max_length=500,null=True, blank=True)
    availale_qty = models.CharField( max_length=500,null=True, blank=True)
    qty = models.CharField( max_length=500,null=True, blank=True)
    price = models.CharField( max_length=500,null=True, blank=True)
    total_price = models.CharField( max_length=500,null=True, blank=True)
    allTotal = models.CharField( max_length=500,null=True, blank=True)
    
    def __str__(self) -> str:
        return  self.cust_name
    
class veh_parts(models.Model):
    items = models.CharField( max_length=500,null=True, blank=True)
    availale_qty = models.CharField( max_length=500,null=True, blank=True)
    price = models.CharField( max_length=500,null=True, blank=True)
    
    def __str__(self) -> str:
        return self.items

    
class importExcel(models.Model):
    file = models.FileField(upload_to="import_excel_files")
    
    
class job_machanic(models.Model):
    job_type = models.CharField(("Job Type"), max_length=50)
    
    def __str__(self) -> str:
        return self.job_type
    
class machanic_name(models.Model):
    machanic_names = models.CharField(("Machanic Name"), max_length=50)
    
    def __str__(self) -> str:
        return self.machanic_name
    

class New_job_order(models.Model):
    cust_name = models.CharField(("Customer Name"), max_length=50)
    quotation_no = models.CharField(("Quotation No."), max_length=50)
    cust_addr = models.CharField(("Customer Address."), max_length=50)
    veh_reg_no = models.CharField(("Vehical Registration No."), max_length=50)
    cust_phone = models.CharField(("Customer Phone No."), max_length=50)
    cust_mobile = models.CharField(("Customer Mobile No."), max_length=50)
    cust_refer = models.CharField(("Reference"), max_length=50)
    seh_time = models.CharField(("Schedule_Date"), max_length=50)
    deliver_time = models.CharField(("Delivery Date"), max_length=50)
    cust_note = models.CharField(("Customer Details"), max_length=50)
    alert_via = models.CharField(("Alert Via"), max_length=50)
    job_type = models.CharField(("Job Type"), max_length=50)
    machanic_names = models.CharField(("Machanic Name"), max_length=50, null=True, blank=True)
    notes = models.CharField(("Customer Note"), max_length=50)
    
    def __str__(self) -> str:
        return (f"Id {str(self.id)}  Name : {self.cust_name}")
     
class add_mechanics(models.Model):
    name = models.CharField(("Mechanics Name"), max_length=50,null=True, blank=True)
    age = models.CharField(("AGE"), max_length=50,null=True, blank=True)
    mobile = models.CharField(("Mobile"), max_length=50 ,null=True, blank=True)
    address = models.CharField(("Address"), max_length=50,null=True, blank=True)
    identity_image = models.FileField(("Identity Image"), upload_to='mechanics_identity', max_length=100)
    exp_cer_image = models.FileField(("Experienced Certificate Image"), upload_to='mechanics_certificate', max_length=100)
    machanic_type = models.CharField(("Machanics Type"), max_length=50, default="Fresher" , null=True, blank=True)
    no_of_exper = models.CharField(("Experience"), max_length=50,null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name