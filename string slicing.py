'''var1="whatever it takes"
print(var1[::2])
var2="im a good"
print(var2.replace("a","the"))
var3="kingroyal"
print(var3.index("o"))
var4="only one"
print(var4.upper())'''


##string slicing exersice

product=("redmi |rs: 80000 |brand new")
name=(product[0:product.index("|")])
print("the name of a phoneis",name)
price=(product[product.index("|")+1:product.rindex("|")])
print("the price of  a phone is ",price)
model=(product[product.rindex("|")+1:])
print("th model of phone is ",model)