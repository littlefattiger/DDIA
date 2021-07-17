# Chapter 9 Consistency and Consensus
---
One of the most important abstractions for distributed systems is **consensus**: that is, getting all of the nodes to agree on something. 

There is some similarity between distributed consistency models and the hierarchy of transaction isolation levels we discussed previously. But while there is some overlap, they are mostly independent concerns: transaction isolation is primarily about avoiding race conditions due to concurrently executing transactions, whereas distributed consistency is mostly about coordinating the state of replicas in the face of delays and faults.
