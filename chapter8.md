# Chapter 8 The Trouble with Distributed Systems
---

Yes, this chapter mainly talk about what may go wrong and how it may go wrong.

If we want to make distributed systems work, we must accept the possibility of partial failure and build fault-tolerance mechanisms into the software. In other words, we need to build a reliable system from unreliable components.

Several ways of fault, including: 
* Whenever you try to send a packet over the network, it may be lost or arbitrarily delayed.
* A node’s clock may be significantly out of sync with other nodes, it may suddenly jump forward or back in time, and relying on it is dangerous because you most likely don’t have a good measure of your clock’s error interval.
* A process may pause for a substantial amount of time at any point in its execution, be declared dead by other nodes, and then come back to life again without realizing that it was paused.

We need to have a distribute system which can tolerate fault:
* To tolerate faults, the first step is to detect them, but even that is hard. 
* Once a fault is detected, making a system tolerate it is not easy either: there is no global variable, no shared memory, no common knowledge or any other kind of shared state between the machines.

In this chapter we also went on some tangents to explore whether the unreliability of networks, clocks, and processes is an inevitable law of nature. 

