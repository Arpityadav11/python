'''
                                        *** Object-Oriented Programming (OOP) ***

🔹 Definition:
Object-Oriented Programming is a method of solving real-world problems using **classes** and **objects**.

---

🔹 Key Features of OOP:
- Security  
- Code Reusability  
- Scalability  
- Fewer lines of code compared to Procedural-Oriented Programming (POP)

---

🔹 Four Pillars of OOP:
1. **Inheritance** – Reusing code from one class in another  
2. **Encapsulation** – Hiding internal details and exposing only necessary parts  
3. **Polymorphism** – Performing a single action in different ways  
4. **Abstraction** – Showing only essential features and hiding complexity

---

🔹 Class:
Every real-world entity can be modeled as a class.  
- **Attributes** → Variables (e.g., name, age)  
- **Behaviors** → Functions (e.g., walk(), speak())

📌 Definition:  
A **class** is a blueprint for creating objects.  
Its attributes and behaviors are shared with the objects created from it.

---

🔹 Object:
An **object** is an instance of a class.  
It represents a specific example of the blueprint defined by the class.

*** Creating Objects in OOP ***

🔹 To create an object from a class:
Assign the class name followed by parentheses to a variable.

📌 Syntax:
obj = ClassName()

📌 Example:
obj = c1()  # Creates an object of class c1

                *** Object Independence in OOP ***

🔹 When an object changes its attribute(e.g., color), it does **not** affect other objects of the same class.

📌 Example:
If `obj1.color = "red"`  
Then `obj2.color` remains unchanged unless explicitly modified.

🧠 Why?
Each object has its **own copy** of the class attributes (unless they are class-level/static variables).  
This ensures **object independence** in behavior and state.

                    *** Class Attributes and Methods in OOP ***

🔹 Attributes:
- Attributes store data or state related to a class or object.
- They can be modified by either the class itself or its objects.
- Typically represent **static information** (e.g., name, age, color).

🔹 Methods:
- Methods define actions or behaviors associated with a class.
- They operate on attributes and perform tasks (e.g., display info, update values).

🧠 Summary:
- **Attributes** = Data (variables)
- **Methods** = Actions (functions)
 
'''

# class car:
#     color = 'red'
#     model = 2025
#     def start(self):
#         print('car started')
#     def start_travelling(self):
#         print('going for ujjain mahakal temple .. ...')
        
# bmw = car() # object of the class 
# # bmw.start()
# # bmw.start_travelling()
# bmw.color = 'black'
# print(bmw.color)

''' 
create a class with the three attributes and two methods then create two different objects of same
class show how the attribute change with respect to the object and class
'''

# class pubg:
#     lobby = 100
#     remaining = 4
#     finished = lobby-remaining
#     def winner(self):
#         print('winner winner chicken dinner')
#     def lose(self):
#         print('better luck next time')

# p1 = pubg()
# p1.remaining = 45
# print(p1.lobby)
# p1.lose()

# # custom 
# pubg.lobby = 64
# pubg.finished = 50
# p2 = pubg()
# p2.remaining = 2
# print(p2.finished)

# p2.winner()

'''
                        *** Class Variables in OOP ***

🔹 Definition:
Class variables are shared across all instances of a class.  
They hold the same value for every object unless modified at the class level.

---

🔹 Characteristics:
- Stored at the class level, not per object.
- Accessible via both `ClassName.variable` and `object.variable`.
- Ideal for values that should be consistent across all objects (e.g., counters, configuration flags).
 
---

🔹 Ways to Declare Class Variables:

1. **Inside the class, outside any method**
   class MyClass:
       count = 0  # class variable
       
2.Inside a method using the class name
    class MyClass:
        def update():
        MyClass.count = 10
        
3.Outside the class using the class name
    My Class.count = 20
'''

'''
Word pattern leetcode problem
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        temp = []
        for i in pattern:
            temp.append(pattern.find(i))

        ref = []
        for i in words:
            ref.append(words.index(i))

        return temp == ref
'''
