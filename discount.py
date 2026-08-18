amount=float(input("price"))
discount=0 if amount <500 else amount*0.05 if amount <=1000 else amount *0.10 if amount <=2000 else amount*0.15
final_price= (amount*(100-discount))/100
print ("ميزان تخفيف",discount)
print("قيمت نهايي" ,final_price)
             
