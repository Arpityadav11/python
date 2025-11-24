# '''

# # 📘 NumPy Library

# ---

# ## ❓ Q1. What is NumPy?
# - **NumPy (Numerical Python)** is a Python library used for numerical and scientific computing.  
# - It provides:
#   - **N-dimensional arrays (ndarray)** for fast computation  
#   - Mathematical functions (linear algebra, statistics, random numbers)  
#   - Efficient memory usage compared to Python lists  

# ---

# ## ⚙️ How to Use NumPy
# ```python
# # Importing NumPy
# import numpy as np   # 'as' is used to give a short name (alias)

# # Creating an array
# data = np.array([1, 2, 3, 4, 5])

# print(data)   # Output: [1 2 3 4 5]
# ```

# ### ✅ Advantages of NumPy Arrays
# 1. **Faster** than Python lists (written in C for performance)  
# 2. **Memory efficient** (stores homogeneous data types compactly)  

# ---

# ## ❓ Q2. Difference Between Library, Package, and Module

# | Term      | Definition | Example |
# |-----------|------------|---------|
# | **Module** | A single Python file (`.py`) containing functions, classes, or variables | `math.py` |
# | **Package** | A folder containing multiple modules, must include `__init__.py` | `numpy` package |
# | **Library** | A collection of packages and modules designed for a purpose | NumPy library |

# ---

# ## 📝 Quick Recap
# - **NumPy** is a **library**.  
# - Inside NumPy, there are **packages** (like `numpy.linalg`, `numpy.random`).  
# - Each package contains **modules** (Python files with functions).  

# ---

# ## 🎯 Interview-Oriented Notes
# - **Q:** Why is NumPy faster than lists?  
#   **A:** Because it uses contiguous memory blocks and vectorized operations written in C.  

# - **Q:** How do you import NumPy with a short name?  
#   **A:** `import numpy as np`  

# - **Q:** What is the difference between `np.array()` and Python lists?  
#   **A:** NumPy arrays are faster, memory-efficient, and support mathematical operations directly.  


# # 📘 NumPy Array Data Storage

# ## 🔹 Homogeneous Data
# - **NumPy arrays** store **homogeneous data** (all elements of the same type).  
# - Example:
#   ```python
#   import numpy as np
#   arr = np.array([1, 2, 3, 4])
#   print(arr.dtype)   # int64 (all elements are integers)

# - This makes arrays **faster and memory-efficient** compared to Python lists, which can store mixed types.

# ---

# ## 🔹 Python Lists vs NumPy Arrays
# | Feature | Python List | NumPy Array |
# |---------|-------------|-------------|
# | **Data type** | Can store mixed types (int, str, float) | Must store similar types (all int, all float, etc.) |
# | **Storage** | Each element is a full Python object | Stored as raw C data types (compact) |
# | **Speed** | Slower (extra overhead of Python objects) | Faster (contiguous memory, vectorized ops) |
# | **Memory** | More memory usage | Less memory usage |

# ---

# ## 🔹 "Similar but According to Python Objects"
# - When you create a NumPy array, it **infers the data type** from the Python objects you pass.  
# - Example:
#   ```python
#   arr1 = np.array([1, 2, 3])       # dtype = int64
#   arr2 = np.array([1.0, 2.0, 3.0]) # dtype = float64
#   arr3 = np.array(['a', 'b'])      # dtype = <U1 (Unicode string)
#   ```
# - So the **data must be similar**, but the **type is chosen based on Python objects** inside the array.

# ---

# ## 🎯 Interview-Ready Explanation
# - **Q:** Why are NumPy arrays faster than lists?  
#   **A:** Because lists store each element as a Python object (with metadata), 
#   while NumPy arrays store raw homogeneous data in contiguous memory blocks.  

# - **Q:** Can NumPy arrays store mixed data types?  
#   **A:** No, they enforce homogeneity. If mixed types are given, 
#   NumPy will **upcast** to a common type (e.g., int + float → float).  

# ---

