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
#         print(self.remaining)
#         print('winner winner chicken dinner')
#     def lose(self):
#         print('better luck next time')

# p1 = pubg()
# p1.remaining = 45
# print(p1.lobby)
# p1.winner()

# # custom 
# pubg.lobby = 64
# pubg.finished = 50
# p2 = pubg()
# p2.remaining = 2
# print(p2.finished)

# p2.winner()


'''
                        *** Static Variables in Object-Oriented Programming ***

🔹 Definition:
Static variables, also known as **class variables**, are variables that are shared across all instances of a class.  
They are defined at the class level and maintain a single copy that is accessible and modifiable by all objects of that class.

---

🔹 Purpose:
Static variables are used when a value needs to be **consistent across all objects**, such as:
- Counters (e.g., tracking number of objects created)
- Configuration flags
- Shared resources or limits

---

🔹 Characteristics:
- Stored in the class namespace, not in the object’s instance dictionary.
- Accessible via both `ClassName.variable` and `object.variable`.
- Changing the value via the class affects all objects.
- Changing via an object creates a new instance variable (unless explicitly referencing the class).

---

🔹 Ways to Declare Static Variables:

1. **Inside the class, outside any method**
   ```python
   class MyClass:
       count = 0  # static/class variable
   ```

2. **Inside a method using the class name**
   ```python
   class MyClass:
       def update():
           MyClass.count = 10
   ```

3. **Outside the class using the class name**
   ```python
   MyClass.count = 20
   ```

4. **Using the @classmethod decorator**
   ```python
   class MyClass:
       count = 0

       @classmethod
       def set_count(cls, value):
           cls.count = value
   ```

5. **Using the @staticmethod decorator**
   ```python
   class MyClass:
       count = 0

       @staticmethod
       def show_count():
           print(MyClass.count)
   ```

---

🔹 Decorators Explained:

- **@classmethod**
  - Used to define methods that operate on class-level data.
  - First parameter is `cls` (refers to the class itself).
  - Can access and modify static variables using `cls.variable`.

- **@staticmethod**
  - Used to define utility methods that don’t need access to instance (`self`) or class (`cls`) data.
  - Cannot directly access static variables unless referenced by class name.
  - Ideal for logic that belongs to the class but doesn’t depend on its state.

---

🔹 Conceptual Clarification:

- Static variables are **not tied to any specific object**.
- They are part of the class definition and exist **once** in memory.
- Instance variables, on the other hand, are **unique to each object** and defined using `self`.

🧠 Summary:
| Type             | Scope        | Shared Across Objects | Accessed By         |
|------------------|--------------|------------------------|---------------------|
| Static Variable  | Class-level  | ✅ Yes                 | Class or object     |
| Instance Variable| Object-level | ❌ No                  | Only that object    |
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
'''
                        *** Instance Variables in OOP ***

🔹 Definition:
Instance variables are variables whose values are **unique to each object**.  
They are used to store object-specific data and are defined using `self` inside methods (typically in `__init__` or other instance methods).

---

🔹 Characteristics:
- Stored in the object’s namespace.
- Created using `self.variable_name`.
- Each object gets its own copy.
- Changing one object’s instance variable does **not** affect others.

---

🔹 Example Code:
class iv:
    def m1(self, a, b):
        self.inst1 = a
        self.inst2 = b

    def display(self):
        print(self.inst1, self.inst2)

# First object
obj = iv()
obj.m1(10, 20)
obj.inst1 = 100  # Changing inst1 for obj only
obj.display()    # Output: 100 20

# Second object
obj2 = iv()
obj2.m1(20, 50)
obj2.display()   # Output: 20 50
'''

''' 
                        *** What is self in Python OOP? ***

🔹 Definition:
`self` is a reference to the **current instance of the class**.  
It allows access to the instance’s attributes and methods from within the class.

🧠 Think of `self` as a way for the object to refer to itself.

---

🔹 Why is `self` important?

Without `self`, you **cannot**:
1. Declare instance variables  
2. Access instance variables  
3. Modify instance variables  
4. Use instance variables across methods  
5. Call instance methods from within the class

---

🔹 Example:
'''
class Student:
    marks = 70
    def set_data(self, name, age):
        self.name = name        # instance variable
        self.age = age

    def display(self):
        print(self.name, self.age,self.marks)
s1 = Student()
s1.set_data("Arpit", 21)
s1.display()  # Output: Arpit 21

'''
Here:
- `self.name` and `self.age` are instance variables.
- `self` ensures that each object stores its own data.

---

🔹 Summary:
| Keyword | Refers to        | Used for                          |
|---------|------------------|-----------------------------------|
| self    | Current object   | Accessing/modifying instance data |
           
'''

'''
Here’s a clean and complete theory + code note on **Constructors (`__init__`) in Python OOP**, formatted for easy copy-paste and understanding:

```python
                        *** Constructors in Python OOP ***

🔹 Definition:
A **constructor** is a special method in Python used to initialize objects of a class.  
It is automatically called when an object is created.

🔹 Syntax:
```python
def __init__(self, ...):
    # initialization logic
```

- `__init__` is the constructor method.
- `self` refers to the current object.
- You can pass parameters to set initial values for instance variables.

---

🔹 Key Points:
- Constructor is defined using `def __init__(self)`
- It runs **automatically** when an object is created.
- Used to declare and initialize **instance variables**.
- You can have multiple parameters to customize object creation.

'''
# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print('I am init')
#         print(a+b)

# obj = c1(20,10)

'Q. tell the output '
# class c1:
#     def __init__(self,a):
#         self.a=a
#     def m2(self):
#         self.a+=1
# obj1 = c1(5)
# obj1.m2()
# obj1.m2()
# obj1.m2()
# print(obj1.a)

'''
✅ **Accessing a Class Variable via `self`**

You **can read** a class variable using `self`, and it will still refer to the **class variable**, as long as you don’t assign a new value to it.

```python
class MyClass:
    count = 0  # class variable

    def show(self):
        print(self.count)  # ✅ Accessing class variable via self

obj = MyClass()
obj.show()  # Output: 0
---

 ⚠️ **Modifying a Class Variable via `self`**

If you **assign** a value to the class variable using `self`, it creates a **new instance variable** (object-level), shadowing the class variable.

```python
class MyClass:
    count = 0  # class variable

    def modify(self):
        self.count = 10  # ❗ Creates an instance variable, doesn't change class variable

obj1 = MyClass()
obj2 = MyClass()

obj1.modify()
print(obj1.count)  # 10 (instance variable)
print(obj2.count)  # 0  (still using class variable)
print(MyClass.count)  # 0 (unchanged)
---

✅ To Modify the Class Variable Properly

Use the **class name** or `cls` inside a `@classmethod`:

class MyClass:
    count = 0

    @classmethod
    def modify(cls):
        cls.count = 10  # ✅ Modifies class variable

MyClass.modify()
print(MyClass.count)  # 10
---

🧠 Summary Table

| Access Style        | Reads Class Variable? | Modifies Class Variable? | Creates Instance Variable? |
|---------------------|------------------------|----------------------------|-----------------------------|
| `self.var` (read)   | ✅ Yes                 | ❌ No                     | ❌ No                       |
| `self.var = value`  | ❌ No (creates new)    | ❌ No                     | ✅ Yes                      |
| `ClassName.var = v` | ✅ Yes                 | ✅ Yes                    | ❌ No                       |
| `cls.var = value`   | ✅ Yes (in @classmethod) | ✅ Yes                  | ❌ No                       |

'''