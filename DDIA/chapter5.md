# Chapter 5 Replication
---
This chapter mainly talk about different type of replications.
* Purpose:
  * High availability
  * Disconnected operation
  * Latency
  * Scalability
* problems with replication log
  * Reading Your Own Writes -> if you edit profile, you need to read from leader; Compare the write time and the replica latest time; Give more condition there to read leader
  * Monotonic Reads -> easy, you need to read from a replica according to your profile or something, not random
  * Consistent Prefix Reads -> consistent prefix reads -> Write to same partition for causally related to each other.
  * Solutions for Replication Lag -> Transactions for distributed db
* Leaders and Followers
* Single-leader replication
* Multi-Leader Replication
* leaderless model
* The general idea is about reduce latency, data outdated.
* eventually consistent?
* Whether one operation happens before another operation is the key to defining what concurrency means. 
* multiple writes -> like github version control to control concurrency
