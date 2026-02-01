start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
result = 0
for num in range(start, end+1):
    result = result + num
print(f"The sum of numbers from 1 to 50 is: {result}")