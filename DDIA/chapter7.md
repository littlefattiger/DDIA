# Chapter 7 Transactions
---
A transaction is a way for an application to group several reads and writes together into a logical unit. Conceptually, all the reads and writes in a transaction are executed as one operation: either the entire transaction succeeds (commit) or it fails (abort, rollback).
* Mainly using transactions to deal with some issues. But transactions is not there for grant.

Concept of ACID: **atomicity, consistency, isolation, and durability**. everything between a BEGIN TRANSACTION and a COMMIT statement is considered to be part of the same transaction

Isolation -> Prevent concurrency.

Week Isolation levels
  * Read commit -> no dirty read and no dirty write
  * Snapshot isolation and repeatable read -> have a snapshot and it can do multiple read without any issue
  * prevent lost update -> two updates together, one may loss
    * Atomic write operations -> Need to have this function
    * Explicit locking -> the application can perform a read-modify-write cycle, and if any other transaction tries to concurrently read the same object, it is forced to wait until the first read-modify-write cycle has completed
Automatically detecting lost updates
  * An alternative is to allow them to execute in parallel and, if the transaction manager detects a lost update, abort the transaction and force it to retry its read-modify-write cycle Lost update detection is a great feature, because it doesn’t require application code to use any special database features—you may forget to use a lock or an atomic opera‐ tion and thus introduce a bug, but lost update detection happens automatically and is thus less error-prone ->Automatically detecting lost updates
    * Compare-and-set
    * Conflict resolution and replication -> Allow conflict and concurrent write because of its multiple leader/leaderless
    * On the other hand, the last write wins (LWW) conflict resolution method is prone to lost update. Unfortunately, LWW is the default in many replicated databases.

Write skew 
* What is write skew? This anomaly is called write skew [28]. It is neither a dirty write nor a lost update, because the two transactions are updating two different objects
* This effect, where a write in one transaction changes the result of a search query in another transaction, is called a phantom [3]. Snapshot isolation avoids phantoms in read-only queries, but in read-write transactions like the examples we discussed, phantoms can lead to particularly tricky cases of write skew
* materializing conflicts should be considered a last resort if no alternative is possible. A serializable isolation level is much preferable in most cases. -> The action here is to use a thrid fake table to materia the conflict

Read committed and snapshot isolation levels can solve some problem, but not all. -> Before is week isolation-> use serializable isolation. Serializable isolation is usually regarded as the strongest isolation level -> the database prevents all possible race conditions -> Current chapter, we mainly talk about single node level. They used mainly these 3 ways:
  * Literally executing transactions in a serial order -> a single-threaded loop -> stored procedures: book tickets and only submit once with all transactions
  * For around 30 years, there was only one widely used algorithm for serializability in databases: two-phase locking (2PL) -> not 2PC, which for sev‐ eral decades was the only viable option
    *  If transaction A has read an object and transaction B wants to write to that object, B must wait until A commits or aborts before it can continue. (This ensures that B can’t change the object unexpectedly behind A’s back.)
    *  If transaction A has written an object and transaction B wants to read that object, B must wait until A commits or aborts before it can continue. (Reading an old version of the object, like in Figure 7-1, is not acceptable under 2PL.)
    *  In 2PL, writers don’t just block other writers; they also block readers and vice versa. Snapshot isolation has the mantra readers never block writers, and writers never block readers, which captures this key difference between snapshot isolation and two-phase locking. On the other hand, because 2PL provides serializability, it protects against all the race conditions dis‐ cussed earlier, including lost updates and write skew
    *  Index-range locks use most
  * Serializable Snapshot Isolation (SSI) has the possibility of being fast enough to become the new default in the future. -> optimistic concurrency control; Two-phase locking is a so-called pessimistic concurrency control mechanism
