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

It is a way to change the behavior of existing function or method without writing code in to it
we yse decorator with @ symbol followed by decorator name

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
| Type             | Scope        | Shared Across Objects  | Accessed By         |
|------------------|--------------|-------------------------|---------------------|
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
# class Student:
#     marks = 70
#     def set_data(self, name, age):
#         self.name = name        # instance variable
#         self.age = age

#     def display(self):
#         print(self.name, self.age,self.marks)
# s1 = Student()
# s1.set_data("Arpit", 21)
# s1.display()  # Output: Arpit 21

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

'''
destructor
destructors are used to destroy the attirbutes, methods and even the object itself.
used del to destroy
'''
# class c:
#     data = 90
#     def m1(self,a):
#         self.a=a
#         print('i am m1')
# obj1 = c()
# del obj1.data
# print(obj1.data) #error that data doesn't exist
# del obj1.a
# print(obj1.a)  #error that a doesn't exist
'''

                    *** Decorators in Python ***

🔹 Definition:
A **decorator** is a design pattern in Python that allows you to **modify the behavior of a function or method**  
without changing its actual code. Decorators are applied using the `@decorator_name` syntax.

---

🔹 Syntax & Flow:
```python
def mydecorator(func):
    def wrapper():
        # Pre-processing
        func()
        # Post-processing
    return wrapper

@mydecorator
def display():
    print("I am the original function")
```

🔹 Output:
```
Wrapper: Before function
I am the original function
Wrapper: After function
```

---

🔹 Decorator Practice Example:
```python
def multiply_10(fun):
    def wrapper(a, b):
        print(10 * fun(a, b))
    return wrapper

@multiply_10
def sub(a, b):
    return a - b

sub(2, 10)  # Output: -80
```

---

🔹 Decorators Explained:

Decorators allow you to **wrap** a function and **extend or alter its behavior** without modifying its source code.

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
- Instance variables are **unique to each object** and defined using `self`.

🧠 Summary:
| Type             | Scope        | Shared Across Objects  | Accessed By         |
|------------------|--------------|-------------------------|---------------------|
| Static Variable  | Class-level  | ✅ Yes                 | Class or object     |
| Instance Variable| Object-level | ❌ No                  | Only that object    |
```

---
'''

'''
Write a decorator to count the recursion call apply this decorator on the factorial of a number
here we have to use the 'nonlocal' keyword which is used to identify or tell that the variable we are using
is no local. Non local is used only when you are using the nested functions.
'''
# count = 0

# def counter(fun):
#     def wrapper(b, fact=1):
#         global count
#         count += 1
#         return fun(b, fact)
#     return wrapper
        
# @counter
# def factorial(a,fact=1):
#     fact *=a
#     if a==1:
#         return fact
#     else:
#         return factorial(a-1,fact)
# print(factorial(5))
# print(count)
'''
    Using destructor inside the method
'''
# class c4:
#     data = 900
#     def m1(self):
#         del self.data # the data will get deleted when method is executed
# obj = c4()
# print(obj.data)