# # 📘 NumPy Library - Key Functions & Concepts

# ---

# ## 🔹 Array Attributes
# - **`array.ndim`** → Returns number of dimensions (axes).  
#   ```python
#   arr = np.array([[1,2,3],[4,5,6]])
#   print(arr.ndim)   # 2
#   ```

# - **`array.shape`** → Returns tuple of dimensions (rows, columns).  
#   ```python
#   print(arr.shape)  # (2, 3)
#   ```

# - **`array.size`** → Returns total number of elements.  
#   ```python
#   print(arr.size)   # 6
#   ```

# - **`dtype`** → Shows data type of array elements.  
#   ```python
#   print(arr.dtype)  # int64
#   ```

# ---

# ## 🔹 Array Creation
# - **`numpy.array()`** → Create array from list/tuple.  
#   ```python
#   data = np.array([1,2,3,4,5])
#   ```

# - **`numpy.arange(start, stop, step)`** → Range of evenly spaced values.  
#   ```python
#   np.arange(0, 10, 2)   # [0 2 4 6 8]
#   ```

# - **`astype(datatype)`** → Convert array to another datatype.  
#   ```python
#   arr = np.array([1,2,3])
#   arr = arr.astype(float)
#   ```

# - **`numpy.zeros((rows, cols))`** → Array of zeros.  
#   ```python
#   np.zeros((2,3))   # [[0. 0. 0.] [0. 0. 0.]]
#   ```

# - **`numpy.ones((rows, cols))`** → Array of ones.  
#   ```python
#   np.ones((2,2))    # [[1. 1.] [1. 1.]]
#   ```

# - **`numpy.full((rows, cols), number)`** → Array filled with given number.  
#   ```python
#   np.full((2,3), 7) # [[7 7 7] [7 7 7]]
#   ```

# - **`numpy.linspace(start, end, num=50)`** → Equal spacing between two numbers.  
#   ```python
#   np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1. ]
#   ```

# - **`numpy.logspace(start, end, num=50, base=10)`** → Logarithmic spacing.  
#   ```python
#   np.logspace(1, 3, 3, base=10)  # [10. 100. 1000.]
#   ```

# ---

# ## 🔹 Random Numbers
# - **`random.random()`** → Generates random float between 0 and 1.  
#   ```python
#   import random
#   print(random.random())  # e.g. 0.374
#   ```

# - **`random.randint(start, end)`** → Random integer in range.  
#   ```python
#   import random
#   print(random.randint(1, 10))  # e.g. 7
#   ```

# - **NumPy Random (preferred for arrays):**
#   ```python
#   np.random.rand(3)       # [0.12 0.45 0.89]
#   np.random.randint(1,10,5) # [3 7 2 9 4]
#   ```

# ---

# ## 🔹 `np.fromfunction(function, shape)`
# - Creates array by applying a function to each coordinate.  
#   ```python
#   def func(i, j):
#       return i + j
#   arr = np.fromfunction(func, (3,3), dtype=int) #()-> it is to the row and column here
#   print(arr)
#   # [[0 1 2]
#   #  [1 2 3]
#   #  [2 3 4]]
#   ```

# ---

# ## 🔹 Broadcasting
# - **Definition:** NumPy automatically expands smaller arrays/scalars to match shapes during arithmetic.  
# - **Example:**
#   ```python
#   arr = np.array([1,2,3])
#   print(arr * 2)   # [2 4 6]
#   ```
# - Works when:
#   - Shapes are identical  
#   - One operand is a scalar  
#   - Dimensions are compatible (e.g., `(3,1)` with `(1,3)`)

# ---

# ## 🎯 Interview-Ready Recap
# - `ndim`, `shape`, `size`, `dtype` → Array properties  
# - `array()`, `arange()`, `zeros()`, `ones()`, `full()` → Array creation  
# - `linspace()`, `logspace()` → Spaced sequences  
# - `astype()` → Type conversion  
# - `random` vs `np.random` → Random numbers  
# - `fromfunction()` → Generate arrays via function  
# - **Broadcasting** → Automatic expansion for arithmetic  

