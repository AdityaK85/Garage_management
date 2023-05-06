from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from datetime import datetime
from django.template.loader import render_to_string 
import csv
from django.conf import settings
import pandas as pd
from django.core.mail import send_mail ,EmailMultiAlternatives
from django.utils.html import strip_tags
from garage_motors import settings 
from django.core.files.storage import FileSystemStorage

 
# Create your views here.


def login(request):
    return render(request, 'login.html')

@csrf_exempt
def handle_login(request):
    user_name = request.POST.get('user_name')
    user_password = request.POST.get('user_password')  
    if not user_login.objects.filter(user_name = user_name, user_password = user_password).exists():
        return HttpResponse('1')
    else :
        obj = user_login.objects.get(user_name = user_name, user_password = user_password)
        request.session['user_id'] = str(obj.id)
        return HttpResponse('0')

def sign_in(request):
    return render(request, 'sign_in.html')

@csrf_exempt
def register_handle(request):
    user_name = request.POST.get('user_name')
    user_email = request.POST.get('user_email')
    user_pass = request.POST.get('user_pass')
    user_conf_pass = request.POST.get('user_conf_pass')
    
    if user_login.objects.filter(user_email = user_email):
        return HttpResponse("exists")
    elif(user_pass != user_conf_pass):
        return HttpResponse("not match")
    else :
        user_login.objects.create(
            user_name = user_name,
            user_email = user_email,
            user_password = user_pass,
            user_conf_pass = user_conf_pass,
        )
        return HttpResponse('1')
        

def sign_out(request):
    del request.session['user_id']
    return redirect('/')


def dashboard(request):
    if request.session.get('user_id'):
        return render(request, 'dashboard.html')
    else:
        return redirect('/')


def add_new_customer(request):
    if request.session.get('user_id'):
        return render(request, 'add_new_customer.html')
    else:
        return redirect('/')

@csrf_exempt
def manage_customer(request):
    if request.session.get('user_id'):
        get_data = add_new_cust.objects.all().order_by("-id")
        csvData = vehicle_details.objects.all().order_by("-id")
        obj = {
            'get_data': get_data,
            'csvData' : csvData
        }
        return render(request, 'manage_customer.html', obj)
    else:
        return redirect('/')

@csrf_exempt
def cust_det_get(request):
    if request.method == "POST":
        cust_name = request.POST.get('cust_name')
        cust_phone = request.POST.get('cust_phone')
        cust_mobile = request.POST.get('cust_mobile')
        cust_email = request.POST.get('cust_email')
        cust_skype = request.POST.get('cust_skype')
        cust_addr = request.POST.get('cust_addr')
        comp_name = request.POST.get('comp_name')
        comp_no = request.POST.get('comp_no')
        gst_vat_no = request.POST.get('gst_vat_no')
        comp_type = request.POST.get('comp_type')
        postal_addr = request.POST.get('postal_addr')
        phy_addr = request.POST.get('phy_addr')
        comp_web = request.POST.get('comp_web')
        dir_name = request.POST.get('dir_name')
        dir_mobile = request.POST.get('dir_mobile')
        dir_phone = request.POST.get('dir_phone')
        dir_addr = request.POST.get('dir_addr')
        trade_ref_1 = request.POST.get('trade_ref_1')
        trade_ref_2 = request.POST.get('trade_ref_2')
        trade_ref_3 = request.POST.get('trade_ref_3')
        status = request.POST.get('status')
        notes = request.POST.get('notes')
        notif = request.POST.get('notif')
        pay_met = request.POST.get('pay_met')
        pay_period = request.POST.get('pay_period')
        comp_sal_disc = request.POST.get('comp_sal_disc')
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        role_name = request.POST.get('role_name')

        obj = add_new_cust(cust_name=cust_name, cust_phone=cust_phone, cust_mobile=cust_mobile, cust_email=cust_email, cust_skype=cust_skype, cust_addr=cust_addr, comp_name=comp_name, comp_no=comp_no, gst_vat_no=gst_vat_no, comp_type=comp_type, postal_addr=postal_addr, phy_addr=phy_addr, comp_web=comp_web, dir_name=dir_name,
                           dir_mobile=dir_mobile, dir_phone=dir_phone,  dir_addr=dir_addr, trade_ref_1=trade_ref_1, trade_ref_2=trade_ref_2, trade_ref_3=trade_ref_3, status=status, notes=notes, notif=notif, pay_met=pay_met, pay_period=pay_period, comp_sal_disc=comp_sal_disc, user_name=user_name, user_pass=user_pass, role_name=role_name)
        obj.notif = request.POST.get('notif')
        obj.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")