'''
                        *** Inheritance in Python OOP ***

🔹 Definition:
Inheritance is an object-oriented programming feature that allows a class (child) to **inherit properties and behaviors**  
from another class (parent). It promotes **code reuse**, **modularity**, and **hierarchical design**.

---

🔹 Key Terms:

- **Super Class / Parent Class**  
  The class whose properties and methods are inherited.  
  Example: `class Animal:` → Animal is the parent class.

- **Base Class / Child Class**  
  The class that inherits from the parent class.  
  Example: `class Dog(Animal):` → Dog is the child class.

---

🔹 Types of Inheritance:

1. **Single Inheritance**
   - One child class inherits from one parent class.
   ```python
   class A:
       pass

   class B(A):
       pass
   ```

2. **Multiple Inheritance**
   - One child class inherits from **multiple parent classes**.
   ```python
   class A:
       pass

   class B:
       pass

   class C(A, B):  # C inherits from both A and B
       pass
   ```

   🔸 Subtypes:
   - **Multiple Upward**: One child inherits from multiple parents.
   - **Multiple Downward**: One parent is inherited by multiple children.

3. **Multilevel Inheritance**
   - A chain of inheritance across multiple levels.
   ```python
   class A:
       pass

   class B(A):
       pass

   class C(B):
       pass
   ```

4. **Hierarchical Inheritance**
   - Multiple child classes inherit from a single parent class.
   ```python
   class A:
       pass

   class B(A):
       pass

   class C(A):
       pass
   ```

---

🧠 Summary Table:

| Type                  | Structure                          | Example Classes        |
|-----------------------|-------------------------------------|------------------------|
| Single Inheritance    | One parent → One child              | A → B                  |
| Multiple Inheritance  | Multiple parents → One child        | A, B → C               |
| Multilevel Inheritance| Parent → Child → Grandchild         | A → B → C              |
| Hierarchical          | One parent → Multiple children      | A → B, A → C           |

                    *** Hybrid Inheritance in Python OOP ***

🔹 Definition:
**Hybrid inheritance** is a combination of two or more types of inheritance (e.g., single, multiple, multilevel, hierarchical)  
within the same program. It allows flexible and complex class relationships.

---

🔹 Why Use Hybrid Inheritance?
- To model real-world relationships more accurately.
- To reuse code across multiple layers and branches.
- To combine benefits of different inheritance types.

---

🔹 Example Structure:
Hybrid inheritance often looks like a **mix of hierarchical + multilevel + multiple** inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):  # Single inheritance
    def show_b(self):
        print("Class B")

class C(A):  # Hierarchical inheritance
    def show_c(self):
        print("Class C")

class D(B, C):  # Multiple inheritance
    def show_d(self):
        print("Class D")

'''

'''
# 🧠 `super()` Class in Python

## 📘 Theory
The `super()` class in Python is used to refer to the **parent class** from within a **child class**, especially when dealing with **inheritance**. 
It allows you to call methods (including constructors) from the parent class without explicitly naming it.

This is particularly useful when:
- You override a method in the child class but still want to use the parent’s version.
- You’re working with **multiple inheritance**, and Python’s **Method Resolution Order (MRO)** decides which parent method to call.
- You want to write **clean, maintainable code** that respects hierarchy and avoids duplication.

Instead of:
```python
ParentClass.method(self)
```
You use:
```python
super().method()
```
This ensures flexibility and correctness, especially in complex inheritance chains.

---

## 🧪 Code Example

```python
class Club:
    def welcome(self):
        print("Welcome to the gaming club!")

class ValorantTeam(Club):
    def welcome(self):
        super().welcome()  # Calls parent method
        print("Welcome to the Valorant division!")

team = ValorantTeam()
team.welcome()
```

**Output:**
```
Welcome to the gaming club!
Welcome to the Valorant division!
```

---

## 🎯 Common Interview Questions
- What is the purpose of `super()` in Python?
- How does `super()` differ from directly calling `ParentClass.method(self)`?
- Can you use `super()` in constructors (`__init__`)? Why would you?
- How does Python determine which method `super()` calls in multiple inheritance?
- What is MRO (Method Resolution Order) and how does it relate to `super()`?
```

'''


'''Q. develop a inventory management system using oop concept'''
# class Inventory:
#     def __init__(self):
#         self.num_of_products = 0
#         self.price = 100  
#         self.cost = 70    
#         self.amount = 0
#         self.investment = 0

#     def purchase_item(self, num):
#         self.num_of_products += num
#         self.investment += num * self.cost
#         print(f"Purchased {num} items. Investment: ₹{self.investment}")

#     def sell_item(self, num):
#         if num <= self.num_of_products:
#             self.num_of_products -= num
#             self.amount += num * self.price
#             print(f"Sold {num} items. amount: ₹{self.amount}")
#         else:
#             print("Not enough stock to sell.")

