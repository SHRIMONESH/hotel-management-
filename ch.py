import csv
from datetime import datetime 
class Customer_details():
    def cust_details(self):
        
        
        self.y=[]
        self.name=input("Enter Customer name : ")
        self.y.append(self.name.upper())
        while True:
            try:
                self.ph_no=(input("Enter phone number : "))
                    
                
                
                if (len(self.ph_no)!=10 ):
                    raise ValueError("Please enter 10 digit phone  number!!")
                break
            except ValueError as e:
                print(e)
        self.y.append(int(self.ph_no))
                
        while True:
            try:
                self.id_proof=(input("Enter Aadhar Number : "))
                
                if len(self.id_proof)!=12:
                    raise ValueError("Please enter 12 digit Aadhar   number!!")
                break
            except ValueError as e:
                print(e)
        self.y.append(int(self.id_proof))
        
        

        
        self.add=input("Enter Address : ")
        self.y .append(self.add)
        self.no_of_members=int(input("Enter total members : "))
        self.y .append(self.no_of_members)
        
        return self.y

class Booking_record(Customer_details):
    

    def booking_recd(self):
        self.ar=self.cust_details()
        
        print("TYPE:1 EXCUTIVE ROOM 12000RS  ")
        print("TYPE:2 DELUXE ROOM 9000Rs ")
        print("TYPE:3 SUITE ROOM 7000Rs")
        print("TYPE:4 STANDARD ROOM 5000Rs")
        
        while True:
            try:
                self.typ_room=int(input("Enter the room no type: "))
                if self.typ_room<=0 or self.typ_room>4:
                    raise ValueError("Please enter a proper room type number!!")
                if self.typ_room==1:
                    self.b_amt=12000
                if self.typ_room==2:
                    self.b_amt=9000
                if self.typ_room==3:
                    self.b_amt=7000
                if self.typ_room==4:
                    self.b_amt=5000
                
                break
            except ValueError as e:
                print(e)

        
        
        self.no=int(input("Enter no of rooms needed : "))
        self.ar.append(self.b_amt * self.no )
        
        self.time=int(input("Enter Check in hour : "))
             
        self.ar.append(self.time)
        
        
        while True:
            try:
                self._in=(input("Enter Chech In Date : "))
                self._out=(input("Enter Check Out Date: "))
                self.ch_in = datetime.strptime(self._in, "%Y-%m-%d") 
                self.ch_out= datetime.strptime(self._out, "%Y-%m-%d")
                if self.ch_in >self.ch_out:
                    raise ValueError("Please Enter a proper date ")
                
                break
            
                
            except ValueError as e:
                print(e)
        self.ar.append(self.ch_in)
        self.ar.append(self.ch_out)
        self.r=(self.ch_out - self.ch_in)
        self.rs = self.r.days
        self.ar.append(self.rs)
        self.ar.append(self.rs*self.b_amt*self.no)
            
            
        return self.ar
class Restaurant_Bill(Booking_record):
    def res(self,name,id_proof):
        self.name=name
        self.id_proof=id_proof
        
        
        
        print("             Breakfast" )
        print("1.Breakfast_Non Veg Combo ","           Rs200")
        print("2.Breakfast_Veg Combo ","               Rs180")
        print("")
        print("             Lunch")
        print("3.Lunch_Non Veg Combo ","           Rs300")
        print("4.Lunch_Veg Combo ","               Rs250")
        print(" ")
        print("             Dinner")
        print("5.Dinner_NonVeg_Combo         Rs250")
        print("6.Dinner_Veg_Combo            Rs150")
        self.tot=0
        self.n=int(input("Enter total members : "))
        self.total=0
        for self.i in range(self.n):
            while True:
                try:
                    self.Breakfast=int(input("Enter the Breakfast type no : "))
                    self.Lunch=int(input("Enter the Lunch type no : "))
                    self.Dinner=int(input("Enter the Dinner type no : "))
                
                    if self.Breakfast<1 or self.Breakfast>2:
                        raise ValueError("Please enter a proper Breakfast type number !!")
                    if self.Breakfast==1:
                        self.tot=200+self.tot
                    if self.Breakfast==2:
                        self.tot=180+self.tot
                    if self.Lunch<3 or self.Lunch>4:
                        raise ValueError("Please enter a proper Lunch type number !!")
                    if self.Lunch==3:
                        self.tot=300+self.tot
                    if self.Lunch==4:
                        self.tot=250+self.tot
                    if self.Dinner<5 or self.Dinner>6:
                        raise ValueError("Please enter a proper Dinner type number !!")
                    if self.Breakfast==5:
                        self.tot=250+self.tot
                    if self.Breakfast==6:
                        self.tot=150+self.tot
                
                    break
                except ValueError as e:
                    print(e)
            self.total=self.total+self.tot

        add(self.name,self.id_proof,self.total)
            
            