@csrf_exempt
def delete_customer(request):
    id = request.POST.get('id')
    del_id = add_new_cust.objects.get(id=id).delete()
    return HttpResponse('success')



@csrf_exempt
def edit_customer(request, id):
    if request.session.get('user_id'):
        edit_cust = add_new_cust.objects.get(id=id)
        edit_data = add_new_cust.objects.all()

        obj = {
            'edit_cust': edit_cust,
            'edit_data': edit_data
        }

        return render(request, 'edit_customer.html', obj)
    else:
        return redirect('/')


@csrf_exempt
def update_customer(request, id):
    if request.session.get('user_id'):
        upd_id = add_new_cust.objects.get(id=id)
        upd_id.cust_name = request.POST.get('cust_name')
        upd_id.cust_phone = request.POST.get('cust_phone')
        upd_id.cust_mobile = request.POST.get('cust_mobile')
        upd_id.cust_email = request.POST.get('cust_email')
        upd_id.cust_skype = request.POST.get('cust_skype')
        upd_id.cust_addr = request.POST.get('cust_addr')
        upd_id.comp_name = request.POST.get('comp_name')
        upd_id.comp_no = request.POST.get('comp_no')
        upd_id.gst_vat_no = request.POST.get('gst_vat_no')
        upd_id.comp_type = request.POST.get('comp_type')
        upd_id.postal_addr = request.POST.get('postal_addr')
        upd_id.phy_addr = request.POST.get('phy_addr')
        upd_id.comp_web = request.POST.get('comp_web')
        upd_id.dir_name = request.POST.get('dir_name')
        upd_id.dir_mobile = request.POST.get('dir_mobile')
        upd_id.dir_phone = request.POST.get('dir_phone')
        upd_id.dir_addr = request.POST.get('dir_addr')
        upd_id.trade_ref_1 = request.POST.get('trade_ref_1')
        upd_id.trade_ref_2 = request.POST.get('trade_ref_2')
        upd_id.trade_ref_3 = request.POST.get('trade_ref_3')
        upd_id.status = request.POST.get('status')
        upd_id.notif = request.POST.get('notif')
        upd_id.pay_met = request.POST.get('pay_met')
        upd_id.pay_period = request.POST.get('pay_period')
        upd_id.comp_sal_disc = request.POST.get('comp_sal_disc')
        upd_id.user_name = request.POST.get('user_name')
        upd_id.user_pass = request.POST.get('user_pass')
        upd_id.role_name = request.POST.get('role_name')
        upd_id.save()
        return redirect('/manage-customer')


@csrf_exempt
def add_vehicles(request):
    if request.session.get('user_id'):
        obj = add_new_cust.objects.all().order_by('-id')
        return render(request, 'add_new_vehicles.html', {'obj': obj})
    else:
        return redirect('/')


@csrf_exempt
def vehicle_det_get(request):
    if request.method == "POST":
        cust_name = request.POST.get('cust_name')
        veh_name = request.POST.get('veh_name')
        veh_year = request.POST.get('veh_year')
        veh_reg_date = request.POST.get('veh_reg_date')
        veh_reg_no = request.POST.get('veh_reg_no')
        created_date =  datetime.now()


        vehicle_details.objects.create(
            fk_user_id=cust_name,
            veh_name=veh_name,
            veh_year=veh_year,
            veh_reg_date=veh_reg_date,
            veh_reg_no=veh_reg_no,
            created_date=created_date,
        )

        return HttpResponse('success')
    else:
        return HttpResponse("error")