#     def show_status(self):
#         print(f"Products in stock: {self.num_of_products}")
#         print(f"Total investment: ₹{self.investment}")
#         print(f"Total amount: ₹{self.amount}")
#         print(f"Profit: ₹{self.amount - self.investment}")

# store = Inventory()
# store.purchase_item(25)
# store.sell_item(80)
# store.show_status()

'''
attr - product_name,quantity,price,amount
mthd - sell , buy, update, display product list
'''

# class ims:
#     # constructor
#     def __init__(self):
#         self.product_name=[]
#         self.quantity=[]
#         self.data={}
#         self.price=[]
#         self.SP=[]
#         self.investment = []
#         self.profit=[]
#         self.amount=[]
    
#     # to purchase the items or add product to the inventory
    
#     def add(self,p_name,p_quantity,pc_price):
#         self.product_name.append(p_name)
#         self.quantity.append(p_quantity)
#         self.price.append(pc_price)
#         self.SP.append((pc_price*0.2)+pc_price)
#         self.investment.append(pc_price*p_quantity)
#         self.profit.append(0)
#         self.amount.append(0)
#         for i in range(len(self.product_name)):
#             self.data[self.product_name[i]] = {'quantity':self.quantity[i],'cost':self.price[i],'investment':self.investment[i],'SP':self.SP[i],'amount':self.amount[i],'profit':self.profit[i]}       
    
#     # used to update the inventory data
    
#     def update(self,p_name):
#         if self.data.get(p_name) == None:
#             print('the product doesnt exist')
#         else:
#             p_quantity=int(input("enter the quantity : "))
#             p_cost = int(input("enter the cost of product : "))
#             self.value = self.data.get(p_name)
#             self.value['quantity']=p_quantity
#             self.value['cost']=p_cost
#             self.value['investment']=self.value['cost']*self.value['quantity']
         
#     # selling the products
    
#     def sell(self,p_name):
#                 if self.data.get(p_name) == 'None':
#                     print('the product doesnt exist')
#                 else:
#                     p_quantity=int(input("enter the quantity : "))
#                     self.value = self.data.get(p_name)
#                     if self.value['quantity']>=p_quantity:
#                         self.value['quantity']-=p_quantity
#                         self.value['amount']=self.value['SP']*p_quantity
#                         self.value['profit']=self.value['amount']-self.value['investment']
#                     else:
#                         print('insufficient stock')
    
#     # display the records of the inventory
    
#     def display_record(self):
#         self.revenue = 0
#         self.netInvestment=0
#         self.netProfit = 0
#         print(self.data)
#         for i in self.product_name:
#             self.val = self.data.get(i)
#             self.revenue += self.val['amount']
#             self.netInvestment += self.val['investment']
#         self.netProfit = self.revenue - self.netInvestment
#         print(f'the net revenue of the session is: {self.revenue}')
#         print(f'the net investment of the session is: {self.netInvestment}')
#         print(f'the net profit of the session is: {self.netProfit}')

# mahindra_service=ims()
# while True:
#     choice = input('''enter what you want
#                    press 1 if you want to buy item
#                    press 2 if you want to update the purchase
#                    press 3 if you want to sell item 
#                    press other key to exit''')
    
#     if choice=='1':
#         product=input("enter the product name :  ")
#         quantity=int(input("enter the quantity : "))
#         cost = float(input("enter the cost of product : "))
#         mahindra_service.add(product,quantity,cost)
        
#     elif choice=='2':
#         product=input("enter the product name :  ")
#         mahindra_service.update(product)
        
#     elif choice=='3':
#         product=input("enter the product name :  ")
#         mahindra_service.sell(product)
        
#     else:
#         break
        
# mahindra_service.display_record()

# def f(x, y=[]): #kyunki jo list h vo mutable h toh address same rhega uska 
#                 # so output k time list jo h vo as it is jayegi function k pas
#    y.append(x) 
#    return y
# print(f(1))
# print(f(2))

'''constructor in inheritance'''
# class c1:
#     age = 90
#     def __init__(self):
#         print('i am c1 constructor')
# class c2(c1):
#     def __init__(self):
#         print('i am c2 constructor ')
#         super().__init__() # this is calling the constructor of parent class
        
