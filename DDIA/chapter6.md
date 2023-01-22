# Chapter 6 Partitioning
---
* Partitioning of Key-Value Data
  * Partitioning by Key Range. The partition boundaries might be chosen manually by an administrator, or the data‐ base can choose them automatically-> bigtable. [Bigtable vs Bigquery](https://stackoverflow.com/questions/39919815/whats-the-difference-between-bigquery-and-bigtable) 
  * Partitioning by Hash of Key
* Secondary index
  * Document-partitioned secondary indexes -> each partition has its own local index. 2 partion has its own index. When you write, you only will impact this partition and its index, becaue the index is local. When you read, you need to check index from both side -> search color=read, in 2 partitions. Easy write and complicated read, you need to search all partitions to read to check the index.
  * Partitioning Secondary Indexes by Term. Use a global index for term, and the 2nd index is also partition. Obvioud easy read, because it is global index, you will only go to the partitions it contain this like color:red=[223,345,466]. But hard to write, for example, a car with read and model = audi, color:red and model:audi may not be in the same index partition.
* Strategies for Rebalancing
  * How not to do it: hash mod N
  * create many more partitions than there are nodes 
  * Dynamic partitioning
  * Operations: Automatic or Manual Rebalancing
* For example, LinkedIn’s Espresso uses Helix [31] for cluster management (which in turn relies on ZooKeeper), implementing a routing tier as shown in Figure 6-8. HBase, SolrCloud, and Kafka also use ZooKeeper to track partition assignment.
* Request Routing
  * Allow clients to contact any node
  * Send all requests from clients to a routing tier first, which determines the node that should handle each request and forwards it accordingly
  * Require that clients be aware of the partitioning and the assignment of partitions to nodes
  * 2nd is just like using zookeeper
