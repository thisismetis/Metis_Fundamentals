# Demo Pair Problem

The problem is to determine a schedule of pairings for a list of students so that everyone has a pair every day, and everyone eventually pairs with everyone else.

Write a function that takes a list of names and returns a list of lists of tuples representing pairs. (Assume an even number of names, all distinct.) For example:

```
>>> pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug'])
# [[('Bob', 'Cassandra'), ('Andrea', 'Doug')],
#  [('Andrea', 'Bob'), ('Cassandra', 'Doug')],
#  [('Andrea', 'Cassandra'), ('Bob', 'Doug')]]
```

See [here](./solution/pair_demo_solution.ipynb) for a solution.
