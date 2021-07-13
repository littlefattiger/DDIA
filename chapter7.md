# Chapter 7 Transactions
---
A transaction is a way for an application to group several reads and writes together into a logical unit. Conceptually, all the reads and writes in a transaction are executed as one operation: either the entire transaction succeeds (commit) or it fails (abort, rollback).
* Mainly using transactions to deal with some issues. But transactions is not there for grant.

The Meaning of ACID: **atomicity, consistency, isolation, and durability**. everything between a BEGIN TRANSACTION and a COMMIT statement is considered to be part of the same transaction

* Mainly want to resolve race conditions issue here
* Locks and compare-and-set operations assume that there is a single up-to-date copy of the data. 
* write skew 
* materializing conflicts should be considered a last resort if no alternative is possible. A serializable isolation level is much preferable in most cases.

* Serializability
  * Literally executing transactions in a serial order (see “Actual Serial Execution” on page 252)
  * Two-phase locking (see “Two-Phase Locking (2PL)” on page 257), which for sev‐ eral decades was the only viable option
  * Optimistic concurrency control techniques such as serializable snapshot isolation (see “Serializable Snapshot Isolation (SSI)” on page 261)
