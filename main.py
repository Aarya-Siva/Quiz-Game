points=0
print("Multiple Choice Game")
print("")
print("")
print("1. What is the capital of the US?")
print("A = Washington D.C")
print("B = India")
print("C = Vermont")

answer_1=input("> ")
if answer_1=="A" or answer_1=="a":
    print("Correct")
    points=points+1
else:
    print("wrong")
    
print("2. Which soccer player has the most Ballon D'or's?")
print("A = Pele")
print("B = Ronaldo")
print("C = Messi")

answer_2=input("> ")
if answer_2=="C" or answer_2=="c":
    print("Correct")
    points=points+1

else:
    print("wrong")
print(points)

print("3. What year was the first Harry Potter book published ?")
print("A = 1995")
print("B = 1997")
print("C = 1999")

answer_3=input("> ")
if answer_3=="B" or answer_3=="b":
    print("Correct")
    points=points+1

else:
    print("wrong")
print(points)


print("4. What planet is known as the red planet?")
print("A = Mars")
print("B = Earth")
print("C = Venus")

answer_4=input("> ")
if answer_4=="A" or answer_4=="a":
    print("Correct")
    points=points+1

else:
    print("wrong")
print(points)

print("5. Which element has the chemical symbol Fe")
print("A = Gold")
print("B = Iron")
print("C = Lead")

answer_5=input("> ")
if answer_5=="B" or answer_5=="b":
    print("Correct")
    points=points+1

else:
    print("wrong")
print(points)


print("6. Which city is known as the Big Apple")
print("A = Chicago")
print("B = Los Angeles")
print("C = New York City")

answer_6=input("> ")
if answer_6=="C" or answer_6=="c":
    print("Correct")
    points=points+1
    
print("5. Which player got drafted 1st overall in the 2023 NBA Draft? ")
print("A = Victor Webanyama")
print("B = Lebron James")
print("C = Anthony Edwards")

answer_7=input("> ")
if answer_7=="A" or answer_7=="a":
    print("Correct")
    points=points+1
else:
    print("wrong")
print("Quiz Complete")
print("You answered " + str(points) + " out of 7 correctly.")

#Please put more questions, otherwise very good