def manage_vehicles(request):
    if request.session.get('user_id'):
        get_data = vehicle_details.objects.all().order_by("-id")
        obj = {
            'get_data': get_data,
        }
        return render(request, 'manage_vehicles.html', obj)
    else:
        return redirect('/')


@csrf_exempt
def delete_veh(request):
    id = request.POST.get("id")
    del_id = vehicle_details.objects.get(id=id).delete()
    return HttpResponse('success')

@csrf_exempt
def delete_mech(request):
    id = request.POST.get("id")
    add_mechanics.objects.get(id=id).delete()
    return HttpResponse('success')


@csrf_exempt
def edit_veh(request, id):
    if request.session.get('user_id'):
        edit_id = vehicle_details.objects.get(id=id)
        get_data = vehicle_details.objects.all()
        

        data = {
            'edit_id': edit_id,
            'get_data': get_data,
            
        }
        return render(request, 'edit_vehicle.html', data)
    else:
        return redirect('/')


@csrf_exempt
def update_veh(request, id):
    
    upd_id = vehicle_details.objects.get(id=id)
    # upd_id.fk_user = request.POST['fk_user']
    upd_id.veh_name = request.POST['veh_name']
    upd_id.veh_year = request.POST['veh_year']
    upd_id.veh_reg_date = request.POST['veh_reg_date']
    upd_id.veh_reg_no = request.POST['veh_reg_no']
    upd_id.save()
    return redirect('/manage-vehicles')