# ---
# ---

# # 📘 Vectorization vs Broadcasting in NumPy

# ## 🔹 What is Vectorization?
# - **Definition:** Vectorization is the process of replacing explicit Python loops with array operations.  
# - **Why:** NumPy uses optimized C code internally, so vectorized operations are much faster than
# looping in Python.  
# - **Example:**
# ```python
# import numpy as np

# # Without vectorization (using loop)
# arr = [1, 2, 3, 4]
# squared = [x**2 for x in arr]

# # With vectorization
# np_arr = np.array([1, 2, 3, 4])
# squared = np_arr**2   # [1 4 9 16]
# ```
# 👉 Here, the loop is eliminated. NumPy applies the operation to the whole array at once.

# ---

# ## 🔹 What is Broadcasting?
# - **Definition:** Broadcasting is the ability of NumPy to perform arithmetic operations on arrays of 
# different shapes by automatically expanding the smaller array.  
# - **Rule:** Dimensions must be compatible (either equal or one of them is 1).  
# - **Example:**
# ```python
# arr = np.array([1, 2, 3])
# scalar = 5
# result = arr + scalar   # [6 7 8]
# ```
# 👉 The scalar `5` is **broadcast** across the array, as if `[5, 5, 5]` was created internally.

# Another example with different shapes:
# ```python
# A = np.array([[1], [2], [3]])   # shape (3,1)
# B = np.array([10, 20, 30])      # shape (3,)
# print(A + B)
# # [[11 21 31]
# #  [12 22 32]
# #  [13 23 33]]
# ```
# 👉 NumPy expands shapes `(3,1)` and `(3,)` to `(3,3)` automatically.

# ---

# ## 🔹 Key Differences

# | Feature            | **Vectorization** | **Broadcasting** |
# |--------------------|-------------------|------------------|
# | **Definition**     | Eliminates loops by applying operations to entire arrays | Allows arrays of different shapes to interact |
# | **Focus**          | Speed & simplicity | Shape compatibility |
# | **Requirement**    | Arrays of same shape (or scalar) | Arrays of compatible shapes (dimension = 1 or equal) |
# | **Example**        | `arr**2` (vectorized squaring) | `arr + 5` (scalar broadcasted) |
# | **Benefit**        | Faster execution | Flexible operations without reshaping |

# ---

# ## 🎯 Interview-Ready Recap
# - **Vectorization** → Technique to perform operations without loops, using optimized C code.  
# - **Broadcasting** → Mechanism to handle arrays of different shapes in arithmetic operations.  
# - **Relation:** Broadcasting is often used *within* vectorized operations when shapes differ.  

# ---
# 👉 *Vectorization = “no loops” (speed)*  
# 👉 *Broadcasting = “different shapes can still work together” (flexibility)*  

# ---

# ## 🔹 Broadcasting
# - Definition:A mechanism in numerical libraries(like NumPy) that allows operations on arrays of different shapes
# by automatically expanding the smaller array to match the larger one.
# - **Example**:  
#   ```python
#   import numpy as np
#   a = np.array([1, 2, 3])
#   b = 2
#   print(a + b)   # [3, 4, 5]
#   ```
#   Here, `b` (a scalar) is *broadcast* to `[2, 2, 2]` before addition.

# - **Key Idea**: It’s about **shape compatibility**. The smaller array is conceptually replicated (without actually copying data) to match the larger array’s shape.

# ---

# ## 🔹 Vectorization
# - **Definition**: The process of expressing operations in terms of whole arrays (vectors/matrices) instead of explicit Python loops. It leverages optimized C/Fortran routines under the hood.
# - **Example**:  
#   ```python
#   a = np.array([1, 2, 3])
#   b = np.array([4, 5, 6])
#   print(a * b)   # [4, 10, 18]
#   ```
#   This is vectorized multiplication — no explicit `for` loop is written.

