# Fundamentals: Redis Lists

## Redis List Commands Tutorial (Workbench CLI)

## 1. Using `LRANGE` to Read List Contents

`LRANGE` retrieves elements from a Redis list between two specified indexes.

### Syntax:
```
LRANGE key start stop
```

### Example:
```bash
LPUSH mylist "item1" "item2" "item3"
LRANGE mylist 0 -1
```

### Output:
```
1) "item3"
2) "item2"
3) "item1"
```

- `0` is the starting index (leftmost).
- `-1` means "up to the end of the list".

To get only the first two elements:
```bash
LRANGE mylist 0 1
```

---

## 2. Removing Items with `LPOP`

`LPOP` removes and returns the first (leftmost) item of the list.

### Example:
```bash
LPOP mylist
```

### Output:
```
"item3"
```

Now check the list again:
```bash
LRANGE mylist 0 -1
```

### Result:
```
1) "item2"
2) "item1"
```

---

## 3. Removing Items with `RPOP`

`RPOP` removes and returns the last (rightmost) item of the list.

### Example:
```bash
RPOP mylist
```

### Output:
```
"item1"
```

Check the list again:
```bash
LRANGE mylist 0 -1
```

### Result:
```
1) "item2"
```

---

## 4. Command Output and List Indexing

### Important Notes:

- Redis list indexes start at **0**.
- CLI output numbers (`1)`, `2)`, etc.) are **not the actual indexes** — they just number the lines for display.
- Use `LRANGE` with `0` as the starting point to see this in action.

```bash
LRANGE mylist 0 -1
```

Even if CLI shows:
```
1) "itemA"
2) "itemB"
```
These items are at index `0` and `1`, respectively.

---

## 5. Combining Commands in Workflow

You can chain `LRANGE`, `LPOP`, and `RPOP` to simulate simple queue or stack operations.

### Example Workflow:

```bash
LPUSH queue "job1" "job2" "job3"
LRANGE queue 0 -1      # View all jobs
LPOP queue             # Remove the first job
LRANGE queue 0 -1      # View updated list
RPOP queue             # Remove the last job
LRANGE queue 0 -1      # Final state
```

This sequence shows how the list updates as items are removed from both ends.

---