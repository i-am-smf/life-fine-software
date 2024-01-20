from datetime import date, datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import os
import mysql.connector

cwd=os.getcwd()
main=Tk()
main.title("LifeFine")
main.iconbitmap("./images/lf2.ico")
main.geometry("1500x800")
main.configure(bg="antiquewhite4")
main.state('zoomed')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="smfsql123",
    database="LIFEFINE"
)
mydb1=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="smfsql123",
    database="LIFEFINE_CUSTOMERS"
)

my_cursor=mydb.cursor()
my_cursor1=mydb1.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS all_customers(id_number VARCHAR(225),\
    first_name VARCHAR(225),\
    last_name VARCHAR(225),\
    root VARCHAR(225),\
    address_1 VARCHAR(225),\
    address_2 VARCHAR(225),\
    district VARCHAR(225),\
    state VARCHAR(225),\
    pincode VARCHAR(225),\
    mobile1 VARCHAR(225),\
    mobile2 VARCHAR(225),\
    telephone VARCHAR(225),\
    warrenty_from VARCHAR(225),\
    warrenty_to VARCHAR(225),\
    model VARCHAR(225),\
    date VARCHAR(225),\
    service_type VARCHAR(225),\
    se_name VARCHAR(225),\
    customer_notes VARCHAR(225),\
    applied_date VARCHAR(225))")
 
my_cursor.execute("CREATE TABLE IF NOT EXISTS compliants(id_number VARCHAR(225),\
    compliant_date VARCHAR(225),\
    compliant_details VARCHAR(225),\
    notes VARCHAR(225))")

now=datetime.now()
yr=now.strftime("%Y")
yr1=int(yr)
today=now.strftime("%d-%m-%Y")

def insert():
    Preview.destroy()
    sql_command="INSERT INTO all_customers(id_number,first_name,last_name,root,address_1,address_2,district,state,pincode,mobile1,mobile2,telephone,warrenty_from,warrenty_to,model,date,service_type,se_name,applied_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(id_num.get(),f_name.get(),l_name.get(),root.get(),address1.get(),address2.get(),district.get(),state.get(),pincode.get(),mobile1.get(),mobile2.get(),telephone.get(),warrenty_from.get(),warrenty_to.get(),model.get(),date1.get(),service_type_select.get(),se_name.get(),today)
    my_cursor.execute(sql_command,values)
    id=id_num.get()
    mydb.commit()
    my_cursor1.execute(f"CREATE TABLE IF NOT EXISTS `{id}`(visit_date VARCHAR(225),\
    work_details VARCHAR(225),\
    parts_replaced VARCHAR(225),\
    amount_charged VARCHAR(225),\
    feed_water VARCHAR(225),\
    pure_water VARCHAR(225),\
    serviced_by VARCHAR(225),\
    notes VARCHAR(225))")

    nc.destroy()

