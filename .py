#qno-5
a = [66,20,56,33,77,66]
b= [26,55,13,55,55,66]
if a[0]==a[-1]:
    print("True")
else:
    print("False")
if b[0]==b[-1]:
    print("True")
else:
    print("False")            





#Qno-4
#class circle():
   # def __init__(self,r):
      #  self.radius= r
    #def area(self):
        #return self.radius**2*3.14
   # def perimeter(self):
       # return 2*self.radius*3.14
#NewCircle = circle(9)
#print(NewCircle.area())
#print(NewCircle.perimeter())            



#QNO-1          
#a,b,c,d,e=input("enter no.1 :"),input("enter no.2 :"),input("enter no.3 :"),input("enter no.4 :"),input("enter no.5 :")
#li=[a,b,c,d,e]
#print(max(li))





#Qno-3
#class Rectangle():
   # def __init__(self,l,w):
        #self.length = l
        #self.widith = w
    #def rectangle_area(self):
        #return self.length*self.widith
#newRectangle = Rectangle(22,40)
#print(newRectangle.rectangle_area())            



#qno-1
#numbers = [23,5,6,7,7,7]
#print(max(numbers))
#qnoo-2
#class py_solution:
    #def twoSum(self , nums , target):
       # lookup = {}
    #for i in num in(nums):
       ## if target - num in lookup:
            #return (lookup[target - num], i)
        #lookup[num] = i
#print("index1=%d, index2=%d" % py_solution().twoSum((12,55,33,565,3)))            

#numbers = []
#for i in range(0,5):
    #inputNumber = int(input("Enter a number: "))
    #numbers.append(inputNumber)
    #print(numbers)
#print("--------------->")    
 
numbers = [10,20,30,40,50,60,70]
target = 50
for i in range(0, len(numbers)-1):
    sum = numbers[i] + numbers+i
    #
for i in numbers:
    if (i> max):
            max = i
    print(max)        

 
numbers = []
for i in range(0,5):
   inputNumber = int(input("Enter a number: "))
   numbers.append(inputNumber)
 
max = 0
for i in numbers:
   if (i > max):
       max = i
 
print(max)