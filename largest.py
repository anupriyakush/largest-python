num = int
largest=None
smallest=None
while True:
    data = input("Enter integers: ")
    if data == 'done':
        break
    try:
        num = int(data)
    except:
        print("Invalid input")
    if largest is None:
        largest=num
    if num>=largest:
        largest = num
    if smallest is None:
        smallest=num
    if num<=smallest:
         smallest = num
    continue
print("Maximum is "+str(largest))
print("Minimum is "+str(smallest))