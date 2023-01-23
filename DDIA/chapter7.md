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

write skew 
* materializing conflicts should be considered a last resort if no alternative is possible. A serializable isolation level is much preferable in most cases.

* Serializability
  * Literally executing transactions in a serial order (see “Actual Serial Execution” on page 252)
  * Two-phase locking (see “Two-Phase Locking (2PL)” on page 257), which for sev‐ eral decades was the only viable option
  * Optimistic concurrency control techniques such as serializable snapshot isolation (see “Serializable Snapshot Isolation (SSI)” on page 261)