# - **Key Idea**: It’s about **performance and abstraction**. You write operations at the array level, and NumPy executes them efficiently.

# ---

# ## ⚖️ Difference in One Line
# - **Broadcasting** = how arrays of different shapes are aligned for operations.  
# - **Vectorization** = how operations are applied to arrays without explicit loops.

# ---

# ## ✅ Putting Them Together
# - Broadcasting often **enables** vectorization. For example, when you add a scalar to a vector, 
# broadcasting makes the shapes compatible, and vectorization executes the operation efficiently.
# '''

# # import numpy as np
# # data = np.arange(10,-1,-1)
# # data.shape
# # data.ndim
# # print(data,data.shape)
# # print(data.ndim)
# # print(data.size)
# # data.dtype

# # data1 = data.astype(float)
# # print(data1)

# # new = np.zeros((3,6))
# # print(new)
# # new = np.ones((3,6))
# # print(new)

# # new = np.linspace(2,100,5)
# # print(new)

# # np.random.randint(1,100,100)

# '''using the operators  
# data = np.array([1,2,3,4,5,6,7,8,9,10])
# print(data+2)
# print(data-2)
# print(data*2)
# print(data/2)
# print(data//2)
# print(data%2)
# print(data**2)
# '''
# '''
# # broadcasting
# data = np.array([1,2,3,4,5,6,7,8,9,10])
# data2 = np.array([5])
# print(data+data2)
# new = np.array([
#     [[1,2,3],[1,2,3],[1,2,3]],
#     [[1,2,3],[1,2,3],[1,2,3]],
#     [[1,2,3],[1,2,3],[1,2,3]]
# ])

# print(new)
# print(new.shape)
# '''
# '''
# # fancy indexing
# # data = np.array([1,2,3,4,5,6,7,8,9,10])
# # print(data[0])
# # print(data[[1,2,3]])

# # 2-d array
# # data2 = np.array([
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ])
# # print(data2[0,1])
# # print(data2[[0,1,0],[1,1,2]])

# how to access entire column using indexing
# # data2 = np.array([
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ])
# # print(data2[:,1])

# slicing 1-d
# # new = np.array([1,2,3,4,5,6,7,8,9,10])
# # print(new[0:5])
# # print(new[0:5:2])

# slicing 2-d 
# # data2 = np.array([
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ])
# # print(data2[::-1,::-1])

# slicing in 3-d array
# # array3 = np.array([
# #     [[1,2,3],[4,5,6],[7,8,9]],
# #     [[1,2,3],[4,5,6],[7,8,9]],
# #     [[1,2,3],[4,5,6],[7,8,9]]
# # ])
# # print(array3[0:2,0:2,0:2])

# '''
# '''

# ## 🎯 Boolean Indexing Basics
# ```python
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# ```

# ### 1. Equality (`==`)
# ```python
# mask = arr == 30
# print(mask)        # [False False  True False False]
# print(arr[mask])   # [30]
# ```

# ### 2. Inequality (`!=`)
# ```python
# mask = arr != 30
# print(arr[mask])   # [10 20 40 50]
# ```

# ### 3. Greater Than (`>`)
# ```python
# mask = arr > 25
# print(arr[mask])   # [30 40 50]
# ```

# ### 4. Greater Than or Equal (`>=`)
# ```python
# mask = arr >= 40
# print(arr[mask])   # [40 50]
# ```

# ### 5. Less Than (`<`)
# ```python
# mask = arr < 25
# print(arr[mask])   # [10 20]
# ```

# ### 6. Less Than or Equal (`<=`)
# ```python
# mask = arr <= 20
# print(arr[mask])   # [10 20]
# ```

# ---

# ## 🔗 Combining Conditions
# Use **bitwise operators** (`&`, `|`, `~`) instead of Python’s `and`, `or`, `not`.

# ### AND (`&`)
# ```python
# mask = (arr > 15) & (arr < 45)
# print(arr[mask])   # [20 30 40]
# ```

