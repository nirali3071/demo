print("-------- welcome to kalyan jwellers---------")

name = input("enter name :")
gender = input("enter gender :")
age = int(input("enter age:"))
product_nm input("enter product:")
product_grm =int("enter product gram:")
gold_price =int(input("enter gold price:"))
mk_charge =int(input("enter making charges:"))

print("name:",name)
print("gender:",gender)
print("age:",age)
print("product:",product)
print("product_gram:",product gram)
print("gold_price:",)

total_rate = product_grm * gold price
print("total gold rate:",total_rate)


total_mkcharge = total_rate +(mk charge*product gram)
print("total amount :",total_amt)

total_amt = total_rate + total_mkcharge
print("total making charge:",total_amt)

discount =""
if gender=="male":

    if age>65:
        if total_amt>=200000 and total_amt<300000
        print("discount 20%")
        discount=total_amt"0.2

    elif total_amt>=300000 and total_amt<500000
        print("discount 30%")
        discount=total_amt*0.3

    elif total_amt>500000:
        print("discount 35%")
        discount=total_amt*0.1
 
    else:
        print("no discount")

    else
        if total_amt=200000 and total_amt<300000:
               print("discount 10%")
               discount=total_amt*0.1

        elif total_amt=<300000 and total_amt<500000
               print("discount 20%")
               discount=total_amt*0.2

            elif=total_amt>=500000
               print("discount 25%")
               discount=total_amt*0.25            
           
           else:
            print("no discount")

if gender=="female":
    if age>65:
        if total_amt>=200000 and total_amt<300000:
            print("discount 25%")
            discount=total_amt"0.25

    elif total_amt>=300000 and total_amt<500000:
        print("discount 35%")
        discount=total_amt*0.35

    elif total_amt>500000:
        print("discount 40%")
        discount=total_amt*0.4

        else
            print("no discount")

    else:
        if total_amt>=200000 and total_amt<300000:
            print("discount 25%")
            discount=total_amt*0.15

        elif total_amt>=300000 and total_amt<500000
        print ("discount 25%")
        discount=total_amt"0.25

       elif total_amt>500000:
        print("discount30 %")
        discount=total_amt*0.3

        else
            print("no discount")

dis_amt = (total_amt-total_mkcharges)-discount
print("discount amount :",dis_amt)

totalnet_amount = total_amt-dis_amt
print("total net amount:",totalnet_amt)
















