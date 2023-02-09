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
* Think about the immutuable log and final state.
* This idea is sometimes known as command query responsibility segregation (CQRS)
* The traditional approach to database and schema design is based on the fallacy that data must be written in the same form as it will be queried.
* What remains is to discuss what you can do with the stream once you have it— namely, you can process it. Broadly, there are three options:
  1. You can take the data in the events and write it to a database, cache, search index, or similar storage system, from where it can then be queried by other clients.
  2. You can push the events to users in some way, for example by sending email alerts or push notifications, or by streaming the events to a real-time dashboard where they are visualized. 
  3. You can process one or more input streams to produce one or more output streams. Streams may go through a pipeline consisting of several such processing stages before they eventually end up at an output (option 1 or 2).   
Stream Joins
* Stream-stream join (window join)
* Stream-table join (stream enrichment)
* Table-table join (materialized view maintenance)
Fault Tolerance
* Microbatching and checkpointing
* Atomic commit revisited
* Idempotence
* Rebuilding state after a failure
