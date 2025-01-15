'''Q. Write a program to generate all combinations of 1, 2 and 3 using for loop.'''

for i in range(1,4): 
        for j in range(1,4): 
            for k in range(1,4): 
                  
                # check if the indexes are not 
                # same 
                if (i!=j and j!=k and k!=i): 
                    print(i, j, k) 
