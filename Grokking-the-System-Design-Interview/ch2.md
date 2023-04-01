## Designing a URL Shortening service like TinyURL
- Requirements and Goals of the System
   - Functional Requirements
      1. Given a URL, our service should generate a shorter and unique alias of it. This 
      is called a short link.
      2. When users access a short link, our service should redirect them to the 
      original link.
      3. Users should optionally be able to pick a custom short link for their URL.
      4. Links will expire after a standard default timespan. Users should be able to 
      specify the expiration time.
   - Non-Functional Requirements:
      1. The system should be highly available. This is required because, if our service is down, all the URL redirections will start failing.
      2. URL redirection should happen in real-time with minimal latency.
      3. Shortened links should not be guessable (not predictable).
- Capacity Estimation and Constraints
  - **Write** Traffic estimates: Assuming, we will have 500M new URL shortenings per month
  - **Read** with 100:1 read/write ratio, we can expect 50B redirections during the same period 100 * 500M => 50B messages
  - **Write** QPS: New URLs shortenings per second 500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s
  - **Read** Considering 100:1 read/write ratio, 100 * 200 URLs/s = 20K/s
  - Storage estimates
    - Let’s assume we store every URL shortening request for 5 years.
    - 500 million * 5 years * 12 months = 30 billion
    - Let’s assume that each stored object will be approximately 500 bytes
    - We will need 15TB of total storage, 30 billion * 500 bytes = 15 TB.  500 bytes = 0.5 KB
  - Bandwidth estimates: 
    - total incoming data 200 * 500 bytes = 100 KB/s
    - read requests 20K * 500 bytes = ~10 MB/s
    - 20K requests per second, 1.7 billion requests per day. 20K * 3600 seconds * 24 hours = ~1.7 billion
    - To cache 20% of these requests,we will need 170GB of memory: 0.2 * 1.7 billion * 500 bytes = ~170GB
