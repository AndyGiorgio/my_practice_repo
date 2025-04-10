# Lists
cart=["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
if "cherry" in cart:
    cart.remove("cherry")
print(cart)

cart.pop(2)
print(cart)
cart.pop()
print(cart)

cart.reverse()
print(cart)
cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

fruit_basket=cart[3:]
print(cart)
print(fruit_basket)

squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares=[x*x for x in range(1,11)]
print(squares)

print(cart)
b_items=[item for item in cart if item.startswith('b')]
print(b_items)

lst=['1','2','20','15','180']
num_lst=[int(x) for x in lst]
num_lst.sort()
print(num_lst)

inventory=[0]*len(cart)
print(inventory)
inventory[0]=1
print(inventory)

# Sets
empty=set()
num_sets={1,1,3,4}
num_sets.add(5)
num_sets.add(10)
print(num_sets)
lst=[1,2,2,3,3,4]
unique=set(lst)
print(unique)
unique=list(unique)
print(unique)

st={4,10,3,7,8}
print(st)
sorted(st)
print(st)

# Dictionary
fav_snack={}
fav_snack={
    "Kathleen":"tortilla chips",
    "Ava":"chex mix",
    "Emily":"buffalo chicken dip",
    "Wade":"popcorn"
}
print(fav_snack)
fav_snack["Lucas"]="chocolate"
print(fav_snack)
for key in fav_snack:
    print(f"{key}'s favorite snack is {fav_snack[key]}")
    print(key+"'s"+" favorite snack is "+fav_snack[key])

for key,value in fav_snack.items():
    print(key,value)

if "Bob" in fav_snack:
    print("Bob's fav snack is "+fav_snack["Bob"])
else:
    fav_snack["Bob"]="chips"

keys=fav_snack.keys()
values=fav_snack.values()
print(sorted(keys))
print(sorted(values))

fav_snack["Alice"]=["chips","nuts"]
print(fav_snack)




