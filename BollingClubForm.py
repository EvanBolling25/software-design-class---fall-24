import tkinter
from tkinter import ttk

class ClubFrame(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent,padding = "10 10 10 10")
        self.pack(fill="both",expand = True)
        personal_frame = tkinter.LabelFrame(root, text = "Personal Information")
        shirt_frame = tkinter.LabelFrame(root, text = "Club Dues and T-shirt size")
        confirmation_frame = tkinter.LabelFrame(root, text = "Confirmation")

        #organzing the frames so they show up
        personal_frame.pack()
        shirt_frame.pack()
        confirmation_frame.pack()
        
        #setting variables to get used later in fuctions
        self.name_var=tkinter.StringVar()
        self.email=tkinter.StringVar()
        self.year= tkinter.StringVar()
        self.student_var=tkinter.StringVar(value="yes")
        self.tshirt_var= tkinter.StringVar()
        self.quantity_var= tkinter.IntVar()

        #personal frame items/widgets (varibles arnt being used i know , theyre there for me to quickly find what is what)
        name_label = ttk.Label(personal_frame, text = "First and Last name:").grid(column=0, row=0)
        name_textbox =ttk.Entry(personal_frame, textvariable=self.name_var).grid(column=1, row=0,columnspan=2)
        email_label = ttk.Label(personal_frame, text ="Email Address:" ).grid(column=0, row=1)
        email_textbox = ttk.Entry(personal_frame,textvariable=self.email).grid(column=1, row=1)
        year_label =ttk.Label(personal_frame, text="Year").grid(column=0, row=3)
        year_combobox=ttk.Combobox(personal_frame, value = ["N/A","Freshman","Sophomore","Junior","Senior"],textvariable=self.year).grid(column=1, row=3)

        #checkboxes for student
        student_label =ttk.Label(personal_frame, text = "Are you a student?").grid(column=0, row=2)
        student_var=tkinter.IntVar()
        student_var.set(1)
        student_yes =ttk.Checkbutton(personal_frame, text = "yes",variable=student_var).grid(column=1,row=2)
        student_no =ttk.Checkbutton(personal_frame, text ="No").grid(column=3,row=2)

        #shirt frame items/widgets
        clubfee_label = ttk.Label(shirt_frame, text = "Club Fee").grid(column=0, row=0)
        #setting the default entry for the fee textbox
        self.fee=tkinter.StringVar()
        self.fee.set("$25")
        clubfee_textbox = ttk.Entry(shirt_frame,textvariable=self.fee, state="readonly").grid(column=1, row=0,)
        tshirt_label = ttk.Label(shirt_frame, text = "T-shirt Size").grid(column=0, row=1)
        tshirt_combobox = ttk.Combobox(shirt_frame, value = ["SM","M","L","XL","XXL"],textvariable=self.tshirt_var).grid(column=1, row=1)
        quanity_label=ttk.Label(shirt_frame, text="Quantity").grid(column=0,row=2,)
        quanity_spinbox=ttk.Spinbox(shirt_frame, from_=1, to= 10,textvariable=self.quantity_var).grid(column=1,row=2)
        

        #confirmation frame items/eidgets
        message_label=ttk.Label(confirmation_frame,text="Please verify that all info\nis correct before hitting submit")
        submit_button=ttk.Button(confirmation_frame,text="submit",)
        message_label.grid(column=0,row=0,padx=10,pady=10)
        submit_button = ttk.Button(confirmation_frame, text="Submit", command=self.save_data)
        submit_button.grid(column=1, row=0)

        #applies padding to each widget
        for child in self.winfo_children():
            child.grid_configure(padx=10,pady=10)


        #collects data from the form using the get method from each widget
    def collect_data(self):
        name = self.name_var.get()
        email = self.email.get()
        year = self.year.get()
        is_student = self.student_var.get()
        tshirt_size = self.tshirt_var.get()
        quantity =self.quantity_var.get()

        # Print to console 
        #print(f"Name: {name}, Email: {email}, Year: {year}, Student: {is_student}, T-Shirt Size: {tshirt_size}, Quantity: {quantity}")

        # returns data to be used in the next fuction
        return name, email, year, is_student, tshirt_size, quantity
        
    def write_to_file(self, name, email, year, is_student, tshirt_size, quantity):
        #Writes form data to a text file.
        try:
            with open("club_signup.txt", "a") as file:
                file.write("Club Signup Form Submission:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Email: {email}\n")
                file.write(f"Year: {year}\n")
                file.write(f"Student: {is_student}\n")
                file.write(f"T-Shirt Size: {tshirt_size}\n")
                file.write(f"Quantity: {quantity}\n")
                file.write("-" * 40 + "\n")
            print("Data successfully written to club_signup.txt")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")       

    def save_data(self):
        #runs the two previos funtions in one and is set to the submit button
        # Collect the data
        name, email, year, is_student, tshirt_size, quantity = self.collect_data()

        # Writes data to the file
        self.write_to_file(name, email, year, is_student, tshirt_size, quantity)
        
        #after it saves all the data, the window is closed 
        self.master.destroy()



if __name__ == "__main__":
 
    root = tkinter.Tk()
    
    root.title("Club Sign Up Form")
    
    ClubFrame(root)
    
    root.mainloop()