@csrf_exempt
def search_veh_report(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    if vehicle_details.objects.filter(created_date__gte=start_date, created_date__lte=end_date).exists():
        obj1 = vehicle_details.objects.filter(
            created_date__gte=start_date, created_date__lte=end_date).order_by('-created_date')
        rendered = render_to_string('search_vehicle.html', {
                                    'obj1': obj1, "start_date": start_date, "end_date": end_date, })
        return HttpResponse(rendered)
    else:
        return HttpResponse("error")


def add_quotation(request):
    if request.session.get('user_id'):
        obj = add_new_cust.objects.all().order_by('-id')
        obj1 = vehicle_details.objects.all().order_by('-id')
        veh_part = veh_parts.objects.all().order_by('-id')

        context = {
            'obj': obj,
            'obj1': obj1,
            'veh_part': veh_part,
        }

        return render(request, 'quotation.html', context)
    else:
        return redirect('/')


@csrf_exempt
def get_details(request):
        
    cust_id = request.POST.get('cust_id')
    cust_name = add_new_cust.objects.get(id=cust_id).cust_name
    address = add_new_cust.objects.get(id=cust_id).cust_addr
    phone = add_new_cust.objects.get(id=cust_id).cust_phone
    notes = add_new_cust.objects.get(id=cust_id).notes

    obj1 = vehicle_details.objects.all().order_by('-id')
    list = []
    if vehicle_details.objects.filter(fk_user_id=cust_id):
        obj1 = vehicle_details.objects.filter(fk_user=cust_id)

        for i in obj1:
            list.append(i.veh_reg_no)
            data = json.dumps(list)

        context = {
            'msg': 'success',
            'cust_name': cust_name,
            'address': address,
            'phone': phone,
            'notes': notes,
            'data': data
        }

        return JsonResponse(context)


@csrf_exempt
def store_quotation(request):
    if request.method == "POST":
        cust_name = request.POST.get('cust_name')
        quotation_no = request.POST.get('quotation_no')
        cust_addr = request.POST.get('cust_addr')
        quot_date = request.POST.get('quot_date')
        cust_phone = request.POST.get('cust_phone')
        veh_reg_no = request.POST.get('veh_reg_no')
        notes = request.POST.get('notes')
        # job Card
        job_name = request.POST.get('job_name')
        rates = request.POST.get('rates')
        note = request.POST.get('note')
        # vehicle parts
        items = request.POST.get('items')
        availale_qty = request.POST.get('availale_qty')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        total_price = request.POST.get('total_price')
        allTotal = request.POST.get('allTotal')
        

        quotations.objects.create(
            cust_name=cust_name,
            quotation_no=quotation_no,
            cust_addr=cust_addr,
            quot_date=quot_date,
            cust_phone=cust_phone,
            veh_reg_no=veh_reg_no,
            notes=notes,
            job_name=job_name,
            rates=rates,
            note=note,
            items=items,
            availale_qty=availale_qty,
            qty = qty,
            price=price,
            total_price=total_price,
            allTotal=allTotal
            
        )
        return HttpResponse('success')



@csrf_exempt
def veh_repair_part(request):
    part_id = request.POST.get('part_id')
    qty = veh_parts.objects.get(id=part_id).availale_qty
    price = veh_parts.objects.get(id=part_id).price

    context = {

        'msg': 'success',
        'qty': qty,
        'prod_price': price,

    }
    return JsonResponse(context)


def manage_quotation(request):
    if request.session.get('user_id'):
        quo_det = quotations.objects.all().order_by('-id')
        context = {
            'quot_det': quo_det,
        }
        
        return render(request, 'manage_quotation.html', context)

def edit_quotation(request, id):
    if request.session.get('user_id'):
        obj_cust = add_new_cust.objects.all().order_by('-id')
        obj = quotations.objects.get(id=id)
        get_det = quotations.objects.all()
        veh_part = veh_parts.objects.all().order_by('-id')
        
        context = {
            'obj' : obj,
            'obj_cust':obj_cust,
            'get_det' : get_det,
            'veh_part' : veh_part
        }
        return render(request, 'edit_Quaotation.html', context)
    else:
        return redirect('/')

@csrf_exempt
def update_quotation(request, id):
    edit_id = quotations.objects.get(id=id)
    edit_id.cust_name = request.POST['cust_name']
    edit_id.quotation_no = request.POST['quotation_no']
    edit_id.cust_addr = request.POST['cust_addr']
    edit_id.quot_date = request.POST['quot_date']
    edit_id.cust_phone = request.POST['cust_phone']
    edit_id.veh_reg_no = request.POST['veh_reg_no']
    edit_id.notes = request.POST['notes']
    edit_id.job_name = request.POST['job_name']
    edit_id.rates = request.POST['rates']
    edit_id.note = request.POST['note']
    edit_id.items = request.POST['items']
    edit_id.availale_qty = request.POST['availale_qty']
    edit_id.qty = request.POST['qty']
    edit_id.price = request.POST['price']
    edit_id.total_price = request.POST['total_price']
    edit_id.allTotal = request.POST['allTotal']
    edit_id.save()
    return redirect('/Manage-quotations')


@csrf_exempt
def delete_quot(request):
    if request.session.get('user_id'):
        id = request.POST.get('id')
        del_id = quotations.objects.get(id=id).delete()
        return HttpResponse('success')

    def edit_parts(request, id):
        veh_part = veh_parts.objects.all().order_by('-id')
        context = {
            'veh_part':veh_part,
        }
        return render(request, 'edit_vehicle_parts.html', context)
    


def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values ]
    print(list_of_csv)
    
    for i in list_of_csv:
        vehicle_details.objects.create(
            fk_user_id = i[0],
            veh_name = i[2],
            veh_year = i[3],
            veh_reg_date = i[4],
            veh_reg_no = i[5],
            created_date = i[6],
        )

@csrf_exempt
def importData(request):
    if request.method == "POST":
        csvSelectore = request.FILES.get('csvSelectore')

        obj = importExcel.objects.create(
            file = csvSelectore
        )
        create_db(obj.file)        
    
    return redirect('/manage-customer/')

    
