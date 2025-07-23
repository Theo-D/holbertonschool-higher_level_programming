# Python - Everything is Object - Understanding the interactions between names, identities and values.

## Introduction

In Python, the behavior and handling of names and values can be confusing. Python's philosophy comes at a price and the need for simplicity and fast scripting can lead to behind the scenes shenanigans that might be hard to grasp for someone not used to the language.
Let's walk through some of its features.

---

## ID and Type

- Every object in Python has:
  - A **type**: What kind of data is holds (`int`, `list`, `str`, etc.)
  - An **identity**: A unique identifier retrieved by using `id()` (which is its memory address in the CPython implementation). <br>
- In some cases, it can also be assigned a:
  - A **value**: That is refered to by a **name** (*a* in the following code snippet).

```python
>>> a = 512
>>> print(type(a))
<class 'int'>
>>> print(id(a))
11760968
>>> print(a)
512
```

## Mutable and immutable objects.

A **mutable object** is an object that can have its value or the data they hold modified without changing its identity.

for instance:

```python
>>> list_1 = [1, 2, 3]
>>> print(list_1)
[1, 2, 3]
>>> print(id(list_1))
125283079981888
>>> list_1 += [4]
>>> print(list_1)
[1, 2, 3, 4]
>>> print(id(list_1))
125283079981888
```
We can see that eventhough the **value** has changed (from `[1, 2, 3]` to `[1, 2, 3, 4]`), its **identity** did not (it remained `12528307998188`).

On the other hand an **immutable object** cannot be altered once created and must be allocated a new space in memory.
Let's use a tuple as an example:

```python
>>> tuple_1 = (1, 2)
>>> print(id(tuple_1))
125283078379072
>>> to_add = (3, )
>>> tuple_1 += to_add
>>> print(tuple_1)
(1, 2, 3)
>>> print(id(tuple_1))
125283078548160
```

This time when we added an element to the tuple, its **value** changed as well as its **identity**. This is because python created a new object named `tuple_1` under the hood to assign it the value `(1, 2, 3)`.

### Mutable Object types:

**Built-in mutable** objects type:
  - Lists
  - Dictionaries
  - Sets

**By default, custom classes and objects are mutable.**

### Immutable Object types:

**Built-in immutable** objects types:

  - Numbers (int, float...)
  - Booleans
  - Strings
  - Bytes
  - Tuples

## Why does mutability matters when programming in python:

Beneath is a non-exhaustive list of specific mutability related issues that one could encounter:

### Aliasing Variables:
As we saw earlier, a mutable object can have its value changed without affecting its memory address, when on the other hand, a immutable objects must be assigned to a different memory address when modified. This affects how **aliases** work. Because aliases are a reference to the memory address of an object, modifying the value of an alias pointing to a *mutable* object will modify the value of the object aliased, so tread carefully. However, it is safer to alias **immutable** objects because each time its value is updated, the memory address will be too, in which case, modifying the alias won't affect the aliased object.

### Mutating Arguments in Functions:
Python allows functions to modify objects that are passed to it.

```python
>>> def add_to_new_list(list, num):
...     list.append(num)
...     return list
...
>>> list_1 = [1, 2, 3]
>>> add_to_new_list(list_1, 4)
[1, 2, 3, 4]
>>> print(list_1)
[1, 2, 3, 4]
```
In the above example, the input data was modified by the function. This behaviour does not occur for an object of immutable type like int:

```python
>>> def add_two(a):
...     return a + 2
...
>>> num = 1
>>> add_two(num)
3
>>> print(num)
1
```

If the intended behaviour was not to modify the input of `add_to_new_list()`, a copy of the original object should have been used and mofified to preserve the input's object value.

### Using Mutable Default Values:
Python provides the ability to assign default value on function definition like so:
`def add_to_new_list(num, list=[]):`
Here, the argument `list` has been assigned a mutable object type as a default value (an empty list in this case).

It is a dangerous practice because function default values are defined when the Python interpreter first parses the function which implies that between every subsequent call to the function, the argument will retain the value it was assigned during the function execution.

By assigning an empty list as default value to the argument `list` you might expect the following output:

```python
>>> def add_to_new_list(num, list=[]):
...     list.append(num)
...     return list
...
>>> add_to_new_list(4)
[4]
>>> add_to_new_list(4)
[4]
>>> add_to_new_list(4)
[4]
```

