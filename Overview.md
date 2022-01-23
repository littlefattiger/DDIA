1. Hadoop
    - Distributed file storing system
    - Learned 3.13
3. Zookeeper
    - This is distributed linux like file system
    - It used CP out of CAP
    - It will help Kafka and Hive
    - Using ZAP protocal/I think it is similar to paxos and raft
5. Hive
    - HDFS based SQL data warehouse 
    - Compector is presto. Presto use within athena in S3.
    - Hive is more like a MR optimizer. You write SQL code and you will get a result from HDFS, no need to write JAVA code to do so. SQL is easy.
6. Flume
    - Log collector: Linux system -> HDFS
    - Different destination: Flume -> Kafka
8. Hbase
    - HDFS based NoSQL database
    - compact and split
9. Scala
    - Very similar to Java
    - functional language
    - OOP
11. Spark
12. Atlas
    - metadata manage
    - Variable dictionary
    - Table lineage/dependency
12. Kylin
    - no idea now
14. Prometheus+Grafana+ruixiang cloud. It is similar to Datadog + slack
    - this set is just for alerting. We can integrate the alert system with slack and pageduty
### Message Queue
1. Kafka
    - producer, consumer
3. Flink
4. Spark Stream


### Scheduler and coordinator
[Ref](https://www.jdon.com/workflow/Airflow-vs-Azkaban-vs-Conductor-vs-Oozie-vs-Amazon-Step-Functions.html)
This part is easy. The most based scheduler is crontab from linux but it can not solve the dependency problem. Then we have the follow one. We can think them as a alternative for cron.
1. Azkaban3.x
    - Using Yaml file 
2. Oozie
    - Using XML file
3. Airflow
    - Using Python flask 
