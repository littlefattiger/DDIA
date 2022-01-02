1. Hadoop
    - Distributed file storing system
3. Zookeeper
    - This is distributed linux like file system
    - It used CP out of CAP
    - It will help Kafka and Hive
    - Using ZAP protocal/I think it is similar to paxos and raft
5. Hive
    - HDFS based SQL data warehouse 
6. Flume
    - Log collector: Linux system -> HDFS
    - Different destination: Flume -> Kafka
8. Hbase
    - HDFS based NoSQL database

### Message Queue
1. Kafka
    - producer, consumer
3. Flink
4. Spark Stream


### Scheduler
[Ref](https://www.jdon.com/workflow/Airflow-vs-Azkaban-vs-Conductor-vs-Oozie-vs-Amazon-Step-Functions.html)
1. Azkaban3.x
    - Using Yaml file 
2. Oozie
    - Using XML file
3. Airflow
    - Using Python flask 
