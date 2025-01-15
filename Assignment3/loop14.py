'''Q. A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The 
machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent 
per annum can be earned on alternate investments what would be the minimum life of the 
machine to make it a more attractive investment compared to alternative investment?'''

y=1
while (1):
    business=y*1000 + 2000
    investment=(6000*y*12)/100 +6000
    if business>investment:
        print('Minimum year =',y)
        break
    y=y+1
