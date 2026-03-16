# Fundamentals: Redis Lists

## Redis CLI Tutorial: Managing List Size with LTRIM

## 2. Basic Syntax and Usage

The `LTRIM` command trims a list to only include elements between a given start and stop index.

### Example:

```bash
redis-cli DEL mylist
redis-cli RPUSH mylist "a" "b" "c" "d" "e"
redis-cli LTRIM mylist 1 3
```

**Explanation:**
- This keeps only the items at index 1 through 3 (`"b"`, `"c"`, `"d"`).
- The resulting list will be: `["b", "c", "d"]`.

You can use negative indexes:
```bash
redis-cli LTRIM mylist -3 -1
```
This keeps the last 3 items in the list.

---

## 3. Trimming After Adding Items

A common pattern is to push new items to a list and immediately trim it to a fixed size.

### Example:

```bash
redis-cli DEL logs
redis-cli LPUSH logs "log-1"
redis-cli LTRIM logs 0 4
redis-cli LPUSH logs "log-2"
redis-cli LTRIM logs 0 4
```

**Explanation:**
- This keeps the newest 5 logs in the list.
- `LPUSH` adds to the head; `LTRIM 0 4` ensures only 5 elements are kept.

---

## 4. Using LTRIM for Capped Lists

Simulate a fixed-size list where only the most recent N items are preserved.

### Example:

```bash
redis-cli DEL recent_searches
for i in {1..10}; do redis-cli RPUSH recent_searches "search-$i"; redis-cli LTRIM recent_searches -5 -1; done
```

**Explanation:**
- Each time an item is added, the list is trimmed to keep only the last 5.
- This creates a simple "capped list" behavior.

To see the final result:

```bash
redis-cli LRANGE recent_searches 0 -1
```

Expected output:

```bash
1) "search-6"
2) "search-7"
3) "search-8"
4) "search-9"
5) "search-10"
```

---

## 5. Handling Edge Cases

### Case 1: Indexes out of range

```bash
redis-cli LTRIM mylist 100 200
```

- If the indexes are outside the list's bounds, the list becomes empty.

### Case 2: Start index > Stop index

```bash
redis-cli LTRIM mylist 3 1
```

- This also results in an empty list.

### Case 3: Empty list

```bash
redis-cli DEL mylist
redis-cli LTRIM mylist 0 10
```

- Works without error, but does nothing — the list stays empty.

### Case 4: List does not exist

```bash
redis-cli LTRIM nonexistent 0 5
```

- No error is returned. Redis simply does nothing.

---

## Summary

- `LTRIM` helps you control the size of a list using index-based slicing.
- Works well with `LPUSH` or `RPUSH` to maintain capped or sliding windows.
- It's safe to run even when the list is empty or doesn't exist.
