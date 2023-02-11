# Chapter 11 Transmitting Event Streams
---
We can use database, this is what batch job done. However, instead, it is better for consumers to be notified when new events appear.

Messaging Systems
* Direct messaging from producers to consumers
* Message brokers
  * Message brokers compared to databases
  * Multiple consumers
  * Acknowledgments and redelivery

Partitioned Logs
* Using logs for message storage
* Logs compared to traditional messaging
* Consumer offsets
* Disk space usage
* When consumers cannot keep up with producers
* Replaying old messages

Databases and Streams
* CDC(change data capture) -> update database -> update search index
* [Event Sourcing](https://zhuanlan.zhihu.com/p/38968012)
* discussion about state, steam and Immutability


Processing Streams
* Uses of Stream Processing
  * Complex event processing
  * Stream analytics
  * Maintaining materialized views
  * Search on streams
* Reasoning About Time
  * Event time versus processing time
  * Types of windows
    * Tumbling window
    * Hopping window
    * Sliding window
    * Session window

* Stream Joins
  * Stream-stream join (window join)
  * Stream-table join (stream enrichment)
  * Table-table join (materialized view maintenance)
*Fault Tolerance
  * Microbatching and checkpointing
  * Atomic commit revisited
  * Idempotence
  * Rebuilding state after a failure