However, because a list is a mutable type and its address does not change when modified, it does not change either between call of the function, which gives us the following output:

```python
>>> def add_to_new_list(num, list=[]):
...     list.append(num)
...     return list
...
>>> add_to_new_list(4)
[4]
>>> add_to_new_list(4)
[4, 4]
>>> add_to_new_list(4)
[4, 4, 4]
```

Better practice wuld have been to assign `list` to `None`, like so:
`def add_to_new_list(num, list=None):`

### Storing Mutable Objects in Tuples:

Tuples might be immutable objet types, they can still store mutable object types like lists.

Let's consider the following tuple:

```python
>>> tuple = (1, [2])
>>> tuple[0] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

We get a `TypeError` because tuples, being immutable objects, do not support assignement. However, the second item of the tuple being a list, we can proceed like so:

```python
>>> tuple = (1, [2])
>>> tuple[1][0] = 3
>>> print(tuple)
(1, [3])
```

Tuples do not allow the id of the items they contain to change. But as we've seen earlier, in the case of a mutable object, its value can change without affecting its identifier. that's what allows us to modify the value of an item of a list, eventhough it is contained in an immutable tuple.

## Side note about object creation and optimization in Python:

Python is a flexible programming language that offers various mechanisms to optimize performance and memory usage.
I will walk you through some of those methods of optimization, namely: **Aliases**, **slots** and **object interning**

### Aliases :

Python uses aliases to avoid the creation of objects with equivalent value given the following:

```python
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 10
>>> b = 10
>>> a is b
True
>>> a == b
True
```
In the above exemple an alias was used to reuse the value of `a` as the value of `b`. They are both equal and identical, which means two values occupy the same space in memory, dividing its the need for space by 2.

### __dicts__  vs __slots__ :

When an user defines a class, python autmatically map its datas to a dictionnary. This newly created dictionnary can be accessed through the magic method `__dict__`

```python
>>> class DictData:
...     def __init__(self):
...             pass
...
>>> dict_data = DictData()
>>> dict_data2 = DictData()
>>> # We dynamically create new attributes
>>> dict_data.a = 10
>>> dict_data2.a = 10
>>>
>>> print(dict_data.__dict__)
{'a': 10}
>>> print(dict_data2.__dict__)
{'a': 10}
>>> # We now test if they are two different objects (which, they are)
>>> dict_data2.__dict__ is dict_data.__dict__
False
```

As we can see for every instance of a class, a new dictionnary is created. On the long run and for large data sets it can become very memory-hungry and ineficient.
That's where `__slots__` come in handy.

```python
>>> class SlotData:
...     __slots__ = ["a", "b"]
...
>>> slot_data = SlotData()
>>> slot_data.a = 10
>>> slot_data.b = 20
>>> slot_data.c = 30
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SlotData' object has no attribute 'c'
>>>
>>> print(slot_data1.__dict__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SlotData' object has no attribute '__dict__'. Did you mean: '__dir__'?
```

When using slots, you can't dynamically allocate attributes to an instance outside of what was explicitely defined in `__slots__ = [ ... ]`.
As we can see above, the SlotData class has no attribute `__dict__`, this allows us to keep in check the attribute creation and to have better control over object creation and memory consumption.

### Object interning :

Object interning in Python is an optimization technique where certain immutable objects are reused rather than recreated to save memory and speed up performance.

Python interns small integers in the range defined by the **most used integers**: `NSMALLNEGINTS` (-5 included) to `NSMALLPOSINTS` (257 excluded), meaning these integers are preallocated and reused throughout a program. What it means in practice is that typing `a = 10` will not create any new object, python will simply reuse allocated positive int, however `a = 257` will create a new object, the value of a being greater than `NSMALLPOSINTS`.

Similarly, string interning involves reusing identical immutable strings, especially short strings without spaces (less than 20 characters), strings that look like identifiers (tipycally short strings with underscores in them) or strings that are explicitly interned using sys.intern().

By interning frequently used small integers and strings, Python reduces memory consumption improving efficiency overall.

---

Sources:
- https://medium.com/@datasciencejourney100_83560/python-interning-for-each-data-types-397b0ba70986
- https://realpython.com/python-mutable-vs-immutable-types/
- https://nedbatchelder.com/text/names.html
- python3 interpreter
