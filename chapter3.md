# Chapter 3 Storage and Retrieval
---
* Introduce a very simple database using shell command. Insert is O(1), read is O(n)
* Introduce Index here. This is an important trade-off in storage systems: well-chosen indexes speed up read queries, but every index slows down writes. 
* Hash Indexes. Put the index in memory. Merge it later for different segments. -> compaction process.
* Sorted String Table -> key-value pairs is sorted by key. memtable -> disk.
* Log-Structured Merge-Tree -> LSM storage. Bloom filters use here to save some time if you want to confirm that key does not exist.