'''
# 🧠 Encapsulation in Python

## 📘 Theory
Encapsulation is an **object-oriented programming (OOP)** concept that focuses on **restricting direct access to data** 
and exposing it only through controlled interfaces (methods). 
In Python, this is typically done by making attributes **private** using double underscores (`__`).

This helps:
- Protect sensitive data from being modified accidentally
- Enforce rules or validation before accessing/modifying data
- Maintain clean and secure class design

**Key idea**: You hide internal details and expose only what's necessary — like giving permission through methods.

---

## 🧪 Code Example

```python
class Player:
    def __init__(self, name, score):
        self.__name = name        # private attribute
        self.__score = score      # private attribute

    def get_score(self):          # public method to access score
        return self.__score

    def set_score(self, new_score):  # controlled way to update score
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Invalid score!")

player = Player("Arpit", 100)

# Direct access fails
print(player.__score)  # AttributeError

# Access via method
print(player.get_score())  # ✅ 100

# Update via method
player.set_score(150)
print(player.get_score())  # ✅ 150

# 🧠 Types of Encapsulation in Python

## 📘 Theory

Encapsulation can be categorized into two types based on how strictly access to internal data is controlled:

### 1. ✅ Partial Encapsulation
- Implemented using a **single underscore (`_`)** before an attribute or method.
- This is a **developer-level convention** indicating that the member is intended for internal use.
- The **Python interpreter does not enforce access restrictions** — the attribute is still accessible from outside the class.
- Used when you want to signal "protected" access but allow flexibility.

```python
class Game:
    def __init__(self):
        self._rank = "Diamond"  # partial encapsulation

game = Game()
print(game._rank)  # ✅ Accessible, but discouraged
```

### 2. 🔒 Full Encapsulation
- Implemented using a **double underscore (`__`)** before an attribute or method.
- The **Python interpreter enforces access restrictions** through **name mangling**.
- The attribute cannot be accessed directly using `object.__attribute` — it must be accessed via class methods.

```python
class Player:
    def __init__(self):
        self.__score = 100  # full encapsulation

    def get_score(self):
        return self.__score

player = Player()
print(player.get_score())  # ✅ Allowed
print(player.__score)      # ❌ AttributeError
```

---

## 🎯 Common Interview Questions
- What is the difference between partial and full encapsulation in Python?
- How does the Python interpreter treat `_attribute` vs `__attribute`?
- What is name mangling and how does it relate to full encapsulation?
- Why might a developer choose partial encapsulation over full?
-How does partial encapsulation differ from full encapsulation?

- Why might you choose partial encapsulation in a real-world system?

- How does full encapsulation improve data security?

- Can you give an example of a fully encapsulated class?
```

# 🧠 Getter and Setter Methods in Encapsulation

## 📘 Theory

In encapsulation, **getter and setter methods** are used to **access and modify private attributes** of a class. 
Since private attributes (defined with `__`) cannot be accessed directly, these methods act as **controlled interfaces**.

- **Getter**: Retrieves the value of a private attribute.
- **Setter**: Updates the value of a private attribute, often with validation logic.

This ensures:
- Data protection
- Controlled access
- Validation before modification

---

## 🧪 Code Example

```python
class Player:
    def __init__(self):
        self.__score = 0  # private attribute

    # Getter method
    def get_score(self):
        return self.__score

    # Setter method
    def set_score(self, value):
        if value >= 0:
            self.__score = value
        else:
            print("Invalid score!")

player = Player()

# Accessing private attribute via getter
print(player.get_score())  # ✅ 0

# Modifying private attribute via setter
player.set_score(100)
print(player.get_score())  # ✅ 100

# Trying to set invalid value
player.set_score(-50)      # ❌ Invalid score!
```

---

## 🎯 Common Interview Questions
- What are getter and setter methods in Python?
- Why are getter and setter methods used in encapsulation?
- Can you access private attributes without getters/setters?
- How do you implement validation in a setter method?
- What is the difference between direct access and using getters/setters?
```

'''        