# ### OR (`|`)
# ```python
# mask = (arr < 15) | (arr > 45)
# print(arr[mask])   # [10 50]
# ```

# ### NOT (`~`)
# ```python
# mask = ~(arr > 25)
# print(arr[mask])   # [10 20 25]
# ```

# ---

# ## 🧩 Example with 2D Arrays
# ```python
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# mask = matrix % 2 == 0   # even numbers
# print(matrix[mask])      # [2 4 6 8]
# ```

# ---

# ## ⚡ Key Notes
# - Always wrap conditions in parentheses when combining (`(arr > 10) & (arr < 50)`).
# - Boolean masks must be the same shape as the array.
# - This works for **1D, 2D, and higher-dimensional arrays**.

# ---
# '''

# '''

# # 🧮 NumPy Bitwise Operators – Complete Notes

# ## 1. Bitwise AND (`np.bitwise_and`)
# - **Operation:** Each bit → 1 if both are 1  
# ```python
# d1 = np.array([12, 15])
# d2 = np.array([9, 21])
# np.bitwise_and(d1, d2)   # [8 5]
# ```
# - Example:  
# 12 (00001100) & 9 (00001001) = 8 (00001000)  
# 15 (00001111) & 21 (00010101) = 5 (00000101)

# ---

# ## 2. Bitwise OR (`np.bitwise_or`)
# - **Operation:** Each bit → 1 if either is 1  
# ```python
# np.bitwise_or(d1, d2)    # [13 31]
# ```
# - Example:  
# 12 | 9 = 13  
# 15 | 21 = 31  

# ---

# ## 3. Bitwise XOR (`np.bitwise_xor`)
# - **Operation:** Each bit → 1 if bits differ  
# ```python
# np.bitwise_xor(d1, d2)   # [5 26]
# ```
# - Example:  
# 12 ^ 9 = 5  
# 15 ^ 21 = 26  

# ---

# ## 4. Bitwise NOT / Invert (`np.bitwise_not` or `~`)
# - **Operation:** Flips all bits (two’s complement)  
# ⚠️ Works on **one array only**.  
# ```python
# np.bitwise_not(d1)       # [-13 -16]
# ~d1                      # [-13 -16]
# ```
# - Example:  
# ~12 = -13  
# ~15 = -16  

# ---

# ## 5. Left Shift (`np.left_shift`)
# - **Operation:** Shifts bits of `d1` left by `d2` positions  
# ```python
# np.left_shift(d1, d2)    # [6144 31457280]
# ```
# - Example:  
# 12 << 9 = 6144  
# 15 << 21 = 31457280  

# ---

# ## 6. Right Shift (`np.right_shift`)
# - **Operation:** Shifts bits of `d1` right by `d2` positions  
# ```python
# np.right_shift(d1, d2)   # [0 0]
# ```
# - Example:  
# 12 >> 9 = 0  
# 15 >> 21 = 0  

# ---

# ## ⚡ Quick Comparison Table

# | Operator | Symbol | NumPy Function       | Example (d1=12, d2=9) | Result |
# |----------|--------|----------------------|------------------------|--------|
# | AND      | `&`    | `np.bitwise_and`     | 12 & 9                 | 8      |
# | OR       | `|`    | `np.bitwise_or`      | 12 \| 9                | 13     |
# | XOR      | `^`    | `np.bitwise_xor`     | 12 ^ 9                 | 5      |
# | NOT      | `~`    | `np.bitwise_not`     | ~12                    | -13    |
# | LeftShift| `<<`   | `np.left_shift`      | 12 << 9(n*2^S )        | 6144   | (S is the number of shift
# | RightShift| `>>`  | `np.right_shift`     | 12 >> 9(n/2^S)         | 0      |  n is the number itself)

# ---

# ## 📝 Key Notes
# - All operations are **element-wise** across arrays.  
# - `np.bitwise_not` (or `~`) inverts bits → results in negative numbers due to two’s complement.  
# - Shifts can produce **large values** (left shift) or **reduce to zero** (right shift).  
# - You can use either **NumPy functions** or **Python bitwise symbols** (`&`, `|`, `^`, `~`, `<<`, `>>`) 
# with arrays.

