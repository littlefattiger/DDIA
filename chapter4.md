# Chapter 4 Encoding and Evolution
---
In this chapter we will look at several formats for encoding data, including JSON, XML, Protocol Buffers, Thrift, and Avro. In particular, we will look at how they handle schema changes and how they support systems where old and new data and code need to coexist. We will then discuss how those formats are used for data storage and for communication: in web services, Representational State Transfer (REST), and remote procedure calls (RPC), as well as message-passing systems such as actors and message queues.

* Data In memory
* When you want to write data to a file or send it over the network, you have to encode it as some kind of self-contained sequence of bytes
* The transation from the in-memory representation to a byte sequence is called encoding (also known as serialization or marshalling), and the reverse is called decoding (parsing, deserialization, unmarshalling) 
* JSON, XML, and Binary Variants
* Thrift and Protocol Buffer
* **When I work, I need avro, parquet and redshift in aws" 
