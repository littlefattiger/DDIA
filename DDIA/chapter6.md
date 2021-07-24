# Chapter 6 Partitioning
---
* Partitioning of Key-Value Data
  * Partitioning by Key Range. The partition boundaries might be chosen manually by an administrator, or the data‐ base can choose them automatically-> bigtable. [Bigtable vs Bigquery](https://stackoverflow.com/questions/39919815/whats-the-difference-between-bigquery-and-bigtable) 
  * Partitioning by Hash of Key
* document-partitioned secondary indexes
* Partitioning Secondary Indexes by Term
* Strategies for Rebalancing
  * How not to do it: hash mod N
  * create many more partitions than there are nodes 
  * Dynamic partitioning
  * Operations: Automatic or Manual Rebalancing
* For example, LinkedIn’s Espresso uses Helix [31] for cluster management (which in turn relies on ZooKeeper), implementing a routing tier as shown in Figure 6-8. HBase, SolrCloud, and Kafka also use ZooKeeper to track partition assignment.
