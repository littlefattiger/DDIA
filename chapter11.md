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
* [Event Sourcing](https://zhuanlan.zhihu.com/p/38968012)
* Think about the immutuable log and final state.
* This idea is sometimes known as command query responsibility segregation (CQRS)
* The traditional approach to database and schema design is based on the fallacy that data must be written in the same form as it will be queried.
* What remains is to discuss what you can do with the stream once you have it— namely, you can process it. Broadly, there are three options:
  1. You can take the data in the events and write it to a database, cache, search index, or similar storage system, from where it can then be queried by other clients.
  2. You can push the events to users in some way, for example by sending email alerts or push notifications, or by streaming the events to a real-time dashboard where they are visualized. 
  3. You can process one or more input streams to produce one or more output streams. Streams may go through a pipeline consisting of several such processing stages before they eventually end up at an output (option 1 or 2).   