class Display_Customer_Details(Customer_details):
    
    def display_cust(self):
        self.name=input("Enter the name to find the details : ")
        self.idproof=(input("Enter id proof : "))
        search_records(self.name,self.idproof)
        
class Room_Rent(Booking_record):
    def room_rent(self):
        self.name=input("Enter the name of the customer to show Roon rent : ")
        while True:
            try:
                self.id_proof=input("Enter the id Proof number of the customer : ")
                
                if len(self.id_proof)!=12:
                    raise ValueError("Please enter 12 digit Aadhar   number!!")
                break
            except ValueError as e:
                print(e)
        with open('chk.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if  (self.name.upper() in row):
                    if (self.id_proof in row):
                        return row[10]
                
        csvfile.close()           

class Total_Bill():
    def tot_bill(self):
        self.name=input("Enter the name of the customer to show the total bill  : ")
        while True:
            try:
                self.id_proof=input("Enter the id Proof number of the customer : ")
                
                if len(self.id_proof)!=12:
                    raise ValueError("Please enter 12 digit Aadhar   number!!")
                break
            except ValueError as e:
                print(e)
        with open('chk.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if  (self.name.upper() in row):
                    if (self.id_proof in row):
                        self.total=int(row[10])+int(row[11])*int(row[9])
            
            return self.total 
        csvfile.close()
        

        

    
        

    
def create_record(data):
    with open('chk.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def read_records():
    with open('chk.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def search_records(search_name,search_id):
    with open('chk.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if  (search_name in row):
                if (search_id in row):
                    print(row)
        
def add(name,id_proof,total):
    with open('chk.csv', 'r') as csvfile ,open('temp.csv', 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        for row in reader:
            if  (name in row):
                if (id_proof in row):        
                    row.append(total)
                    writer.writerow(row)
            if (name not in row ):
                    writer.writerow(row)
    csvfile.close()
    outfile.close()
    
    import os
    os.remove('chk.csv')
    os.rename('temp.csv','chk.csv' )


con="Y"
print("\t\t\t!!!WELCOME TO HOTEL TAJ!!!\n")

while con=="Y" or con=="y":
    print("STAFF MENU \n")
    print("Enter choice 1 to enter Customer details and Booking record  ")
    print("Enter choice 2 to Order Food ")
    print("Enter choice 3 to Display Customer details for the particular details ")
    print("Enter choice 4 to see the room rent for the particular Customer")
    print("Enter choice 5 to Display Total Bill for the particular Customer")
    ch=int(input("Enter choice : "))
    if ch==1:
        while True:
            try:
                n=int(input("Enter no of details need to enter : "))
                if float(n) is False  :
                    raise ValueError("Please enter number ")
                
                break
            except ValueError as e:
                print(e)
        for i in range(n):
            b=Booking_record()
    
            create_record(b.booking_recd())   
        read_records()
    
    if ch==2:
        read_records()
        name=input("Enter the name of the customer to order Food : ")
        while True:
            try:
                id_proof=input("Enter the id Proof of the customer to order Food : ")
                
                if len(id_proof)!=12:
                    raise ValueError("Please enter 12 digit Aadhar   number!!")
                break
            except ValueError as e:
                print(e)
        f=Restaurant_Bill()
        f.res(name,id_proof) 
        
    if ch==3:
        read_records()
        d=Display_Customer_Details()
        d.display_cust()
    
    if ch==4:
        r=Room_Rent()
        print("Room rent for the selected customer is Rs " , r.room_rent())
    
    if ch==5:
        t=Total_Bill()
        print("Total Bill for the selected Customer is Rs",t.tot_bill())
        
        
    con=input("Do u want to run the application then press  Y : ")
print("\t\t\tTHANKYOU FOR USING !!!")   