'''
program
create a class which have account number and balance and the account number and balance can't be accessed through object
but the data should be displayed
'''
# class bank:
#     def __init__(self,a,b,c):
#         self.__acc_num = a
#         self.__pass = b
#         self.__balance = c
#     def display(self):
#         print(f'the account number is :{self.__acc_num}')
#         print(f'the password for this account number is : {self.__pass}')
#         print(f'the balance for this account number is : {self.__balance}')
# obj = bank(123,'pass123',5000)
# obj.display()

'''
# 🧠 Data Abstraction (Abstract Class / ABC)

## 📘 Theory

**Data Abstraction** is an object-oriented programming concept that focuses on **hiding internal implementation details** and exposing only the essential functionality.

In Python, abstraction is implemented using **abstract classes** from the `abc` module:
- An **abstract class** defines methods that **must be implemented** by any subclass.
- These methods are marked with the `@abstractmethod` decorator.
- Abstract classes **cannot be instantiated directly**.
- This enforces a **contract**: any subclass must implement the abstract methods.

---

## 🧪 Code Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # it is a keyword in python which is used whenever we declare a block of code but want to leave it empty for future we use pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# shape = Shape()         # ❌ Error: Can't instantiate abstract class
square = Square(5)        # ✅ Valid
print(square.area())      # Output: 25
print(square.perimeter()) # Output: 20
```

## 🎯 Common Interview Questions
- What is abstraction in Python and how is it implemented?
- What is the role of `@abstractmethod`?
- Can you instantiate an abstract class?
- What happens if a subclass does not implement all abstract methods?
- How is abstraction different from encapsulation?
```
'''

'''
# 🧠 Polymorphism in Python

## 📘 Theory

**Polymorphism** is an object-oriented programming concept where a **single method or function behaves differently based on the object**
that calls it. The word "poly" means many, and "morph" means forms — so polymorphism means **many forms**.

In Python, polymorphism allows:
- The same method name to be used across different classes.
- Each class to implement the method in its own way.
- Code to be more flexible and reusable.

🎯 Common Interview Questions
What is polymorphism in Python?

How does Python support polymorphism?

What is the difference between method overloading and method overriding?

Can you give an example of polymorphism using classes?

How does polymorphism improve code flexibility and reusability?

## 🧪 Code Example
'''
# class valorant:
#     def character(self):
#         print('called agents')

# class bgmi:
#     def character(self):
#         print('called characters')

# class eFootball:
#     def character(self):
#         print('called football-players')

# g1 = valorant()
# g2 = bgmi()
# g3 = eFootball()
# data = [g1,g2,g3]
# for game in data:
#     game.character()
''' 
# 🦆 Duck Typing in Python

## 📘 Theory

**Duck Typing** is a dynamic typing concept in Python where the **type of an object is determined by its behavior**, not its class.

> "If it walks like a duck and quacks like a duck, it's treated like a duck."

In Duck Typing:
- You don’t check the type of an object.
- You just call the method or access the attribute you expect it to have.
- If the object supports it, it works — regardless of its class.

This supports **polymorphism without inheritance**.

---

## 🧪 Code Example

```python
class Cat:
    def make_sound(self):
        print('meow')

class Dog:
    def make_sound(self):
        print('bark')

def call(animal):
    animal.make_sound()

call(Cat())  # Output: meow
call(Dog())  # Output: bark
```

Here, both `Cat` and `Dog` have a `make_sound()` method. The `call()` 
function works with any object that defines this method — no need for a common parent class.

---

## 🎯 Common Interview Questions
- What is duck typing in Python?
- How does duck typing differ from traditional polymorphism via inheritance?
- Can you give an example of duck typing?
- What are the advantages and risks of duck typing?
```

'''
class cat:
    def make_sound(s):
        print('meow')

class dog:
    def make_sound(s):
        print('bark')
        
def call(a):
    a.make_sound()

call(cat())
call(dog())