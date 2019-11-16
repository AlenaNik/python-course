name = input('Put you name in here: ')
print(len(name))
if len(name) < 3:
    print("Name must be a least 3 charactrs")
elif len(name) > 50:
    print("Too long")
else:
    print("Looks good to me")