@csrf_exempt
def sendMail(request):
    if request.method == "POST":
        cust_name = request.POST.get('cust_name')
        quotation_no = request.POST.get('quotation_no')
        cust_addr = request.POST.get('cust_addr')
        quot_date = request.POST.get('quot_date')
        cust_phone = request.POST.get('cust_phone')
        veh_reg_no = request.POST.get('veh_reg_no')
        notes = request.POST.get('notes')
        # job Card
        job_name = request.POST.get('job_name')
        rates = request.POST.get('rates')
        note = request.POST.get('note')
        # vehicle parts
        items = request.POST.get('items')
        availale_qty = request.POST.get('availale_qty')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        total_price = request.POST.get('total_price')
        allTotal = request.POST.get('allTotal')
    
        
        content = {
            'cust_name':cust_name,
            'quotation_no':quotation_no,
            'cust_addr':cust_addr,
            'quot_date':quot_date,
            'cust_phone':cust_phone,
            'veh_reg_no':veh_reg_no,
            'notes':notes,
            'job_name':job_name,
            'rates':rates,
            'note':note,
            'items':items,
            'availale_qty':availale_qty,
            'qty':qty,
            'price':price,
            'total_price':total_price,
            'allTotal':allTotal,
            
        }
        
        html_File = render_to_string("email_template.html", content)
        text_content = strip_tags(html_File)
        to = "adityakothekar79@gmail.com"  

        email = EmailMultiAlternatives(
            "All Servicing Details",
            text_content,
            settings.EMAIL_HOST_USER,
            [to]
        )
        email.attach_alternative(html_File, "text/html")
        email.send()
        
        return HttpResponse('success')
    
def job_order(request):
    if request.session.get('user_id'):
        obj = add_new_cust.objects.all().order_by('-id')
        obj1 = job_machanic.objects.all().order_by("-id")
        obj2 = machanic_name.objects.all().order_by("-id")

        context = {
            'obj': obj,
            'obj1': obj1,
            'obj2': obj2,
        }
        return render(request, 'add_job_order.html', context)
    else:
        return redirect('/')

@csrf_exempt
def get_job_details(request):
    cust_id = request.POST.get('cust_id')
    cust_name = add_new_cust.objects.get(id=cust_id).cust_name
    address = add_new_cust.objects.get(id=cust_id).cust_addr
    phone = add_new_cust.objects.get(id=cust_id).cust_phone
    notes = add_new_cust.objects.get(id=cust_id).notes
    mobile = add_new_cust.objects.get(id=cust_id).cust_mobile
    website = add_new_cust.objects.get(id=cust_id).comp_web

    
    obj1 = vehicle_details.objects.all().order_by('-id')
    obj2 = quotations.objects.all()
    list = []
    if vehicle_details.objects.filter(fk_user_id=cust_id) or quotations.objects.filter(cust_name= cust_name):
        obj1 = vehicle_details.objects.filter(fk_user=cust_id)
        obj2 = quotations.objects.filter(cust_name=cust_name)

        for i in obj1:
            list.append(i.veh_reg_no)
            data = json.dumps(list)
            
        quo_list = []
        
        for i in obj2:
            quo_list.append(i.quotation_no)
            
        
        context = {
            'msg': 'success',
            'cust_name': cust_name,
            'address': address,
            'phone': phone,
            'notes': notes,
            'mobile': mobile,
            'data': data,
            'website': website,
            'quo_data': quo_list
        }

        return JsonResponse(context)
    
    
@csrf_exempt
def add_job_order(request):
    if request.method == "POST":
        cust_name = request.POST.get('cust_name')   
        quotation_no = request.POST.get('quotation_no')   
        cust_addr = request.POST.get('cust_addr')   
        veh_reg_no = request.POST.get('veh_reg_no')   
        cust_phone = request.POST.get('cust_phone')   
        cust_mobile = request.POST.get('cust_mobile')   
        cust_refer = request.POST.get('cust_refer')   
        seh_time = request.POST.get('seh_time')   
        deliver_time = request.POST.get('deliver_time')   
        cust_note = request.POST.get('cust_note')   
        alert_via = request.POST.get('alert_via')   
        job_type = request.POST.get('job_type')   
        machanic_names = request.POST.get('machanic_names')   
        notes = request.POST.get('notes')   

        
        New_job_order.objects.create(
            cust_name=cust_name,
            quotation_no=quotation_no,
            cust_addr=cust_addr,
            cust_phone=cust_phone,
            veh_reg_no=veh_reg_no,
            cust_mobile=cust_mobile,
            notes=notes,
            cust_refer=cust_refer,
            seh_time=seh_time,
            deliver_time=deliver_time,
            cust_note=cust_note,
            alert_via=alert_via,
            job_type=job_type,
            machanic_names=machanic_names,            
        )
        
        return HttpResponse("success")
        


