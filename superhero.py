
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

avengers = ["Ant-Man", "Black Panther", "Captain America", "Doctor Strange","Hulk", "Iron Man", "Spider-Man"]

print("Avengers")
for item in avengers:
    print("_", item)
print()

max_index = len(avengers)-1
random_index = random.randint(0, max_index)
print("You are ", avengers[random_index])
print()
print("------")
Justice_League = ["Aquaman", "Bat-man", "Cyborg", "Flash", "Superman", "Wonder-woman"]

print("Justice League") 
for item in Justice_League:
    print("_", item)
print()                  

max_index = len(Justice_League)-1
random_index = random.randint(0, max_index)
print("You are ", Justice_League[random_index]) 
print()
print("------")

teentitans = ["Beast Boy", "Raven", "Robin", "Starfire", "Terra"]

print("Teen Titans")
for item in teentitans:
    print("_", item)
print()

print("You are ", teentitans[random_index])
print()
print("------")

max_index = len(teentitans)-1
random_index = random.randint(0, max_index)

superhero = avengers + Justice_League + teentitans
max_index = len(superhero)-1
random_index = random.randint(0, max_index)
print("You are ", superhero[random_index])
