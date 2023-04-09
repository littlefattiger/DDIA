## Designing Typeahead Suggestion
    Similar Services: Auto-suggestions, Typeahead search 

- ####  Functional Requirements: 
  - As the user types in their query, our service should suggest top 10 terms starting with whatever the user has typed.
- ####  Non-function Requirements: 
  - The suggestions should appear in real-time. The user should be able to see the suggestions within 200ms.
- #### Basic System Design and Algorithm
  - Trie in memory
  - assume our data is case insensitive.
  - How to find top suggestion? could be to store the count of searches that **terminated** at each node
  - store top suggestions with each node? We can store top 10 suggestions at each node that we can return to the user
  - How would we build this trie? bottom up; recursively
  - How to update the trie? I think we can use a db idea; snapshot + cdc
    - We can make a copy of the trie on each server to update it offline. Once done we can switch to start using it and discard the old one.
    - Another option is we can have a master-slave configuration for each trie server. We can update slave while the master is serving traffic. Once the update is complete, we can make the slave our new master. We can later update our old master, which can then start serving traffic, too
    - How can we update the frequencies of typeahead suggestions? After inserting a new term in the trie, we’ll go to the terminal node of the phrase and increase its frequency. Since we’re storing the top 10 queries in each node, it is possible that this particular search term jumped into the top 10 queries of a few other nodes. So, we need to update the top 10 queries of those nodes then. We have to traverse back from the node to all the way up to the root. For every parent, we check if the current query is part of the top 10. If so, we update the corresponding frequency. If not, we check if the current query’s frequency is high enough to be a part of the top 10. If so, we insert this new term and remove the term with the lowest frequency.
- Permanent Storage of the Trie
  - Down top calculation
-  Scale Estimation
   -  Storage Estimation
      -  Let’s assume we will have 100 million unique terms for which we want to build an index
      -  If on the average each query consists of 3 words and if the average length of a word is 5 characters, this will give us 15 characters of average query size. Assuming we need 2 bytes to store a character, we will need 30 bytes to store an average query. So total storage we will need:100 million * 30 bytes => 3 GB
      -  We can expect some growth in this data every day, but we should also be removing some terms that are not searched anymore. If we assume we have 2% new queries every day and if we are maintaining our index for the last one year, total storage we should expect: 3GB + (0.02 * 3 GB * 365 days) => 25 GB
-   Data Partition
    - Range Based Partitioning
      - First letter? unbalanced servers
    - Partition based on the maximum capacity of the server. We can keep storing data on a server as long as it has memory available. Whenever a sub-tree cannot fit into a server, we break our partition there to assign that range to this server and move on the next server to repeat this process.Let’s say if our first trie server can store all terms from ‘A’ to ‘AABC’, which mean our next server will store from ‘AABD’ onwards. 
    - Partition based on the hash of the term
      - This will make our term distribution random and hence minimize hotspots.

- Cache
  - We can have separate cache servers in front of the trie servers holding most frequently searched terms and their typeahead suggestions. 
  - We can also build a simple Machine Learning (ML) model that can try to predict the engagement on each suggestion based on simple counting, personalization, or trending data etc., and cache these terms
- Personalization
  - Users will receive some typeahead suggestions based on their historical searches, location, language, etc. We can store the personal history of each user separately on the server and cache them on the client too. The server can add these personalized terms in the final set before sending it to the user. Personalized searches should always come before others.
