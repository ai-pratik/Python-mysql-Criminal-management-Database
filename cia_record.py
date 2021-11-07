from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector #pip install mysql-connector-python
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Pratik@5151"
)



class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CIA Bluecore')

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupution = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()





        lbl_title=Label(self.root,text='Criminal Investigation Agency,Bluecore',font=('Asap',40,'bold'),bg='black',fg='skyblue')
        lbl_title.place(x=0,y=0,width=1530,height=70)
        #logo placing
        img_logo=Image.open('Images/cialogo.png')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        #Img_frame
        img_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        #image1
        img1 = Image.open('Images/cialogo.png')
        img1 = img1.resize((350, 150), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img1 = Label(img_frame, image=self.photo1)
        self.img1.place(x=0, y=0, width=350, height=150)

        # image2
        img2 = Image.open('Images/cialogo.png')
        img2 = img2.resize((250, 200), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img2 = Label(img_frame, image=self.photo2)
        self.img2.place(x=400, y=0, width=540, height=160)

        # image3
        img3 = Image.open('Images/cialogo.png')
        img3 = img3.resize((250, 200), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img3 = Label(img_frame, image=self.photo3)
        self.img3.place(x=800, y=0, width=540, height=160)

        #Main Frame
        Main_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_Frame.place(x=10,y=200,width=1425,height=560)

        #upper frame
        Upper_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE,text='Criminal Information',font=('Asap',11,'bold'),fg='Orange',bg='White')
        Upper_Frame.place(x=10, y=10, width=1400, height=270)

        #Labels Entry

        #case id
        caseid=Label(Upper_Frame,text='Case ID:',font=('Asap', 11, 'bold'),fg='skyblue', bg='White')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        case_entry=ttk.Entry(Upper_Frame,textvariable=self.var_case_id,width=22,font=('Asap', 11, 'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal No

        lbl_criminal_no = Label(Upper_Frame, text='Criminal No:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_criminal_no.grid(row=0, column=2, padx=2,pady=7 ,sticky=W)

        txt_criminal_no = ttk.Entry(Upper_Frame,textvariable=self.var_criminal_no, width=22, font=('Asap', 11, 'bold'))
        txt_criminal_no.grid(row=0, column=3, padx=2,pady=7 ,sticky=W)

        # Criminal Name

        lbl_criminal_name = Label(Upper_Frame, text='Criminal Name:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_criminal_name.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_criminal_name = ttk.Entry(Upper_Frame,textvariable=self.var_name, width=22, font=('Asap', 11, 'bold'))
        txt_criminal_name.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # NickName

        lbl_Nick_name = Label(Upper_Frame, text='Nick-Name:', font=('Asap', 11, 'bold'), fg='skyblue',bg='White')
        lbl_Nick_name.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_Nick_name = ttk.Entry(Upper_Frame,textvariable=self.var_nickname, width=22, font=('Asap', 11, 'bold'))
        txt_Nick_name.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # date of arrest

        lbl_DOA = Label(Upper_Frame, text='Date Of Arrest:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_DOA.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_DOA = ttk.Entry(Upper_Frame,textvariable=self.var_arrest_date, width=22, font=('Asap', 11, 'bold'))
        txt_DOA.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Date Of Crime

        lbl_DOC = Label(Upper_Frame, text='Date Of Crime:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_DOC.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_DOC = ttk.Entry(Upper_Frame,textvariable=self.var_date_of_crime, width=22, font=('Asap', 11, 'bold'))
        txt_DOC.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Address

        lbl_Address = Label(Upper_Frame, text='Address:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_Address.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_Address = ttk.Entry(Upper_Frame, textvariable=self.var_address,width=22, font=('Asap', 11, 'bold'))
        txt_Address.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        #Age

        lbl_age = Label(Upper_Frame, text='Age:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_age.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_age = ttk.Entry(Upper_Frame, textvariable=self.var_age,width=22, font=('Asap', 11, 'bold'))
        txt_age.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Occupution

        lbl_Occupution = Label(Upper_Frame, text='Occupution:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_Occupution.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_Occupution = ttk.Entry(Upper_Frame,textvariable= self.var_occupution,width=22, font=('Asap', 11, 'bold'))
        txt_Occupution.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # birthmark

        lbl_birthmark = Label(Upper_Frame, text='Birthmark:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_birthmark.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        txt_birthmark = ttk.Entry(Upper_Frame, textvariable=self.var_birthmark,width=22, font=('Asap', 11, 'bold'))
        txt_birthmark.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # Crime Type

        lbl_Crime_Type = Label(Upper_Frame, text='Crime Type:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_Crime_Type.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        txt_Crime_Type = ttk.Entry(Upper_Frame,textvariable= self.var_crime_type,width=22, font=('Asap', 11, 'bold'))
        txt_Crime_Type.grid(row=0, column=5, padx=2, pady=7, sticky=W)

        # Father Name

        lbl_FatherName = Label(Upper_Frame, text='Father Name:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_FatherName.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        txt_FatherName = ttk.Entry(Upper_Frame,textvariable= self.var_father_name,width=22, font=('Asap', 11, 'bold'))
        txt_FatherName.grid(row=1, column=5, padx=2, pady=7, sticky=W)

        #Gender

        lbl_Gender = Label(Upper_Frame, text='Gender:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        lbl_Gender.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        #wanted

        #lbl_wanted = Label(Upper_Frame, text='Wanted:', font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        #lbl_wanted.grid(row=3, column=4, padx=2, pady=7, sticky=W)

        #radio Button gender
        radio_frame_gender=Frame(Upper_Frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=610,y=80,width=190,height=25)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')

        female = Radiobutton(radio_frame_gender,variable=self.var_gender, text='Female', value='female', font=('Asap', 11, 'bold'), fg='skyblue',bg='White')
        female.grid(row=0, column=1, pady=2, padx=5, sticky=W)
        # wanted Button gender
        #radio_frame_wanted = Frame(Upper_Frame, bd=2, relief=RIDGE, bg='white')
        #radio_frame_wanted.place(x=610, y=120, width=190, height=25)


        #yes=Radiobutton(radio_frame_wanted,text='Yes',value='yes',font=('Asap', 11, 'bold'), fg='skyblue', bg='White')
        #yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        #no = Radiobutton(radio_frame_wanted, text='No', value='no', font=('Asap', 11, 'bold'), fg='skyblue',bg='White')
        #no.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        #Buttons
        button_frame= Frame(Upper_Frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        #add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('Asap', 18, 'bold'),width=14,bg='skyblue',fg='pink')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        # Update button
        btn_update = Button(button_frame,command=self.update_data, text='Update', font=('Asap', 18, 'bold'), width=14, bg='skyblue', fg='pink')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # Delete button
        btn_delete = Button(button_frame,command=self.delete_data, text='Delete', font=('Asap', 18, 'bold'), width=14, bg='skyblue', fg='pink')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # Clear button
        btn_Clear = Button(button_frame,command=self.clear_data, text='Clear', font=('Asap', 18, 'bold'), width=14, bg='skyblue', fg='pink')
        btn_Clear.grid(row=0, column=3, padx=3, pady=5)

        #bg_right-side imag
        right_side = Image.open('Images/cialogo.png')
        right_side = right_side.resize((450, 235), Image.ANTIALIAS)
        self.right_side = ImageTk.PhotoImage(right_side)

        self.right_side = Label(Upper_Frame, image=self.photo2)
        self.right_side.place(x=1000, y=0, width=470, height=250)

        #down frame
        down_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Info Table', font=('Asap', 11, 'bold'),fg='Orange', bg='White')
        down_Frame.place(x=10, y=280, width=1400, height=270)


        #Search frame
        search_Frame = LabelFrame(down_Frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=('Asap', 11, 'bold'),fg='Orange', bg='White')
        search_Frame.place(x=0, y=0, width=1395, height=60)


        lbl_searchby = Label(search_Frame, text='Search By:', font=('Asap', 11, 'bold'), fg='white', bg='red')
        lbl_searchby.grid(row=0, column=0, padx=2, pady=7, sticky=W)


        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_Frame,textvariable=self.var_com_search,font=('Asap', 11, 'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        self.var_search=StringVar()
        txt_search_entry = ttk.Entry(search_Frame,textvariable=self.var_search, width=18, font=('Asap', 11, 'bold'))
        txt_search_entry.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        # search button
        btn_search = Button(search_Frame,command=self.search_data, text='Search', font=('Asap', 18, 'bold'), width=14, bg='skyblue', fg='pink')
        btn_search.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # all button
        btn_all = Button(search_Frame,command=self.fetch_data,text='Show All', font=('Asap', 18, 'bold'), width=14, bg='skyblue', fg='pink')
        btn_all.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        #SECOND TITLE
        lbl_secondtitle = Label(search_Frame, text='Bluecore Creative Share', font=('Asap', 30, 'bold'), fg='orange', bg='yellow')
        lbl_secondtitle.grid(row=0, column=5, padx=12, pady=0, sticky=W)

        #table frame

        table_frame=Frame(down_Frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1395,height=170)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #treeview
        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='CriminalName')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5', text='ArrestDate')
        self.criminal_table.heading('6', text='CrimeofDate')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupution')
        self.criminal_table.heading('10', text='BirthMark')
        self.criminal_table.heading('11', text='CrimeType')
        self.criminal_table.heading('12', text='FatherName')
        self.criminal_table.heading('13', text='Gender')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)



        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #add function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required!!')
        else:
            try:
                connect=mysql.connector.connect(host='localhost',username='root',password='Pratik@5151',database='crime_managment')
                my_cursor=connect.cursor()
                my_cursor.execute('insert into criminal_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupution.get(),
                    self.var_birthmark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get()                              ))
                connect.commit()
                self.fetch_data()
                self.clear_data()
                connect.close()
                messagebox.showinfo('Sucess!','Criminal Record Has Been Added!')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

#fetch data
    def fetch_data(self):
        connect = mysql.connector.connect(host='localhost', username='root', password='Pratik@5151',
                                          database='crime_managment')
        my_cursor = connect.cursor()
        my_cursor.execute('select * from criminal_management')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            connect.commit()
        connect.close()

#get cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupution.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])


#update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required!!')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this record')
                if update>0:
                    connect = mysql.connector.connect(host='localhost', username='root', password='Pratik@5151',
                                              database='crime_managment')
                    my_cursor = connect.cursor()
                    my_cursor.execute('update criminal_management set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupution=%s,Birthmark=%s,crimeType=%s,fatherName=%s,gender=%s where Case_id=%s',(
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupution.get(),
                        self.var_birthmark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_case_id.get()

                                                ))
                else:
                    if not update:
                        return
                connect.commit()
                self.fetch_data()
                self.clear_data()
                connect.close()
                messagebox.showinfo('Sucess','Criminal record Sucessfully Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

#delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required!!')
        else:
            try:
                delete = messagebox.askyesno('Update', 'Are you sure Delete this record')
                if delete > 0:

                    connect = mysql.connector.connect(host='localhost', username='root', password='Pratik@5151',
                                                  database='crime_managment')
                    my_cursor = connect.cursor()
                    sql='delete from criminal_management where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)

                else:
                    if not delete:
                        return
                connect.commit()
                self.fetch_data()
                self.clear_data()
                connect.close()
                messagebox.showinfo('Sucess', 'Criminal record Sucessfully Deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')

    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupution.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                connect = mysql.connector.connect(host='localhost', username='root', password='Pratik@5151',
                                                  database='crime_managment')
                my_cursor = connect.cursor()
                my_cursor.execute('select * from criminal_management where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                    connect.commit()
                connect.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')





































if __name__ == '__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()#we have to keep window at that position unless we stop that


