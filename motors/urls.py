from  django.urls import path
from .import views

urlpatterns = [
    # login
    path('', views.login, name='login'),
    path('handle_login/', views.handle_login,name='handle_login'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('register_handle/', views.register_handle, name='register_handle'),
    path('sign_out/', views.sign_out, name='sign_out'),
    
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # customers
    path('new-customer/', views.add_new_customer, name='add_new_cust'),
    path('cust_det_get/',views.cust_det_get,name='cust_det_get'),
    path('manage-customer/',views.manage_customer,name='manage_customer'),
    path('edit_customer/<int:id>',views.edit_customer, name='edit_customer'),
    path('update_customer/<int:id>',views.update_customer, name='update_customer'),
    path('delete_customer/',views.delete_customer, name='delete_customer/'),
    
    # Vehicles
    path('new-vehicles/',views.add_vehicles,name='add_new_vehicles'),
    path('vehicle_details_get/',views.vehicle_det_get,name="add_vehicle"),
    path('manage-vehicles/',views.manage_vehicles,name='manage_vehicles'),
    path('edit/<int:id>',views.edit_veh, name="edit"),
    path('update/<int:id>',views.update_veh, name="update"),
    path('delete/',views.delete_veh, name="delete"),
    path('search_vehicle_date/',views.search_veh_report,name="search_vehicle_date"),
    path('import-excel/',views.importData,name="import-excel"),
    
    # Quotation
    path('add Quotations/',views.add_quotation,name="add quotation"),
    path('show_details/',views.get_details,name="get details"),
    path('store_quotation/',views.store_quotation,name="store quotations"),
    
    
    # vehicle repairing parts details
    path('veh_repair_part/',views.veh_repair_part,name="veh_repair_part"),
    
    # Manage Quatations
    path('Manage-quotations/',views.manage_quotation,name="Manage-quotations"),
    path('edit-quotation/<int:id>',views.edit_quotation,name="edit-quotations"),
    path('update_quotation/<int:id>',views.update_quotation,name="update-quotations"),
    path('delete_quotation/',views.delete_quot, name="delete_quotation"),
    
    # send email 
    path('send_mail/', views.sendMail, name="send_mail"),
    
    # job order
    path('job_order/', views.job_order, name="job_order"),
    path('Job_details/',views.get_job_details,name="job_details"),
    path('store_job_order/',views.add_job_order,name="store_job_order"),
    path('edit_job/<int:id>',views.edit_job,name="edit_job_order"),
    path('update_job/<int:id>',views.update_job,name="update_job_order"),
    path('delete_job/<int:id>',views.delete_job,name="delete_job_order"),
    path('manage_job_order/', views.manage_job_order, name="manage_job_order"),
    
    # add Machanics
    path('add_machanics/', views.add_machnaics, name="add_machanics"),
    path('upload_mech_details/', views.upload_mech_details, name="upload_mech_details"),
    path('edit_mech/<int:id>', views.edit_mech, name="delete_mech"),
    path('update_mechanics/<int:id>', views.update_mechanics, name="delete_mech"),
    path('delete_mech/', views.delete_mech, name="delete_mech"),
    path('manage_machanics/', views.manage_machnaics, name="manage_machanics"),
    
    
    
]
