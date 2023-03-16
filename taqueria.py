# dict
total = 0
dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:

    try:
        
        question = input("What would you like to eat Sir? ")
        price = dict[question]
        total = int(total) + int(price)
        print(f"Total: ${total:.2f}")
        

    except (EOFError, KeyError):
        pass

