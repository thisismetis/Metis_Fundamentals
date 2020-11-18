# Pair Programming

[Pairing](http://guide.agilealliance.org/guide/pairing.html), ideally, is good for both participants and for the work they produce.

We would like to have everyone do some morning pairing with everyone else.


#### Demo Problem

The first problem is to determine a schedule of pairings so that everyone has a pair every day, and everyone eventually pairs with everyone else.

Write a function that takes a list of names and returns a list of lists of tuples representing pairs. (Assume an even number of names, all distinct.) For example:

```
>>> pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug'])
# [[('Bob', 'Cassandra'), ('Andrea', 'Doug')],
#  [('Andrea', 'Bob'), ('Cassandra', 'Doug')],
#  [('Andrea', 'Cassandra'), ('Bob', 'Doug')]]
```
