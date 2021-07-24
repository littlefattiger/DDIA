# Chapter 9 Consistency and Consensus
---
One of the most important abstractions for distributed systems is **consensus**: that is, getting all of the nodes to agree on something. 

There is some similarity between distributed consistency models and the hierarchy of transaction isolation levels we discussed previously. But while there is some overlap, they are mostly independent concerns: transaction isolation is primarily about avoiding race conditions due to concurrently executing transactions, whereas distributed consistency is mostly about coordinating the state of replicas in the face of delays and faults.

This chapter covers a broad range of topics, but as we shall see, these areas are in fact deeply linked:
* We will start by looking at one of the strongest consistency models in common use, linearizability, and examine its pros and cons.
* We’ll then examine the issue of ordering events in a distributed system, particularly around causality and total ordering.
  * Lamport timestamps 
  * This is no coincidence: it can be proved that a linearizable compare-and-set egister and total order broadcast are both equivalent to consensus
* In the third section we will explore how to atomically commit a distributed transaction, which will finally lead us toward solutions for the consensus problem.
 * two-phase commit -> use coordinator

linearizability essentially means “behave as though there is only a single copy of the data, and all operations on it are atomic”

Consensus algorithms and total order broadcast

ZooKeeper and etcd are designed to hold small amounts of data that can fit entirely in memory
