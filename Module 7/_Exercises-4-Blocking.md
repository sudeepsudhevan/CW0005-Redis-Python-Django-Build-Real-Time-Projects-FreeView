# Fundamentals: Redis Lists

## Redis CLI Tutorial: Blocking Operations (BLPOP, BRPOP)


## 1. Basic Setup: Create Two Empty Lists

Let's start with two lists that are currently empty.

```bash
redis-cli DEL queue1 queue2
```

This deletes any existing data so we can start clean.

---

## 2. Use BLPOP to Wait for Data

Run this command in **Terminal A**:

```bash
redis-cli BLPOP queue1 10
```

This tells Redis:  
> Wait up to 10 seconds for the leftmost item in `queue1`.  
If no item is available within 10 seconds, it returns `(nil)`.

---

## 3. Push Data into the List

In **Terminal B**, run:

```bash
redis-cli LPUSH queue1 "task-1"
```

Now go back to **Terminal A** — you should see an immediate response:

```bash
1) "queue1"
2) "task-1"
```

Redis unblocked the command because new data was pushed into the list.

---

## 4. Try BRPOP on a Different List

In **Terminal A**, run:

```bash
redis-cli BRPOP queue2 5
```

This will wait up to 5 seconds for data from the right end of `queue2`.

Now in **Terminal B**, add data:

```bash
redis-cli RPUSH queue2 "job-42"
```

Terminal A should respond:

```bash
1) "queue2"
2) "job-42"
```

---

## 5. Blocking with Multiple Lists

You can also listen to more than one list. In **Terminal A**:

```bash
redis-cli BLPOP queue1 queue2 15
```

Whichever list gets data first will be returned. Try this in **Terminal B**:

```bash
redis-cli LPUSH queue2 "from-second-list"
```

Terminal A will respond with data from `queue2`.

---

## 6. Timeout Expiration

Try a short timeout to see what happens when no data arrives.

```bash
redis-cli BLPOP queue1 3
```

Wait without pushing anything. After 3 seconds, you should see:

```bash
(nil)
```

---

## Summary

- `BLPOP` waits for data from the **left** of one or more lists.
- `BRPOP` does the same from the **right**.
- The command returns immediately when data becomes available, or after the timeout.
- Useful when you want to pause and wait for new data to process.
