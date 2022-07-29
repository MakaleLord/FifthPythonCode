
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand
import random 

grocery = ["Pizza Rolls", "Chips", "Apples", "Gatorade", "Water"]

print("Groceries")
for item in grocery:
    print("_", item)
print()

max_index = len(grocery)-1
random_index = random.randint(0, max_index)
print("You got ", grocery[random_index])
print()
print("------")

electronics = ["Charger", "MacBook", "iPhone", "Ethernet Cable", "LED Lights"]

print("Electronics")
for item in electronics:
    print("_", item)
print()

max_index = len(electronics)-1
random_index = random.randint(0, max_index)
print("You got ", electronics[random_index])
print()
print("------")

books = ["Harry Potter Series", "DOAWK Series", "Hunger Games Series", "The Book Thief", "The Outsiders"]

print("Books")
for item in books:
    print("_", item)
print()

max_index = len(books)-1
random_index = random.randint(0, max_index)
print("You got ", books[random_index])
print()
print("------")

shopping_list = grocery + electronics + books
max_index = len(shopping_list)-1
random_index = random.randint(0, max_index)
print("You got ", shopping_list[random_index]) 
