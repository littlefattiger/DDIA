# Chapter 11 Transmitting Event Streams
---
We can use database, this is what batch job done. However, instead, it is better for consumers to be notified when new events appear.

Messaging Systems
* something like database? No notification function
* with broker.
* Using logs for message storage -> Apache Kafka, Amazon Kinesis Streams, log basis message queue.
* Thus, in situations where messages may be expensive to process and you want to par‐ allelize processing on a message-by-message basis, and where message ordering is not so important, the JMS/AMQP style of message broker is preferable. On the other hand, in situations with high message throughput, where each message is fast to pro‐ cess and where message ordering is important, the log-based approach works very well.
* At the beginning of “Messaging Systems” on page 441 we discussed three choices of what to do if a consumer cannot keep up with the rate at which producers are send‐ ing messages: dropping messages, buffering, or applying backpressure. In this taxon‐ omy, the log-based approach is a form of buffering with a large but fixed-size buffer
* CDC(change data capture) -> update database -> update search index
* Event Sourcing
