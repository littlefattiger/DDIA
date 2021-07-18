# Chapter 10: Batch Processing
---
1. Talk about Unix data process
2. Map-reduce process, similar as Unix

I found this chapter mainly talk about the map reduce process, HDFS, hadop system. Also discuss in detail some of the feature they have.

The rest of this chapter is talking about other alternatives to Hadoop. Like spark, it can mitigate the materialization of intermediate state issue.

Spark, Flink, and Tez avoid writing intermediate state to HDFS, so they take a differ‐ ent approach to tolerating faults: if a machine fails and the intermediate state on that machine is lost, it is recomputed from other data that is still available 
