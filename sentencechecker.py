vowels = ['a','e','i','o','u']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','%','$','^','&','*','(',')']
vowels_count = 0
numbers_count = 0
symbols_count = 0
names = input("Enter names: ")
for i in names:
    if i in vowels:
        vowels_count = vowels_count + 1
    elif i in numbers:
        numbers_count = numbers_count + 1
    elif i in symbols:
        symbols_count = symbols_count + 1

print("vowels: ", vowels_count)  
print("numbers: ", numbers_count) 
print("symbols: ", symbols_count)



