# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are similar to lists in that they support both indexing and slicing. They are different in that they are immutable (i.e., entries in a tuple cannot be changed). Also, the syntax for a tuple uses parentheses e.g., (1, 2, 3) while lists use brackets e.g., [1, 2, 3].

>> As a key must be immutable, tuples will work as keys in dictionaries because all of its elements are immutable. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are similar to lists in that they are a collection of elements. They are different in that sets require items to be hashable, are immutable, are unordered and must contain unique elements. In addition, math operations related to set theory can be applied to sets. 

Example 1: Counting the number of times the number 2 appears in a list
```python
l = [1, 1, 1, 2, 2, 2, 3, 3, 4]
l.count(2)
```

Example 2: Isolating elements that are common to sets
```python
s1 = {1, 2, 3}
s2 = {2, 4, 5}
s1.intersection(s2)
```

Example 3: Using a set to identify unique elements
```python
l = [1, 1, 1, 2, 2, 2, 3, 3, 4]
set(l)
```

>> Finding an element (i.e., membership testing) in a set is much faster than in a list due to the requirement that items be hashable in a set. As a result, hashing allows membership testing in sets to take a constant, fixed time, whereas membership testing in lists is approximately proportional to the list's length.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda function allows one to define an anonymous, "just-in-time" function in a one line expression. It is generally designed for simple functions that do not need to be recalled again, and have an implicit return statement. Lambda functions are commonly used with map(), filter() and reduce().

Example 1: lambda function that reverses a string
```python
reverse = lambda string: string[::-1]
```

Example 2: Using a lambda in the key argument to sorted (to sort by year)
```python
car_model_year = [('honda', 'civic', 2010), 
                  ('nissan', 'altima', 2008),
                  ('toyota', 'camry', 2009)]

sorted(car_model_year, key = lambda x: x[2])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow the building of lists using a one-line for loop. Map applies a function to every element in a sequence iterable and returns a new sequence iterable changed by the function. Filter allows the filtering of a sequence iterable using a function. Their capabilities differ in that map and reduce both require the definition of a function to operate. 

Example 1: List comprehension vs. map - creating a list of cubed values
```python
[x ** 3 for x in xrange(11)]
```

```python
map(lambda x: x ** 3, xrange(11))
```

Example 2: List comprehension vs. filter - filtering for words beginning with 'j'
```python
l = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']
[x for x in l if x[0] == 'j']
```

```python
l = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']
filter(lambda x: x[0] == 'j', l)
```

Example 3: Set comprehension - creating a set of odd numbers
```python
{x for x in xrange(11) if not x % 2 == 0}
```

Example 4: Dictionary comprehension - creating a dictionary with keys being x and values being x ** 2
```python
{x: x ** 2 for x in range(11)}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513  

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

>> q5_datetime.py updated

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

>> q6_strings.py updated

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

>> q7_lists.py.updated

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

>> q8_parsing.py updated



