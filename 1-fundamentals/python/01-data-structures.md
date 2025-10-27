# 1. Lists - Mutable, Ordered

       # Creation
        my_list = [1, 2, 3, 'hello']
        my_list = list(range(5))
        
        # Common operations
        my_list.append(4)           # Add to end
        my_list.insert(1, 'new')    # Insert at index
        my_list.remove(2)           # Remove first occurrence
        popped = my_list.pop()      # Remove and return last item
        my_list.sort()              # Sort in-place
        sorted_list = sorted(my_list)  # Return new sorted list
        
# 2. Tuples - Immutable, Ordered
      # Creation
      my_tuple = (1, 2, 3, 'hello')
      my_tuple = 1, 2, 3          # Parentheses optional
      single_tuple = (42,)        # Comma required for single element

      # Usage - cannot modify after creation
      coordinates = (10, 20)
      x, y = coordinates          # Unpacking
      
# 3. Dictionaries - Mutable, Key-Value Pairs

       # Creation
        my_dict = {'name': 'Alice', 'age': 30}
        my_dict = dict(name='Bob', age=25)
        
        # Common operations
        my_dict['city'] = 'Boston'          # Add/update
        value = my_dict.get('name')         # Safe access
        value = my_dict.get('missing', 0)   # Default value
        keys = my_dict.keys()               # View of keys
        values = my_dict.values()           # View of values
      
        # Dictionary comprehension
        squares = {x: x*x for x in range(5)}
   
# 4. Sets - Mutable, Unordered, Unique Elements
        # Creation
        my_set = {1, 2, 3, 4}
        my_set = set([1, 2, 2, 3])




**COMPREHENSION PATTERNS CHEAT SHEET**

       # List: [expression for item in iterable]
       # List with condition: [expression for item in iterable if condition]
       # List with if-else: [value_if_true if condition else value_if_false for item in iterable]
       
       # Dict: {key: value for item in iterable}
       # Dict with condition: {key: value for item in iterable if condition}
       
       # Nested: [expression for outer in outer_loop for inner in inner_loop]
