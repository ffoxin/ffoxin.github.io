---
layout: post
author: ffoxin
tags: python
---
Few days ago I was asked if it's possible to create variables with desired names
on the fly, like following:

```python
list_vars = ['a', 'b']

some_method(list_vars)

print(a, b)
```

I was absolutely sure that python offers this feature. Quick googling and thats
it: built-in `vars()` method that stores all variables for the current scope.

```python
list_vars = {
    'a': 1,
    'b': 'string',
}

vars().update(list_vars)

print(a, b)
```
Output:
```bash
1
string
```