def preview():
    global Preview
    Preview=Tk()
    Preview.title("Customer Details")
    #Preview.iconbitmap(cwd+"\LIFEFINE\icons\lf2.ico")
    Preview.configure(bg="cadetblue")

    preview_frame=LabelFrame(Preview,text=id_num.get(),pady=20,padx=20)
    preview_frame.grid(row=0,column=0,padx=20,pady=20)
    preview_frame.configure(bg="cadetblue1")

    label1=Label(preview_frame,text="First name :")
    label1.grid(row=0,column=0,padx=40,pady=10,sticky=W)
    label1.configure(bg="cadetblue2")
    f_name_show=Label(preview_frame,text=f_name.get())
    f_name_show.grid(row=0,column=1,padx=5,pady=10,sticky=W)
    f_name_show.configure(bg="cadetblue2")

    label2=Label(preview_frame,text="Last name :")
    label2.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    label2.configure(bg="cadetblue2")
    l_name_show=Label(preview_frame,text=l_name.get())
    l_name_show.grid(row=0,column=3,padx=5,pady=5,sticky=W)
    l_name_show.configure(bg="cadetblue2")

    label3=Label(preview_frame,text="Root :")
    label3.grid(row=1,column=0,padx=40,pady=5,sticky=W)
    label3.configure(bg="cadetblue2")
    root_show=Label(preview_frame,text=root.get())
    root_show.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    root_show.configure(bg="cadetblue2")

    label4=Label(preview_frame,text="Address 1 :")
    label4.grid(row=2,column=0,padx=40,pady=5,sticky=W)
    label4.configure(bg="cadetblue2")
    address1_show=Label(preview_frame,text=address1.get())
    address1_show.grid(row=2,column=1,padx=5,pady=5,sticky=W)
    address1_show.configure(bg="cadetblue2")

    label5=Label(preview_frame,text="Address 2 :")
    label5.grid(row=3,column=0,padx=40,pady=5,sticky=W)
    label5.configure(bg="cadetblue2")
    address2_show=Label(preview_frame,text=address2.get())
    address2_show.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    address2_show.configure(bg="cadetblue2")

    label6=Label(preview_frame,text="District :")
    label6.grid(row=4,column=0,padx=40,pady=5,sticky=W)
    label6.configure(bg="cadetblue2")
    district_show=Label(preview_frame,text=district.get())
    district_show.grid(row=4,column=1,padx=5,pady=5,sticky=W)
    district_show.configure(bg="cadetblue2")

    label7=Label(preview_frame,text="State :")
    label7.grid(row=5,column=0,padx=40,pady=5,sticky=W)
    label7.configure(bg="cadetblue2")
    state_show=Label(preview_frame,text=state.get())
    state_show.grid(row=5,column=1,padx=5,pady=5,sticky=W)
    state_show.configure(bg="cadetblue2")

    label8=Label(preview_frame,text="Pincode :")
    label8.grid(row=6,column=0,padx=40,pady=5,sticky=W)
    label8.configure(bg="cadetblue2")
    pincode_show=Label(preview_frame,text=pincode.get())
    pincode_show.grid(row=6,column=1,padx=5,pady=5,sticky=W)
    pincode_show.configure(bg="cadetblue2")

    label9=Label(preview_frame,text="Mobile 1 :")
    label9.grid(row=7,column=0,padx=40,pady=5,sticky=W)
    label9.configure(bg="cadetblue2")
    mobile1_show=Label(preview_frame,text=mobile1.get())
    mobile1_show.grid(row=7,column=1,padx=5,pady=5,sticky=W)
    mobile1_show.configure(bg="cadetblue2")

    label10=Label(preview_frame,text="Mobile 2 :")
    label10.grid(row=7,column=2,padx=40,pady=5,sticky=W)
    label10.configure(bg="cadetblue2")
    mobile2_show=Label(preview_frame,text=mobile2.get())
    mobile2_show.grid(row=7,column=3,padx=5,pady=5,sticky=W)
    mobile2_show.configure(bg="cadetblue2")

    label11=Label(preview_frame,text="Telephone :")
    label11.grid(row=8,column=0,padx=40,pady=5,sticky=W)
    label11.configure(bg="cadetblue2")
    telephone_show=Label(preview_frame,text=telephone.get())
    telephone_show.grid(row=8,column=1,padx=5,pady=5,sticky=W)
    telephone_show.configure(bg="cadetblue2")

    label12=Label(preview_frame,text="Warrenty From :")
    label12.grid(row=9,column=0,padx=40,pady=5,sticky=W)
    label12.configure(bg="cadetblue2")
    warrenty_from_show=Label(preview_frame,text=warrenty_from.get())
    warrenty_from_show.grid(row=9,column=1,padx=5,pady=5,sticky=W)
    warrenty_from_show.configure(bg="cadetblue2")

    label13=Label(preview_frame,text="To :")
    label13.grid(row=9,column=2,padx=40,pady=5,sticky=W)
    label13.configure(bg="cadetblue2")
    warrenty_to_show=Label(preview_frame,text=warrenty_to.get())
    warrenty_to_show.grid(row=9,column=3,padx=5,pady=5,sticky=W)
    warrenty_to_show.configure(bg="cadetblue2")

    label14=Label(preview_frame,text="Model :")
    label14.grid(row=10,column=0,padx=40,pady=5,sticky=W)
    label14.configure(bg="cadetblue2")
    model_show=Label(preview_frame,text=model.get())
    model_show.grid(row=10,column=1,padx=5,pady=5,sticky=W)
    model_show.configure(bg="cadetblue2")

    label15=Label(preview_frame,text="Date Of Installation :")
    label15.grid(row=11,column=0,padx=40,pady=5,sticky=W)
    label15.configure(bg="cadetblue2")
    date1_show=Label(preview_frame,text=date1.get())
    date1_show.grid(row=11,column=1,padx=5,pady=5,sticky=W)
    date1_show.configure(bg="cadetblue2")

    label16=Label(preview_frame,text="Service Type :")
    label16.grid(row=12,column=0,padx=40,pady=5,sticky=W)
    label16.configure(bg="cadetblue2")
    service_type_show=Label(preview_frame,text=service_type_select.get())
    service_type_show.grid(row=12,column=1,padx=5,pady=5,sticky=W)
    service_type_show.configure(bg="cadetblue2")

    label17=Label(preview_frame,text="Service Engineer Name :",)
    label17.grid(row=13,column=0,padx=40,pady=5,sticky=W)
    label17.configure(bg="cadetblue2")
    se_name_show=Label(preview_frame,text=se_name.get())
    se_name_show.grid(row=13,column=1,padx=5,pady=5,sticky=W)
    se_name_show.configure(bg="cadetblue2")

    confirm_button=Button(preview_frame,text="Confirm",width=15,height=2,command=insert)
    confirm_button.grid(row=14,column=1,pady=5,padx=5,sticky=E)
    confirm_button.configure(bg="cadetblue3")

