import mysql.connector as ms
import random as r

Con = ms.connect(host="localhost", user="root", password="sql@123", database="online_mb")
MCursor = Con.cursor()

def cus_week():
    MCursor.execute('''SELECT customer_name, SUM(price) AS total_purchase,count(*)
    FROM customer
    WHERE YEARWEEK(date) = YEARWEEK(NOW())
    GROUP BY customer_name
    ORDER BY Count(*) DESC
    LIMIT 1''')
    F=MCursor.fetchone()
    if F is not None:
        ol=F[0]
        return ol
    else:
        return None
def sc():
    MCursor.execute("SELECT * FROM customer")  
    customers = MCursor.fetchall()
    print("Serial   Date     Customer Name          Phone Number      Payment Type         Item Name     Discount    Final Amount")
    print("------  --------  --------------------    --------------    ------------         --------------------    --------    ---------------")
    for customer in customers:
                customer_id, customer_name, phone_number, payment_method, item_name, discount, final_amount , date = customer
                print(f"{customer_id:<8}{str(date):<15} {customer_name:<25} {phone_number:<18} {payment_method:<23} {item_name:<25} {discount:<11} {final_amount:<15}")
                    

def admin():
    MCursor.execute('SELECT * FROM Admin')
    User = MCursor.fetchall()
    max_tries = 3 

    for attempt in range(max_tries):
        u = input("Enter username: ").lower()
        p = int(input("Enter password: "))

        login_successful = False

        for i in User:
            if u == i[1] and p == i[2]:
                print('Login successful!')
                login_successful = True
                break
        if login_successful:
            break
        else:
            remaining_tries = max_tries - (attempt + 1)
            print(f'Invalid username or password. Tries remaining: {remaining_tries}')
            print('Or IF YOU WANT TO QUIT TYPE "1"')
            po=input()
            if po == '1':
                main()

            if remaining_tries == 0:
                    print('Maximum number of tries reached. Exiting..')
                    break   

    if login_successful:
        while True:
            if i[1] == 'san':
                print('Welcome Admin SanjeevD\nWhat Do You Want To Modify:')
            elif i[1] == 'mj':
                print('Welcome Admin ANSHUKMAN MJ\nWhat Do You Want To Modify:')
            elif i[1] == 'sus':
                print('Welcome Admin CNC SUSINDHARAN\nWhat Do You Want To Modify:')
            
            print('1) SmartPhone\n2) Accessories\n3) ShowReport\n4) Quit')
            a = int(input())

            if a == 1:
                print('Do You Want\n1) Update\n2) Delete\n3) Add Records\n4) Quit')
                b = int(input())
                if b == 1:
                            MCursor.execute("SELECT * FROM smartphones")  
                            mobiles = MCursor.fetchall()
                            print("Serial Mobile Name       Brand                RAM   Camera Storage Color     OS   Price")
                            print("------ -------------------- -------------------- ------ ------ -------- ---------- ---------------")
                            for mobile in mobiles:
                                print(f"{mobile[0]:<6} {mobile[1]:<20} {mobile[2]:<20} {mobile[3]:<6} {mobile[4]:<6} {mobile[5]:<8} {mobile[6]:<10} {mobile[7]:<15} {mobile[8]:<6}")
                            print('S.no you want to change')
                            s = int(input())
                            if s== 0 :
                                break
                            MCursor.execute('select * from smartphones where sno = %s', (s,))
                            op = MCursor.fetchall()

                            if not op:
                                print("Record not found.")
                                break

                            for z in op:
                                print('Enter what you want to change:\n1)name\n2)brand\n3)ram\n4)camera\n5)storage\n6)colour\n7)os\n8)price\n9)Quit')
                                qe = int(input())
                                if qe == 1:
                                    name = input("Enter new name: ")
                                    MCursor.execute('update smartphones set name = %s where sno = %s', (name, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 2:
                                    brand = input("Enter new brand: ")
                                    MCursor.execute('update smartphones set brand = %s where sno = %s', (brand, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 3:
                                    ram = int(input("Enter new RAM: "))
                                    MCursor.execute('update smartphones set ram = %s where sno = %s', (ram, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 4:
                                    camera = int(input("Enter new camera: "))
                                    MCursor.execute('update smartphones set camera = %s where sno = %s', (camera, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 5:
                                    storage = int(input("Enter new storage: "))
                                    MCursor.execute('update smartphones set storage = %s where sno = %s', (storage, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 6:
                                    colour = input("Enter new colour: ")
                                    MCursor.execute('update smartphones set color = %s where sno = %s', (colour, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 7:
                                    os = input("Enter new OS: ")
                                    MCursor.execute('update smartphones set os = %s where sno = %s', (os, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                elif qe == 8:
                                    price = int(input("Enter new price: "))
                                    MCursor.execute('update smartphones set price = %s where sno = %s', (price, s))
                                    print('Update Success')
                                    Con.commit()
                                    break
                                else:
                                    break
                elif b == 2:
                    MCursor.execute("SELECT * FROM smartphones")  
                    mobiles = MCursor.fetchall()
                    print("Serial Mobile Name       Brand                RAM   Camera Storage Color     OS   Price")
                    print("------ -------------------- -------------------- ------ ------ -------- ---------- ---------------")
                    for mobile in mobiles:
                        print(f"{mobile[0]:<6} {mobile[1]:<20} {mobile[2]:<20} {mobile[3]:<6} {mobile[4]:<6} {mobile[5]:<8} {mobile[6]:<10} {mobile[7]:<15} {mobile[8]:<6}")
                    print('S.no you want to DELETE')
                    sno = int(input())
                    if sno == 0:
                        break
                    MCursor.execute('delete from smartphones where sno = %s', (sno,))
                    print('Successfully Deleted Record Thank You')
                    Con.commit()
                    break
                elif b == 3:
                    add_smartphone_details()
                    break      
                elif b == 4:
                    break
                else:
                    print('Invalid option')
            elif a == 2:
                print('Do You Want\n1) Update\n2) Delete\n3) Add Records\n4) Quit')
                b = int(input())
                if b == 1:
                    while True:
                            MCursor.execute("SELECT * FROM accessories")
                            accessories = MCursor.fetchall()
                            print("Serial Product Name            Brand   Model No             Product ID Cost")
                            print("------ ------------------------- ------- -------------------- ---------- ----")
                            for accessory in accessories:
                                print(f"{accessory[0]:<6} {accessory[1]:<27} {accessory[2]:<7} {accessory[3]:<20} {accessory[4]:<10} {accessory[5]:<4}")
                            print('Serial No you want to change')
                            serial_no = int(input())
                            if serial_no == 0:
                                break
                            MCursor.execute('SELECT * FROM accessories WHERE serialno = %s', (serial_no,))
                            accessory = MCursor.fetchone()

                            if accessory:
                                print('Enter what you want to change:')
                                print('1) ProductName\n2) Brand\n3) ModelNo\n4) ProductId\n5) Cost')
                                f = int(input())

                                if f == 1:
                                     new_value = input("Enter new ProductName: ")
                                     MCursor.execute('UPDATE accessories SET ProductName= %s WHERE serialno = %s', (new_value, serial_no))
                                     print('Update successful!')
                                     Con.commit()
                                elif f == 2:
                                    new_value = input("Enter new Brand: ")
                                    MCursor.execute(f'UPDATE accessories SET Brand= %s WHERE serialno = %s', (new_value, serial_no))
                                    print('Update successful!')
                                    Con.commit()
                                elif f == 3:
                                    new_value = input("Enter new ModelNo: ")
                                    MCursor.execute(f'UPDATE accessories SET ModelNo= %s WHERE serialno = %s', (new_value, serial_no))
                                    print('Update successful!')
                                    Con.commit()
                                elif f == 4:
                                    new_value = int(input("Enter new ProductId: "))
                                    MCursor.execute(f'UPDATE accessories SET Productid= %s WHERE serialno = %s', (new_value, serial_no))
                                    print('Update successful!')
                                    Con.commit()
                                elif f == 5:
                                    new_value = int(input("Enter new Cost: "))
                                    MCursor.execute(f'UPDATE accessories SET Cost= %s WHERE serialno = %s', (new_value, serial_no))
                                    print('Update successful!')
                                    Con.commit()
                                else:
                                    print("Invalid option")
                                    return

                           
                elif b == 2:
                    while True:
                        MCursor.execute("SELECT * FROM accessories")
                        accessories = MCursor.fetchall()
                        print("Serial Product Name            Brand   Model No             Product ID Cost")
                        print("------ ------------------------- ------- -------------------- ---------- ----")
                        for accessory in accessories:
                            print(f"{accessory[0]:<6} {accessory[1]:<27} {accessory[2]:<7} {accessory[3]:<20} {accessory[4]:<10} {accessory[5]:<4}")
                        print('Serial No you want to DELETE')
                        serial_no = int(input())
                        if serial_no == 0:
                            break
                        else:
                            MCursor.execute('DELETE FROM accessories WHERE serialno = %s', (serial_no,))
                            print('Delete successful!')
                        Con.commit()
                elif b == 3:
                        add_accessory_details()
                        break
                elif b == 4:
                        break
                else:
                        print('Invalid Try Again')
                        print('Accessory not found.')

            elif a == 3:
                        def max_purchase_amount_by_customer():
                            MCursor.execute('''SELECT customer_id, customer_name, MAX(price) AS max_purchase_amount
                            FROM customer
                            GROUP BY customer_id, customer_name
                            ORDER BY max_purchase_amount DESC
                            LIMIT 2;
                            ''')
                            r=MCursor.fetchall()
                            for i in range (0,2):
                                print(i+1,'max amount purchase is')
                                print(r[i][2])
                                print('The Customer gave most amount is\n',r[i][1].upper())
                        def frequent_customer():
                            MCursor.execute("""
                               SELECT MIN(customer_id) AS customer_id, customer_name, COUNT(*) AS purchase_count
                               FROM customer
                               GROUP BY customer_name
                                ORDER BY purchase_count DESC
                                LIMIT 2; """)
                            r=MCursor.fetchall()
                            for i in range (0,2):
                                print('The',i+1,'Star Customer Is:','With Purchase count',r[i][2])
                                print(r[i][1].upper())
                        def no_purchase_of_payment_method():
                            MCursor.execute("""
                            SELECT payment_method, COUNT(*) AS payment_count
                            FROM customer
                            GROUP BY payment_method;""")
                            s=MCursor.fetchall()
                            for i in s:
                                print('The Payment\'s done by method\n',i[0],'Is:',i[1])
                        def total_amount_got():
                            MCursor.execute("""
                            SELECT SUM(price) AS Amount_Given_By_All_Customers
                            FROM customer""")
                            s=MCursor.fetchall()
                            for i in s:
                                print("Amount_Given_By_All_Customers:\n",i)
                        def montly_amount_recieved():
                            query = """
                            SELECT YEAR(date) AS year, MONTH(date) AS month, SUM(price) AS total_amount
                            FROM customer
                            GROUP BY YEAR(date), MONTH(date) """
                            MCursor.execute(query)
                            result = MCursor.fetchall()
                            for row in result:
                                print(f"Year: {row[0]}, Month: {row[1]}, Total Amount Recieved: {row[2]}")
                        def lascus():
                            MCursor.execute("SELECT * FROM customer ORDER BY customer_id DESC LIMIT 1")
                            last_customers = MCursor.fetchone()
                            if last_customers:
                                    last_customer = last_customers
                                    print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<15} {:<11} {:<15}".format(
                                        "Serial", "Date", "Customer Name", "Phone Number", "Payment Type", "Item Name", "Discount", "Final Amount"))
                                    print("*" * 125)
                                    print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<25} {:<12} {:<15}".format(
                                        last_customer[0], str(last_customer[7]), last_customer[1], last_customer[2], last_customer[3], last_customer[4], last_customer[5], last_customer[6]))
                            else:
                                    print("No customer found.")
                        def Billww():
                                print('Date Format = 20xx-0x(month)-xx(date)')
                                date = input('Enter Starting date You want To Search: ')
                                datee = input("Enter Ending date You want to Search: ")  

                                MCursor.execute('SELECT * FROM customer WHERE date BETWEEN %s AND %s', (date, datee))
                                customers = MCursor.fetchall()
                                while True:
                                    if customers:
                                        print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<15} {:<11} {:<15}".format(
                                            "Serial", "Date", "Customer Name", "Phone Number", "Payment Type", "Item Name", "Discount", "Final Amount"))
                                        print("-" * 105)
                                        
                                        for last_customer in customers:
                                            print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<15} {:<11} {:<15}".format(
                                                last_customer[0], str(last_customer[7]), last_customer[1], last_customer[2], last_customer[3], last_customer[4], last_customer[5], last_customer[6]))
                                        break
                                    else:
                                        print('NO CUSTOMER BETWEEN THAT DATE RANGE')
                                        if input('Or If You Want To Quit Press Q').lower() == 'q':
                                            break
                                        

                        print('''The Reports You Want To Show:\n1)1 - Two Star \nCustomer\n2)2 - Paymentmethod Total\n3)3 - Max Amount Of Money Spend by first 2 customers\n4)4 - Total Amount Got\n5)5 - MONTHLY AMOUNT RECIEVED \n6)6 - SHOWCUSTOMERS\n7)7 - SHOWFEEDBACK\n8)8 - Shows Last customer\n9)9 - Bills within Two Date Interval\n10)10 - Quit''')
                        pp=int(input())
                        while True:
                            if pp == 1:
                                frequent_customer()
                                break
                            elif pp == 2:
                                no_purchase_of_payment_method()
                                break
                            elif pp == 3:
                                max_purchase_amount_by_customer()
                                break
                            elif pp == 4:
                                total_amount_got()
                                break
                            elif pp == 5:
                                montly_amount_recieved()
                                break
                            elif pp == 6:
                                sc()
                                break
                            elif pp == 7:
                                feedback_file = "feedback.txt"
                                try:
                                    with open(feedback_file, "r") as f:
                                        contents = f.read()
                                        print(contents)
                                        break
                                except FileNotFoundError:
                                    print("The feedback file does not exist.")
                            elif pp == 8:
                                lascus()
                                break
                            elif pp == 9:
                                Billww()
                                break
                            elif pp == 10:
                                break
                            else:
                                print('Invalid and Try Again')
            elif a == 4:
                break
            else:
                        print('Invalid option')
        
                                                         
                                                                        
                                                                        
                                             
def mobile_purchase():
    MCursor.execute("SELECT * FROM smartphones")  
    mobiles = MCursor.fetchall()
    print("Serial Mobile Name       Brand                RAM   Camera Storage Color     OS   Price")
    print("------ -------------------- -------------------- ------ ------ -------- ---------- ---------------")
    for mobile in mobiles:
        print(f"{mobile[0]:<6} {mobile[1]:<20} {mobile[2]:<20} {mobile[3]:<6} {mobile[4]:<6} {mobile[5]:<8} {mobile[6]:<10} {mobile[7]:<15} {mobile[8]:<6}")

    serial_number = int(input("Enter Serial Number of the mobile you want to buy: "))
    MCursor.execute("SELECT * FROM smartphones WHERE sno = %s", (serial_number,))
    selected_mobile = MCursor.fetchone()

    if selected_mobile:
        print(f"Your desired mobile is {selected_mobile[1]}. Its details are as follows:")
        print(f"Serial Number: {selected_mobile[0]}")
        print(f"Name: {selected_mobile[1]}")
        print(f"Brand: {selected_mobile[2]}")
        print(f"RAM: {selected_mobile[3]}")
        print(f"Camera: {selected_mobile[4]}")
        print(f"Storage: {selected_mobile[5]}")
        print(f"Color: {selected_mobile[6]}")
        print(f"OS: {selected_mobile[7]}")
        print(f'Cost:{selected_mobile[8]}')

        ask_buy = input("Do you want to buy it? (Y - YES/N - NO): ").strip().upper()
        if ask_buy == "Y":
            buy(selected_mobile[1],selected_mobile[8])
        else:
            print("Visit Again")
    else:
        print("Mobile not found. Please try again.")


def accessory_purchase():
    MCursor.execute("SELECT * FROM accessories")
    accessories = MCursor.fetchall()
    print("Serial Product Name            Brand   Model No             Product ID Cost")
    print("------ ------------------------- ------- -------------------- ---------- ----")
    for accessory in accessories:
        print(f"{accessory[0]:<6} {accessory[1]:<27} {accessory[2]:<7} {accessory[3]:<20} {accessory[4]:<10} {accessory[5]:<4}")

    serial_number = int(input("Enter Serial Number of the accessory you want to buy: "))
    MCursor.execute("SELECT * FROM accessories WHERE serialno = %s", (serial_number,))
    selected_accessory = MCursor.fetchone()

    if selected_accessory:
        print(f"Your desired accessory is {selected_accessory[1]}. Its details are as follows:")
        print(f"Serial Number: {selected_accessory[0]}")
        print(f"Product Name: {selected_accessory[1]}")
        print(f"Brand: {selected_accessory[2]}")
        print(f"Model No: {selected_accessory[3]}")
        print(f"Product ID: {selected_accessory[4]}")
        print(f"Cost: {selected_accessory[5]}")

        ask_buy = input("Do you want to buy it? (Y - YES/N - NO): ").strip().upper()
        if ask_buy == "Y":
            buy(selected_accessory[1],selected_accessory[5])
        else:
            print("Visit Again")
    else:
        print("Accessory not found. Please try again.")


def buy(item_name,Price):
    while True:
        phone_number = input("Enter phone number: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            phone_number = '+91' + phone_number
            break
        else:
            print('Invalid phone number. Please enter a 10-digit number.')
            print('Or Do You want to Quit Press 1 \nTo Continue Enter 0')
            po=input()
            if po == '1':
                main()
                
    customer_name = input("Enter customer name: ")
        
    print(' Do You want to Quit Press 1 or \nTo Continue Enter 0')
    if input() == '1':
        main()
        

    print('Your Mode Of Payment')
    print('1 - UPI')
    print('2 - Cash')
    print('3 - Card')
    print('Or To Quit Press 0')
    while True:
        ch = input()
        if ch == '1':
            payment_type = 'UPI'
            break
        elif ch == 0:
            main()
        elif ch == '2':
            payment_type = 'Cash'
            break
        elif ch == '3':
            p = 'Card'
            if p == 'Card':
                print('1 - Credit Card')
                print('2 - Debit Card')
                ok = input()
                while True:
                    if ok == '1':
                        payment_type = 'Card - Credit'
                        break
                    else:
                        payment_type = 'Card - Debit'
                        break
                break
        else:
            print('Not available')
    d = r.randint(0, 4)
    MCursor.execute('''SELECT customer_name, phone_number,COUNT(*) as purchase_count
            FROM customer
            GROUP BY customer_name, phone_number''')
    nb=MCursor.fetchall()
    p=cus_week()
    c = ''
    for i in nb:
        if  i[0] == customer_name and i[1] == phone_number :
            d = d+(i[2]//2)
            print(i[2])
            print(i[2]//2)
        if i[0] == p and p ==  customer_name :
            d=d+5
            c = i[0]
            break
    if d >= 25 and c == p:
        d=0
    elif d >=15 and c!=p:
        d=0
            
    afterdiscount=Price-(Price*(d/100))
    kl = "SELECT curdate()"
    MCursor.execute(kl)
    t = MCursor.fetchone()
    MCursor.execute("INSERT INTO customer (customer_name, phone_number, payment_method, item_name, discount, price , date) VALUES (%s, %s, %s, %s, %s, %s, %s )",
                    (customer_name, phone_number, payment_type, item_name, d, afterdiscount,t[0]))
    Con.commit()
    MCursor.execute('SELECT * FROM customer')
    customerss = MCursor.fetchall()

    if customerss:
        last_customer = customerss[-1]
        print('Here Is Your Bill')
        print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<15} {:<11} {:<15}".format(
            "Serial", "Date", "Customer Name", "Phone Number", "Payment Type", "Item Name", "Discount", "Final Amount"))
        print("*" * 110)
        print("{:<8} {:<15} {:<25} {:<15} {:<20} {:<15} {:<11} {:<15}".format(
            last_customer[0], str(last_customer[7]), last_customer[1], last_customer[2], last_customer[3], last_customer[4], last_customer[5], last_customer[6]))
    else:
        print("No customer found.")
            

        
    print("Payment done.")
    print("Thank you for your purchase!\n Do You want to Give Feedback")
    ph=input('Y - Yes / N - No').upper()
    if ph == 'Y':
        feedback_file = "feedback.txt"
        user_feedback = input("Enter your feedback: ")
        with open(feedback_file, "a") as f:
            f.write(f'Thank You Customer For FeedBack {customer_name}\n')
            while True:
                p=int(input('Rate us Out Of 5'))
                if p>5:
                      print('Try Again')
                else:
                    break
            f.write(f'Our Rating By {customer_name} is {p} Out of 5\n')
            f.write(user_feedback + "\n")
            print('if you give any more feedback please\n continue by pressing 1 else press 0')
            sss=int(input())
            if sss == 1:
                 user_feedback = input("Enter your feedback: ")
                 f.write(user_feedback + "\n")
    Con.commit()
                
            
        
        
        


# MAIN FUNCTION STARTS FROM HERE !!!
def print_decorative_banner(text):
    decorative_line = "█" * (len(text) + 4) 
    print(decorative_line)
    print(f"█ {text} █")
    print("█ By Dev - Anshukman MJ🌟, Sanjeev D🌟, Susindharen CNC🌟█")
    print(decorative_line)




def add_accessory_details():
    product_name = input("Enter product name: ")
    brand = input("Enter brand: ")
    model_no = input("Enter model number: ")
    product_id = input("Enter product ID: ")
    cost = float(input("Enter cost: "))

    MCursor.execute("INSERT INTO accessories (productname, brand, modelno, productid, cost) VALUES (%s, %s, %s, %s, %s)",
                     (product_name, brand, model_no, product_id, cost))
    Con.commit()
    print("Accessory details added successfully!")


def add_smartphone_details():
    mobile_name = input("Enter mobile name: ")
    brand = input("Enter brand: ")
    ram = input("Enter RAM: ")
    camera = input("Enter camera: ")
    storage = input("Enter storage: ")
    color = input("Enter color: ")
    os = input("Enter OS: ")
    price = float(input("Enter price: "))

    MCursor.execute("INSERT INTO smartphones (name, brand, ram, camera, storage, color, os, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                     (mobile_name, brand, ram, camera, storage, color, os, price))
    Con.commit()
    print("Smartphone details added successfully!")

def main():
    while True:
        p=cus_week()
        print_decorative_banner("       🌟 Welcome to Online Mobile Seller! 🌟")
        print('OUR CUSTOMER OF THE WEEK IS::',end='')
        print(f"█ {p} █")
        print('(1)M - MobilePurchase\n(2)A - AccessoryPurchase\n(3)Q - Quit\n(4)U - Admin')
        choice = input("CHOOSE THE OPTION YOU WANT 🌟  ").upper()
        if choice == "M" or choice == '1':
            mobile_purchase()
        elif choice == "A" or choice == '2':
            accessory_purchase()
        elif choice == "Q" or choice == '3':
            break
        elif choice == 'U' or choice == '4':
            admin()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


MCursor.close()
Con.close()







