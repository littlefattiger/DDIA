# Chapter 9 Consistency and Consensus
---
One of the most important abstractions for distributed systems is **consensus**: that is, getting all of the nodes to agree on something. 

There is some similarity between distributed consistency models and the hierarchy of transaction isolation levels we discussed previously. But while there is some overlap, they are mostly independent concerns: transaction isolation is primarily about avoiding race conditions due to concurrently executing transactions, whereas distributed consistency is mostly about coordinating the state of replicas in the face of delays and faults.

This chapter covers a broad range of topics, but as we shall see, these areas are in fact deeply linked:
* We will start by looking at one of the strongest consistency models in common use, linearizability, and examine its pros and cons.
* We’ll then examine the issue of ordering events in a distributed system, particularly around causality and total ordering.
  * Lamport timestamps 
* In the third section we will explore how to atomically commit a distributed transaction, which will finally lead us toward solutions for the consensus problem.

linearizability essentially means “behave as though there is only a single copy of the data, and all operations on it are atomic”
