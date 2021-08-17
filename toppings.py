#requested_toppings= ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        if (requested_topping == 'green peppers'):
            print ("Sorry, we are out of green peppers rigth now.")
    else:
        print ("Adding "+ requested_topping + ".") 
else:
    print("Are you sure you want a plain pizza?")

print ("\nFinished making your pizza!")
