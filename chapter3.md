# Chapter 3 Storage and Retrieval
---
* Introduce a very simple database using shell command. Insert is O(1), read is O(n)
* Introduce Index here. This is an important trade-off in storage systems: well-chosen indexes speed up read queries, but every index slows down writes. 
* Hash Indexes. Put the index in memory. Merge it later for different segments. -> compaction process.
* Sorted String Table -> key-value pairs is sorted by key. memtable -> disk.
* Log-Structured Merge-Tree -> LSM storage. Bloom filters use here to save some time if you want to confirm that key does not exist.
* B-Tree used for most database. In order to make the database resilient to crashes, it is common for B-tree implemen‐ tations to include an additional data structure on disk: a write-ahead log (WAL, also known as a redo log).
* Mainly spend several pages to discuss above two index structure.
* [LSM](https://www.zhihu.com/question/19887265/answer/78839142) explaination from zhihu
* On a high level, we saw that storage engines fall into two broad categories: those opti‐ mized for transaction processing (OLTP), and those optimized for analytics (OLAP).
* OLTP Disk seek time is often the bottleneck here.usually only touch a small number of records in each query(Applied the index mentioned above)
* OLAP Disk bandwidth (not seek time) is often the bottleneck here, and column- oriented storage is an increasingly popular solution for this kind of workload. requiring many millions of records to be scanned in a short time
* OLTP 
  * The log-structured school, which only permits appending to files and deleting obsolete files, but never updates a file that has been written.
  * The update-in-place school, which treats the disk as a set of fixed-size pages that can be overwritten. B-trees are the biggest example of this philosophy

