amount = int(input("Enter amount to withdraw: "))

notes = [500, 200, 100, 50]

for note in notes:
    count = amount // note
    if count > 0:
        print(note, "x", count)
        amount = amount % note

if amount != 0:
    print("Cannot dispense remaining amount:", amount)