def new_customer():
    global nc
    nc=Tk()
    nc.title("NEW CUSTOMER BAR")
    nc.iconbitmap("./lf2.ico")
    #nc.geometry("900x700")
    nc.state('zoomed')
    #nc.resizable(FALSE,FALSE) 

    global id_num
    global id_num_label
    id_num=Entry(nc,width=30)
    id_num.grid(row=0,column=1,padx=20,pady=20,sticky=W)
    id_num_label=Label(nc,text="ID Number :")
    id_num_label.grid(row=0,column=0,padx=20,pady=20,sticky=W)
    
    global f_name
    global f_name_labe
    f_name=Entry(nc,width=30)
    f_name.grid(row=1,column=1,padx=20,pady=(10,0),sticky=W)
    f_name_labe=Label(nc,text="First Name :")
    f_name_labe.grid(row=1,column=0,padx=20,pady=(10,0),sticky=W,columnspan=4)

    global l_name 
    global l_name_label
    l_name=Entry(nc,width=30)
    l_name.grid(row=1,column=3,padx=20,pady=(10,0),sticky=W)
    l_name_label=Label(nc,text="Last Name :")
    l_name_label.grid(row=1,column=2,padx=20,pady=(10,0),sticky=W)

    global root
    global root_label
    root=Entry(nc,width=30)
    root.grid(row=2,column=1,padx=20,pady=20,sticky=W)
    root_label=Label(nc,text="Root :")
    root_label.grid(row=2,column=0,padx=20,pady=20,sticky=W)

    global address1
    global address1_label
    address1=Entry(nc,width=50)
    address1.grid(row=3,column=1,padx=20,pady=10,sticky=W)
    address1_label=Label(nc,text="Address line 1 :")
    address1_label.grid(row=3,column=0,padx=20,pady=10,sticky=W)

    global address2
    global address2_label
    address2=Entry(nc,width=50)
    address2.grid(row=4,column=1,padx=20,pady=20,sticky=W)
    address2_label=Label(nc,text="Address line 2 :")
    address2_label.grid(row=4,column=0,padx=20,pady=10,sticky=W)

    global district
    global district_label
    district=Entry(nc,width=30)
    district.grid(row=5,column=1,padx=20,pady=20,sticky=W)
    district_label=Label(nc,text="District :")
    district_label.grid(row=5,column=0,padx=20,pady=10,sticky=W)

    global state
    global state_label
    state=Entry(nc,width=40)
    state.grid(row=6,column=1,padx=20,pady=20,sticky=W)
    state.insert(0,"TAMILNADU")
    state_label=Label(nc,text="State :")
    state_label.grid(row=6,column=0,padx=20,pady=10,sticky=W)

    global pincode
    global pincode_label
    pincode=Entry(nc,width=30)
    pincode.grid(row=7,column=1,padx=20,pady=20,sticky=W)
    pincode_label=Label(nc,text="Pincode")
    pincode_label.grid(row=7,column=0,padx=20,pady=10,sticky=W)

    global mobile1
    global mobile_label1
    mobile1=Entry(nc,width=40)
    mobile1.grid(row=8,column=1,padx=20,pady=20,sticky=W)
    mobile_label1=Label(nc,text="Mobile 1 :")
    mobile_label1.grid(row=8,column=0,padx=20,pady=10,sticky=W)

    global mobile2
    global mobile_label2
    mobile2=Entry(nc,width=40)
    mobile2.grid(row=8,column=3,padx=20,pady=20,sticky=W)
    mobile_label2=Label(nc,text="Mobile 2 :")
    mobile_label2.grid(row=8,column=2,padx=20,pady=10,sticky=W)

    global telephone
    global telephone_label
    telephone=Entry(nc,width=40)
    telephone.grid(row=9,column=1,padx=20,pady=10,sticky=W)
    telephone_label=Label(nc,text="Telephone :")
    telephone_label.grid(row=9,column=0,padx=20,pady=10,sticky=W)

    global warrenty_frame
    warrenty_frame=LabelFrame(nc,text="Warrenty Period",padx=20,pady=20)
    warrenty_frame.grid(row=10,column=1,padx=20,pady=10)

    global warrenty_from
    global warrenty_from_label
    warrenty_from=DateEntry(warrenty_frame,locale='en_US',date_pattern='dd/MM/yyyy',width=30,bg="darkblue",fg="white",year=yr1)
    warrenty_from.grid(row=10,column=1)
    warrenty_from_label=Label(warrenty_frame,text="From :")
    warrenty_from_label.grid(row=10,column=0)

    global warrenty_to
    global warrenty_to_label
    warrenty_to=DateEntry(warrenty_frame,locale='en_US',date_pattern='dd/MM/yyyy',width=30,bg="darkblue",fg="white",year=yr1+1)
    warrenty_to.grid(row=10,column=3)
    warrenty_to_label=Label(warrenty_frame,text="To :")
    warrenty_to_label.grid(row=10,column=2)

    global model
    global model_label
    model=Entry(nc,width=40)
    model.grid(row=11,column=1,padx=20,pady=10,sticky=W)
    model_label=Label(nc,text="Model :")
    model_label.grid(row=11,column=0,padx=20,pady=10,sticky=W)

    global date1
    global date1_label
    date1=DateEntry(nc,locale='en_US',date_pattern='dd/MM/yyyy',width=30,bg="darkblue",fg="white",year=yr1)
    date1.grid(row=12,column=1,padx=20,pady=10,sticky=W)
    date1_label=Label(nc,text="Date Of Installation :")
    date1_label.grid(row=12,column=0,padx=20,pady=10,sticky=W)

    global service_type
    global service_type_select
    service_options=["60 Days","90 Days"]
    service_type=Label(nc,text="Type Of Service :")
    service_type.grid(row=13,column=0,padx=20,pady=10,sticky=W)
    clicked=StringVar()
    clicked.set("Type Of Service")
    service_type_select=ttk.Combobox(nc,values=service_options)
    service_type_select.current(1)
    service_type_select.bind("<<CoomboboxSelected>>")
    service_type_select.grid(row=13,column=1,padx=20,pady=10,sticky=W)
    
    global se_name
    global se_name_label
    se_name=Entry(nc,width=30,border=5)
    se_name.grid(row=14,column=1,padx=20,pady=10,sticky=W)
    se_name_label=Label(nc,text="Service Engineer Name :")
    se_name_label.grid(row=14,column=0,padx=20,pady=10,sticky=W)

    global save_button
    save_button=Button(nc,text="save",command=preview)
    save_button.grid(row=15,column=2)

