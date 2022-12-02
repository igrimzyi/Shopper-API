#ISAIAH TAMAYO

#CSE 1250(61)

#FINAL PROJECT

# NOV 30 2022




#This program will calculate your total with certain factors such as weight, subtotal, taxes

#States Array:
statesAbbreviated = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'];

# initialize main function loop
runAgain = True;

#initialize user greeting
def userGreeting():
    print("This program will calculate your total with certain factors such as weight, subtotal, taxes");
    print();

#initialize user input for what state they are in and we have to pass our states array
def getState(statesAbbreviated):
    #ask for the input
    stateInput = input("Please Enter your states abbreviation e.g CA: ").upper(); 

    #error handle
    while stateInput not in statesAbbreviated:
        stateInput = input('Input Error: Please enter a valid state:').upper();
    print()

    #return chosen State
    return stateInput;

#initialize function to get the products and pricing, weight, and amount for each
def getProducts():
    #initial item array
    itemList = []; 

    #initial looper 
    isLooped = True;

    #ask user for how many products
    itemsQuantity = int(input("Please Enter the Amount of Items: "));

    #iterate through products and ask for each one
    if itemsQuantity == 0:
        #when iterator hits 0 stop looping
        isLooped = False; 
    else:
        while isLooped: 
            #ask for each factor and then push it on the list
            print()
            itemQuantity = int(input("How many Items do you have of this product: "))
            print()
            itemWeight = int(input("Enter the items weight in pounds: "));
            print()
            itemPrice = int(input("Enter the Price of the item: "));
            print()

            #pushed
            itemList.append([itemQuantity,itemWeight,itemPrice])
            
            #decrement through the iterator
            itemsQuantity = itemsQuantity- 1;

            #set looper to false if the iterator hits 0 
            if itemsQuantity == 0:
                isLooped = False;

    #return our products list 
    return itemList; 

#initialize calculator
def getCalculations(products):
    #initialize the box weight and total
    boxWeight = 0;
    subTotal = 0
    
    #loop through our products list to calculate each product
    for mainIndex in range(len(products)):

                        #initialize temp variables
                        itemQuantity, itemWeight, itemCost = products[mainIndex]
                        
                        #calculations
                        boxWeight = boxWeight + (itemQuantity * itemWeight)
                        subTotal = subTotal + (itemQuantity * itemCost)
    #calc shipping 
    shipping = boxWeight * .25; 

    #get right handling based off of total weight
    if boxWeight < 10:
        handling = 1
    elif boxWeight > 100:
        handling = 5
    else:
        handling = 3


    #add ship and handling
    shipAndHand = shipping + handling;

    #return subtotal and shipping handling

    return (subTotal, shipAndHand); 


#define function to loop main
def loopFunc():
    #ask user for their choice
    choice = input("Would you like to run this program again: ").lower(); 

    #error handler
    while choice != 'y' and choice != 'n':
        choice = input("INPUT ERROR: please enter a y or n: ").lower(); 
    
    #choice return statement
    if choice == 'y':
        return True;
    else:
        return False;

#loop main
while runAgain is True:

    #call user greeting
    userGreeting();

    #call getState and set it to a variable whilst passing in our array
    stateMain = getState(statesAbbreviated);

    #call getProducts and set it to a variable
    products = getProducts();

    #set two variables and call our getCalculations whilst passing or products array 
    subTotal , shippingHandling = getCalculations(products)

    #if statement to set california's state taxes

    if stateMain == "CA":
        tax = subTotal * .08
    else:
         tax = 0.00


    #print sub total
    print(format('Subtotal:', '<10'), format(subTotal, '>10,.2f'))

    #calculate grand total
    total = subTotal + tax + shippingHandling;

    #print shipping and handling
    print(format('Shipping and Handling:', '<10'), format(shippingHandling, '>10,.2f'));

    #print Grand total
    print(format('Grand Total:', '<10'), format(total, '>10,.2f'))

    print(); 





    runAgain = loopFunc();

print('Have a Nice Day!')