# '''

# '''

# # 🧩 Membership Operators with NumPy Arrays

# ## 1. Using `in` and `not in`
# - In Python, `in` checks if an element exists in a sequence.  
# - With **NumPy arrays**, it works too, but only for **element membership** (not indices).

# ```python
# import numpy as np

# arr = np.array([10, 20, 30, 40])

# print(20 in arr)       # True
# print(50 in arr)       # False
# print(20 not in arr)   # False
# print(50 not in arr)   # True
# ```

# ✅ Works exactly like lists, but under the hood NumPy converts the array to an iterable for membership testing.

# ---

# ## 2. Membership with Strings inside NumPy
# ```python
# arr = np.array(["python", "java", "c++"])

# print("java" in arr)       # True
# print("ruby" not in arr)   # True
# ```

# ---

# ## 3. Membership with Multi-Dimensional Arrays
# ⚠️ Important: `in` checks **row membership** in 2D arrays, not element-wise.

# ```python
# matrix = np.array([[1, 2], [3, 4], [5, 6]])

# print([1, 2] in matrix)    # True  (row exists)
# print(3 in matrix)         # False (3 is inside, but not a row)
# ```

# 👉 If you want **element-wise membership** in multi-dimensional arrays, use `np.isin`.

# ---

# ## 4. `np.isin` (Element-wise Membership)
# This is the **NumPy way** to check membership across arrays.

# ```python
# arr = np.array([10, 20, 30, 40])

# mask = np.isin(arr, [20, 40])
# print(mask)        # [False  True False  True]
# print(arr[mask])   # [20 40]
# ```

# ---

# ## 📝 Quick Table

# | Operator / Function | Works On | Example | Result |
# |---------------------|----------|---------|--------|
# | `in`                | 1D array | `20 in np.array([10,20])` | True |
# | `not in`            | 1D array | `50 not in np.array([10,20])` | True |
# | `in` (2D array)     | Rows     | `[1,2] in np.array([[1,2],[3,4]])` | True |
# | `np.isin`           | Element-wise | `np.isin([10,20,30],[20,40])` | [False True False] |

# ---

# ⚡ **Key Notes**
# - `in` / `not in` → good for quick checks.  
# - `np.isin` → best for **vectorized, element-wise membership** (interview-friendly).  
# - For 2D arrays, `in` checks **rows**, not individual elements.  
# '''

# '''

# # 🧮 Handling NaN, +inf, and -inf in NumPy

# ## 1. Detecting Special Values
# NumPy provides functions to check for NaN and infinities:

# ```python
# import numpy as np

# arr = np.array([1, np.nan, np.inf, -np.inf, 5])

# print(np.isnan(arr))    # [False  True False False False]
# print(np.isinf(arr))    # [False False  True  True False]
# print(np.isposinf(arr)) # [False False  True False False]
# print(np.isneginf(arr)) # [False False False  True False]
# ```

# ---

# ## 2. Filtering / Masking
# Remove NaN and Inf values using boolean masks:

# ```python
# clean = arr[~np.isnan(arr) & ~np.isinf(arr)]
# print(clean)   # [1. 5.]
# ```

# ---

# ## 3. Replacing Values
# Use `np.nan_to_num` to replace NaN and infinities:

# ```python
# arr = np.array([1, np.nan, np.inf, -np.inf, 5])

# fixed = np.nan_to_num(arr, nan=0.0, posinf=9999, neginf=-9999)
# print(fixed)   # [    1.     0.  9999. -9999.     5.]
# ```

# - `nan` → replacement for NaN  
# - `posinf` → replacement for +inf  
# - `neginf` → replacement for -inf  

# ---

# ## 4. Ignoring NaN in Computations
# NumPy has **nan-aware functions** that skip NaN values:

