star= '*' 
try:
    num=int(input("Enter number star:"))
    i = 1
    while i < num:
        print(i*star)
        i+=1
        if i==num:
            j=num
            while j >= 1:
                print(j*star)
                j-=1
    
except ValueError:
    print("invalid entered try integer value")
    
  