'''def enter_service(id):
    val1=visite_date_entry.get()
    val2=work_details_text.get(1.0,END)
    val3=parts_replaced_entry.get()
    val4=amount_charged_entry.get()
    val5=feed_water_entry.get()
    val6=pure_water_entry.get()
    val7=serviced_by_entry.get()
    val8=notes_entry.get()
    sql_command=f"INSERT INTO `{id}`(visit_date,work_details,parts_replaced,amount_charged,feed_water,pure_water,serviced_by,notes) VALUES({val1},{val2},{val3},{val4},{val5},{val6},{val7},{val8})"
    my_cursor1.execute(sql_command, )
    mydb1.commit()
    service_window.destroy()
    print(id,val1,val2,val3,val4,val5,val6,val7,val8)'''

def enter_service(id):
    sql_command=f"INSERT INTO `{id}`(visit_date,work_details,parts_replaced,amount_charged,feed_water,pure_water,serviced_by,notes)"+" VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(visite_date_entry.get(),work_details_text.get(1.0,END),parts_replaced_entry.get(),amount_charged_entry.get(),feed_water_entry.get(),pure_water_entry.get(),serviced_by_entry.get(),notes_entry.get())
    my_cursor1.execute(sql_command,values)
    mydb1.commit()
    print(id)
    service_window.destroy()

