# Chapter 7 Transactions
---
A transaction is a way for an application to group several reads and writes together into a logical unit. Conceptually, all the reads and writes in a transaction are executed as one operation: either the entire transaction succeeds (commit) or it fails (abort, rollback).
* Mainly using transactions to deal with some issues. But transactions is not there for grant.

The Meaning of ACID: **atomicity, consistency, isolation, and durability**. everything between a BEGIN TRANSACTION and a COMMIT statement is considered to be part of the same transaction

* Locks and compare-and-set operations assume that there is a single up-to-date copy of the data. 
* write skew 
* materializing conflicts should be considered a last resort if no alternative is possible. A serializable isolation level is much preferable in most cases.

