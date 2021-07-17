# Chapter 8 The Trouble with Distributed Systems
---

Yes, this chapter mainly talk about what may go wrong and how it may go wrong.

If we want to make distributed systems work, we must accept the possibility of partial failure and build fault-tolerance mechanisms into the software. In other words, we need to build a reliable system from unreliable components.

Several ways of fault, including: 
* Whenever you try to send a packet over the network, it may be lost or arbitrarily delayed.
* A node’s clock may be significantly out of sync with other nodes, it may suddenly jump forward or back in time, and relying on it is dangerous because you most likely don’t have a good measure of your clock’s error interval.
* A process may pause for a substantial amount of time at any point in its execution, be declared dead by other nodes, and then come back to life again without realizing that it was paused.


