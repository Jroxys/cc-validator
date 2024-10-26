def validator():
    while True:
        card_num = int(input("ENTER YOUR CARD NUMBER:\n----------------------------------\n"))
        
        a = list(str(card_num))
        
        """if len(a)>16 or len(a)<16:
                print("Please put valid card.")
                print("----------------------------------")
                input("Press Enter for try again.")
        else:"""
        for i in range(len(a)-2,-1,-2):
                    c = int(a[i])*2
                    if c >= 10:
                        c = c%10
                        c = c+1
                        a.pop(i)
                        a.insert(i,str(c))
                    else:
                        a.pop(i)
                        a.insert(i,str(c))
        print(a)
                
        a = list(map(int, a))
        tuple(a)
        sum_a = sum(a)
                
                
                
        if sum_a % 10 == 0:
                    print("Valid Credit Card!")
                    print("----------------------------------")
        else:
                    print("Its not valid credit card!")
                    print("----------------------------------")
                           
        
    

menu = """
    WELCOME TO CREDIT CARD VALIDATOR!
    Enter your credit card number (16 digits!)\n
"""



print(menu)
while True:
    validator()
    