# Demo Pair Problem

The problem is to determine a schedule of pairings for a list of students so that everyone has a pair every day, and everyone eventually pairs with everyone else.

Write a function that takes a list of names and returns a list of lists of tuples representing pairs. (Assume an even number of names, all distinct.) For example:

```
>>> pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug','Casey','Drew'])
# [[('Andrea', 'Casey'), ('Doug', 'Drew'), ('Bob', 'Cassandra')],
# [('Andrea', 'Drew'), ('Casey', 'Cassandra'), ('Doug', 'Bob')],
# [('Andrea', 'Cassandra'), ('Drew', 'Bob'), ('Casey', 'Doug')],
# [('Andrea', 'Bob'), ('Cassandra', 'Doug'), ('Drew', 'Casey')],
# [('Andrea', 'Doug'), ('Bob', 'Casey'), ('Cassandra', 'Drew')]]
```

See [here](./solution/pair_demo_solution.ipynb) for a solution.
