# Series: A Single Bookshelf (A Single Column)

Think of a **Series** as a single, labeled bookshelf.
* **It's One-Dimensional:** Just a single row of books.
* **It has Labels:** Each book (data point) has a label (the index) so you can find it easily, like "Shelf Position 1", "Shelf Position 2", etc.
* **It holds one type of thing:** All the items on this shelf are the same type (e.g., all cookbooks, all novels, or all integers, all strings).

  Example as a Python list:

      # A list of fruits
      fruits_list = ['Apple', 'Banana', 'Cherry']

  Example as a Pandas Series:

      import pandas as pd

      # Creating a Series
      fruits = pd.Series(['Apple', 'Banana', 'Cherry'])
      print(fruits)


  We can even use custom labels:

      fruits = pd.Series(['Apple', 'Banana', 'Cherry'], index=['a', 'b', 'c'])
      print(fruits)