def manage_job_order(request):
    if request.session.get('user_id'):
        obj = New_job_order.objects.all()
        content = {
            'obj':obj
        }
        return render(request, 'manage_job_order.html', content)
    else:
        return redirect('/')


def edit_job(request, id):
    if request.session.get('user_id'):
        obj_id = New_job_order.objects.get(id=id)
        content = {
            'obj_id': obj_id,
        }
        return render(request, 'edit_job_order.html', content)
    else:
        return redirect('/')

@csrf_exempt 
def update_job(request, id):
    upd_job = New_job_order.objects.get(id=id)
    upd_job.cust_name = request.POST.get('cust_name')
    upd_job.quotation_no = request.POST.get('quotation_no')
    upd_job.cust_addr = request.POST.get('cust_addr')
    upd_job.veh_reg_no = request.POST.get('veh_reg_no')
    upd_job.cust_phone = request.POST.get('cust_phone')
    upd_job.cust_mobile = request.POST.get('cust_mobile')
    upd_job.cust_refer = request.POST.get('cust_refer')
    upd_job.seh_time = request.POST.get('seh_time')
    upd_job.deliver_time = request.POST.get('deliver_time')
    upd_job.cust_note = request.POST.get('cust_note')
    upd_job.alert_via = request.POST.get('alert_via')
    upd_job.job_type = request.POST.get('job_type')
    upd_job.machanic_names = request.POST.get('machanic_names')
    upd_job.notes = request.POST.get('notes')
    return redirect("/manage_job_order")
    
def delete_job(request):
    id = request.POST.get("id")
    del_id = New_job_order.objects.get(id=id).delete()
    return HttpResponse('success')

@csrf_exempt
def add_machnaics(request):
    if request.session.get('user_id'):
        return render(request, 'add_machanics.html')
    else:
        return redirect('/')

@csrf_exempt
def upload_mech_details(request):
    names = request.POST.get('name')
    age = request.POST.get('age')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')
    identity_image = request.FILES.get('identity_image')
    exp_cer_image = request.FILES.get('exp_cer_image')
    machanic_type = request.POST.get('machanic_type')
    no_of_exper = request.POST.get('no_of_exper')
    fss = FileSystemStorage()
    file_names = fss.save(identity_image.name , identity_image)
    file_name = fss.save(exp_cer_image.name , exp_cer_image)
    url = fss.url(file_names)
    url = fss.url(file_name)  
    obj = add_mechanics(name=names, age=age, mobile=mobile, address=address, identity_image=identity_image, exp_cer_image=exp_cer_image, machanic_type=machanic_type, no_of_exper=no_of_exper )
    obj.save()
    return JsonResponse({"status":1})
    
@csrf_exempt 
def edit_mech(request, id):
    if request.session.get('user_id'):
        edit_mech = add_mechanics.objects.get(id=id)
        edit_data = add_mechanics.objects.all()

        obj = {
            'edit_mech': edit_mech,
            'edit_data': edit_data
        }

        return render(request, 'edit_mechanic.html', obj)
    else:
        return redirect('/')


@csrf_exempt
def update_mechanics(request, id):
    upd_id = add_mechanics.objects.get(id=id)
    upd_id.name = request.POST.get('name')
    upd_id.age = request.POST.get('age')
    upd_id.mobile = request.POST.get('mobile')
    upd_id.address = request.POST.get('address')
    upd_id.machanic_type = request.POST.get('machanic_type')
    upd_id.no_of_exper = request.POST.get('no_of_exper')
   
    upd_id.save()
    return redirect('/manage_machanics')


def manage_machnaics(request):
    if request.session.get('user_id'):
        obj = add_mechanics.objects.all()
        content = {
            'obj' : obj
        }
        return render(request, 'manage_machanics.html', content)
    else:
        return redirect('/')

