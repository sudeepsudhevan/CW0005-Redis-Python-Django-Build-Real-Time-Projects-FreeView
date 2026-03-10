# Fundamentals: Hash Operations: Performance & Safety

## Redis Workbench Tutorial: Using Pipelines for Efficient Hash Operations

This guide provides step-by-step Redis CLI (Workbench/RedisInsight) commands to perform efficient hash operations using pipelining via MULTI/EXEC.

---

## 🔹 Tutorial 1: Queue Multiple Hash Writes Using MULTI / EXEC

**Goal:** Queue several `HSET` operations to one hash and send them together.

```redis
MULTI
HSET user:1001 name "Alice"
HSET user:1001 email "alice@example.com"
HSET user:1001 status "active"
EXEC
```

📌 *What Happens:*  
All commands are queued until `EXEC` is called. Then Redis executes them in order and returns their results as a list.

---

## 🔹 Tutorial 2: Set Fields for Multiple Hashes at Once

**Goal:** Efficiently write to multiple user hashes in one batch.

```redis
MULTI
HSET user:1002 name "Bob" email "bob@example.com"
HSET user:1003 name "Charlie" email "charlie@example.com"
HSET user:1004 name "Dana" email "dana@example.com"
EXEC
```

📌 *What Happens:*  
Each `HSET` targets a different hash key. Redis queues them, then runs them together after `EXEC`.

---

## 🔹 Tutorial 3: Read from Multiple Hashes Efficiently

**Goal:** Read multiple fields in one operation block.

```redis
MULTI
HGET user:1002 name
HGET user:1003 name
HGET user:1004 name
EXEC
```

📌 *What Happens:*  
Redis returns a list of results for each `HGET`, in order.

---

## 🔹 Tutorial 4: Mix Reads and Writes in One Batch

**Goal:** Update and read from hashes within one pipeline.

```redis
MULTI
HSET user:1002 status "inactive"
HGET user:1002 email
HGET user:1002 status
EXEC
```

📌 *What Happens:*  
The `HSET` is applied first, then `HGET` commands return the updated values, all processed in a single round trip.

---

## 🔹 Tutorial 5: Handle Deletes Efficiently

**Goal:** Delete multiple fields from one or more hashes at once.

```redis
MULTI
HDEL user:1003 email
HDEL user:1004 name
HGETALL user:1003
HGETALL user:1004
EXEC
```

📌 *What Happens:*  
Field deletions and retrievals are queued, then executed together — keeping things clean and efficient.