def compliant(id):
    return

def customer_service(id):
    global service_window
    service_window=Tk()
    service_window.title("NEW CUSTOMER BAR")
    service_window.iconbitmap("./lf2.ico")
    service_window.geometry("900x700")
    service_window.state('zoomed')
    service_window.resizable(FALSE,FALSE)

    sql="SELECT *FROM all_customers WHERE id_number= %s"
    idnum1=(id,)
    my_cursor.execute(sql,idnum1)
    result=my_cursor.fetchall()

    customer_detail=ttk.Labelframe(service_window,text="Customer Details",labelanchor=N,cursor='rtl_logo')
    customer_detail.grid(row=0,column=0,columnspan=2)

    customer_i_label=Label(customer_detail,text="Id :"+result[0][0])
    customer_i_label.grid(row=0,column=0,sticky=W)
    customer_n_label=Label(customer_detail,text="Name :"+result[0][1]+' '+result[0][2])
    customer_n_label.grid(row=1,column=0,sticky=W)
    customer_r_label=Label(customer_detail,text="Root :"+result[0][3])
    customer_r_label.grid(row=2,column=0,sticky=W)
    
    global visite_date_entry
    visite_date_label=Label(service_window,text="Visite Date :")
    visite_date_label.grid(row=2,column=0,padx=40,pady=20,sticky=W)
    visite_date_entry=DateEntry(service_window,locale='en_US',date_pattern='dd/MM/yyyy',width=30,bg="darkblue",fg="white",year=yr1)
    visite_date_entry.grid(row=2,column=1,padx=40,pady=20,sticky=W)

    global work_details_text
    work_details_label=Label(service_window,text="Work Details :")
    work_details_label.grid(row=3,column=0,padx=40,pady=10,sticky=W)
    work_details_text=Text(service_window, width=30, height=3)
    work_details_text.grid(column=1, row=3)
    '''work_details_entry=Entry(service_window,width=30)
    work_details_entry.grid(row=3,column=1,padx=40,pady=10,sticky=W)''' 

    global parts_replaced_entry
    parts_replaced_label=Label(service_window,text="Parts Replaced :")
    parts_replaced_label.grid(row=4,column=0,padx=40,pady=10,sticky=W)
    parts_replaced_entry=Entry(service_window,width=30)
    parts_replaced_entry.grid(row=4,column=1,padx=40,pady=10,sticky=W)

    global amount_charged_entry
    amount_charged_label=Label(service_window,text="Amount Charged :")
    amount_charged_label.grid(row=5,column=0,padx=40,pady=10,sticky=W)
    amount_charged_entry=Entry(service_window,width=30)
    amount_charged_entry.grid(row=5,column=1,padx=40,pady=10,sticky=W)
    
    global feed_water_entry
    feed_water_label=Label(service_window,text="Feed Water :")
    feed_water_label.grid(row=6,column=0,padx=40,pady=10,sticky=W)
    feed_water_entry=Entry(service_window,width=30)
    feed_water_entry.grid(row=6,column=1,padx=40,pady=10,sticky=W)
    
    global pure_water_entry
    pure_water_label=Label(service_window,text="Pure Water :")
    pure_water_label.grid(row=7,column=0,padx=40,pady=10,sticky=W)
    pure_water_entry=Entry(service_window,width=30)
    pure_water_entry.grid(row=7,column=1,padx=40,pady=10,sticky=W)
    
    global serviced_by_entry
    serviced_by_label=Label(service_window,text="Serviced By :")
    serviced_by_label.grid(row=8,column=0,padx=40,pady=10,sticky=W)
    serviced_by_entry=Entry(service_window,width=30)
    serviced_by_entry.grid(row=8,column=1,padx=40,pady=10,sticky=W)

    global notes_entry
    notes_label=Label(service_window,text="Notes :")
    notes_label.grid(row=9,column=0,padx=40,pady=10,sticky=W)
    notes_entry=Entry(service_window,width=30)
    notes_entry.grid(row=9,column=1,padx=40,pady=10,sticky=W)

    entry_button=Button(service_window,text="Confirm Service",cursor='plus',command=lambda:enter_service(id))
    entry_button.grid(row=10,column=1)

    #list customer