# ```python
# arr = np.array([1, np.nan, 2, np.nan, 3])

# print(np.nanmean(arr))   # 2.0
# print(np.nanmax(arr))    # 3.0
# print(np.nanmin(arr))    # 1.0
# print(np.nansum(arr))    # 6.0
# ```

# ---

# ## 5. Example: Cleaning a Dataset
# ```python
# data = np.array([10, np.nan, 20, np.inf, -np.inf, 30])

# mask = ~np.isnan(data) & ~np.isinf(data)
# clean_data = data[mask]

# print(clean_data)   # [10. 20. 30.]
# ```

# ---

# ## 📝 Quick Table

# | Function          | Purpose                          | Example |
# |-------------------|----------------------------------|---------|
# | `np.isnan(x)`     | Check NaN values                 | `[False True ...]` |
# | `np.isinf(x)`     | Check both +inf and -inf         | `[False True ...]` |
# | `np.isposinf(x)`  | Check positive infinity only     | `[False True ...]` |
# | `np.isneginf(x)`  | Check negative infinity only     | `[False True ...]` |
# | `np.nan_to_num(x)`| Replace NaN/inf with numbers     | `[1,0,9999,-9999,5]` |
# | `np.nanmean(x)`   | Mean ignoring NaN                | `2.0` |
# | `np.nansum(x)`    | Sum ignoring NaN                 | `6.0` |

# ---

# ⚡ **Key Notes**
# - NaN propagates: any arithmetic with NaN → NaN.  
# - Inf arises from division by zero or overflow.  
# - Always clean data before applying algorithms (e.g., ML, stats).  

# '''
# '''
# # 🧮 NumPy Master Cheat Sheet (Functions + Syntax)

# ## 1. Array Creation
# ```python
# np.array([1,2,3])              # Create array
# np.zeros((m,n))                # m x n zeros
# np.ones((m,n))                 # m x n ones
# np.full((m,n), value)          # Fill with constant
# np.arange(start, stop, step)   # Range array
# np.linspace(start, stop, num)  # Evenly spaced values
# np.eye(n)                      # Identity matrix
# np.random.rand(m,n)            # Uniform [0,1)
# np.random.randn(m,n)           # Normal distribution
# np.random.randint(low, high, size) # Random ints
# ```

# ---

# ## 2. Array Inspection
# ```python
# arr.shape        # Dimensions
# arr.ndim         # Number of dimensions
# arr.size         # Total elements
# arr.dtype        # Data type
# arr.itemsize     # Bytes per element
# arr.T            # Transpose
# ```

# ---

# ## 3. Array Manipulation
# ```python
# np.reshape(arr, (m,n))         # Reshape
# np.ravel(arr)                  # Flatten
# np.flatten(arr)                # Flatten copy
# np.concatenate([a,b], axis=0)  # Concatenate
# np.stack([a,b], axis=0)        # Stack arrays
# np.hstack([a,b])               # Horizontal stack
# np.vstack([a,b])               # Vertical stack
# np.split(arr, sections)        # Split array
# np.delete(arr, index, axis)    # Delete elements
# np.insert(arr, index, values)  # Insert elements
# np.append(arr, values, axis)   # Append elements
# np.unique(arr)                 # Unique values
# ```

# ---

# ## 4. Indexing & Slicing
# ```python
# arr[i]                         # Element
# arr[i:j]                       # Slice
# arr[::-1]                      # Reverse
# arr[arr > k]                   # Boolean indexing
# np.where(arr > k)              # Indices where condition holds
# np.isin(arr, [values])         # Membership check
# ```

# ---

# ## 5. Mathematical Operations
# ```python
# np.add(a,b)                    # Addition
# np.subtract(a,b)               # Subtraction
# np.multiply(a,b)               # Multiplication
# np.divide(a,b)                 # Division
# np.power(a,n)                  # Power
# np.exp(a)                      # Exponential
# np.log(a)                      # Natural log
# np.sqrt(a)                     # Square root
# np.dot(a,b)                    # Dot product
# np.cross(a,b)                  # Cross product
# np.sum(arr, axis)              # Sum
# np.prod(arr, axis)             # Product
# ```

