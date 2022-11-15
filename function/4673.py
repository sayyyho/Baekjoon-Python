no_self = []
for i in range (0,10000):
    if (i<10):no_self.append(i+i%10)
    elif (i<100): no_self.append(i+i//10+i%10)
    elif (i<1000): no_self.append(i+i//100+i%100//10+i%10)
    else:no_self.append(i+i//1000+i%1000//100+i%100//10+i%10)
for num in range(0, 10000):
    if(num not in no_self):
        print(num)