def list_customer():
    list_customer_query=Tk()
    list_customer_query.title("LIFEFINE CUSTOMER DATA")
    list_customer_query.iconbitmap("./lf2.ico")
    list_customer_query.geometry("800x600")
    list_customer_query.configure(bg="beige")
    list_customer_query.state('zoomed')

    '''my_cursor.execute("SELECT * FROM all_customers")
    result=my_cursor.fetchall()'''

    main_frame=Frame(list_customer_query)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_scrollbar.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    global second_frame
    second_frame=Frame(my_canvas)

    my_canvas.create_window((0,0),window=second_frame,anchor="nw")

    def initial():
        global drop
        global search_entry
        drop=ttk.Combobox(second_frame,values=["All","Place","Customer ID","Root"])
        drop.current(0)
        drop.grid(row=0,column=1,padx=40,pady=40)
        search_entry=Entry(second_frame,width=40)
        search_entry.grid(row=0,column=2,padx=20,pady=40)
    def find():
        selected=drop.get()
        selected2=search_entry.get()
        sql=""
        if selected=="All":
            sql="SELECT * FROM all_customers ORDER BY id_number ASC"
            my_cursor.execute(sql)
            result=my_cursor.fetchall()

        elif selected=="Place":
            sql="SELECT *FROM all_customers WHERE address_2= %s ORDER BY id_number ASC"
            name=(selected2,)
            my_cursor.execute(sql,name)
            result=my_cursor.fetchall()
        
        elif selected=="Customer ID":
            sql="SELECT *FROM all_customers WHERE id_number= %s ORDER BY id_number ASC"
            name=(selected2,)
            my_cursor.execute(sql,name)
            result=my_cursor.fetchall()    
        
        elif selected=="Root":
            sql="SELECT *FROM all_customers WHERE root= %s ORDER BY id_number ASC"
            name=(selected2,)
            my_cursor.execute(sql,name)
            result=my_cursor.fetchall()

        for index,x in enumerate(result):
            
            lookup_frame=LabelFrame(second_frame,text=x[0],pady=10,padx=100)
            lookup_frame.grid(row=index+1,column=2,pady=10,padx=60,sticky=W,columnspan=3)
            
            id_referance=str(x[0])
            service=Button(lookup_frame,text="Service",command=lambda id_referance=id_referance: customer_service(id_referance))
            service.grid(row=index+1,column=0,padx=20,sticky=W)

            compliant_button=Button(lookup_frame,text="Compliant",command=lambda id_referance=id_referance: compliant(id_referance))
            compliant_button.grid(row=index+1,column=1,padx=20,sticky=W)

            lookup_label=Label(lookup_frame,text="Name :")
            lookup_label.grid(row=index,column=0,padx=20)
            
            lookup_label=Label(lookup_frame,text=x[1]+' '+x[2])
            lookup_label.grid(row=index,column=1,sticky=W)
            
            lookup_label=Label(lookup_frame,text="Root :")
            lookup_label.grid(row=index,column=2,padx=20)
            
            lookup_label=Label(lookup_frame,text=x[3])
            lookup_label.grid(row=index,column=3,sticky=W)
            
            lookup_label=Label(lookup_frame,text="Address :")
            lookup_label.grid(row=index,column=4,pady=5,ipadx=20,sticky=W)
            
            lookup_label=Label(lookup_frame,text=x[4]+"\n"+x[5]+"\n"+x[6]+"\n"+x[8],relief=GROOVE,justify=LEFT)
            lookup_label.grid(row=index,column=5,pady=5,sticky=W)
            
            lookup_label=Label(lookup_frame,text="CONTACT :")
            lookup_label.grid(row=index,column=6,pady=5,sticky=W)
            
            lookup_label=Label(lookup_frame,text=x[9]+"\n"+x[10]+"\n"+x[11],relief=GROOVE,justify=LEFT)
            lookup_label.grid(row=index,column=7,pady=5,sticky=W)
    
    initial()
    Button(second_frame,text="Search",command=find).grid(row=0,column=3)

    #csv_button=Button(list_customer_query,text="save to excel",command=lambda: write_to_csv(result))
    #csv_button.grid(row=index+1,column=0)

button1=Button(main,text="CUSTOMER LIST",width=20,height=2,command=list_customer)
button1.grid(row=1,column=1,padx=100,pady=40,columnspan=1)

button2=Button(main,text="NEW CUSTOMER",width=20,height=2,command=new_customer)
button2.grid(row=1,column=2,padx=100,pady=40,columnspan=1)

button3=Button(main,text="COMPLIANTS",width=20,height=2)
button3.grid(row=1,column=3,padx=100,pady=40,columnspan=1)

main.mainloop()