# ---

# ## 6. Statistical Functions
# ```python
# np.mean(arr, axis)             # Mean
# np.median(arr, axis)           # Median
# np.std(arr, axis)              # Standard deviation
# np.var(arr, axis)              # Variance
# np.min(arr, axis)              # Minimum
# np.max(arr, axis)              # Maximum
# np.argmin(arr, axis)           # Index of min
# np.argmax(arr, axis)           # Index of max
# np.percentile(arr, q)          # Percentile
# ```

# ---

# ## 7. Linear Algebra
# ```python
# np.linalg.inv(A)               # Inverse
# np.linalg.det(A)               # Determinant
# np.linalg.eig(A)               # Eigenvalues & vectors
# np.linalg.norm(A)              # Norm
# np.linalg.solve(A,b)           # Solve Ax=b
# np.linalg.matrix_rank(A)       # Rank
# ```

# ---

# ## 8. Random Module
# ```python
# np.random.seed(seed)           # Seed
# np.random.shuffle(arr)         # Shuffle
# np.random.choice(arr, size)    # Random sample
# np.random.permutation(arr)     # Random permutation
# ```

# ---

# ## 9. Handling NaN & Inf
# ```python
# np.isnan(arr)                  # Detect NaN
# np.isinf(arr)                  # Detect Inf
# np.isposinf(arr)               # Detect +inf
# np.isneginf(arr)               # Detect -inf
# np.nan_to_num(arr, nan=0, posinf=999, neginf=-999) # Replace
# np.nanmean(arr)                # Mean ignoring NaN
# np.nansum(arr)                 # Sum ignoring NaN
# ```

# ---

# ## 10. Bitwise & Logical
# ```python
# np.bitwise_and(a,b)            # AND
# np.bitwise_or(a,b)             # OR
# np.bitwise_xor(a,b)            # XOR
# np.bitwise_not(a)              # NOT
# np.left_shift(a,n)             # Shift left
# np.right_shift(a,n)            # Shift right

# np.logical_and(cond1, cond2)   # Logical AND
# np.logical_or(cond1, cond2)    # Logical OR
# np.logical_not(cond)           # Logical NOT
# ```

# ---

# ## 11. Sorting & Searching
# ```python
# np.sort(arr)                   # Sort
# np.argsort(arr)                # Indices of sorted array
# np.partition(arr, k)           # Partition around kth element
# np.searchsorted(arr, value)    # Index to insert value
# ```

# ---

# ## 12. File I/O
# ```python
# np.loadtxt('file.txt')         # Load text file
# np.genfromtxt('file.csv', delimiter=',') # Load CSV
# np.savetxt('file.txt', arr)    # Save to text
# np.save('file.npy', arr)       # Save binary .npy
# np.load('file.npy')            # Load binary .npy
# np.savez('file.npz', a=arr1, b=arr2) # Save multiple arrays
# ```

# ---

# ## 📝 Interview-Favorite Functions
# - **Array creation:** `np.arange`, `np.linspace`, `np.eye`  
# - **Manipulation:** `np.reshape`, `np.concatenate`, `np.delete`  
# - **Indexing:** Boolean indexing, `np.where`, `np.isin`  
# - **Math:** `np.dot`, `np.cross`, `np.exp`, `np.log`  
# - **Stats:** `np.mean`, `np.std`, `np.argmax`  
# - **Linear algebra:** `np.linalg.inv`, `np.linalg.det`, `np.linalg.eig`  
# - **NaN handling:** `np.isnan`, `np.nan_to_num`, `np.nanmean`  
# - **Random:** `np.random.seed`, `np.random.choice`  
# - **Sorting:** `np.sort`, `np.argsort`  

# ---
# '''
# import numpy as np
# data = np.array([1,2,3,4,5,6])
# print(data)
data = [1,2,3,4]
print(data)