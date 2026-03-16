# Fundamentals: Redis Lists

## Adding to Redis Lists: LPUSH and RPUSH

---

In this tutorial, we’ll explore how to add items to Redis lists using the `LPUSH` and `RPUSH` commands in Redis CLI or Workbench.

---

## 🟢 1. Add Items with LPUSH (Left Push)

```redis
# Add items to the front (left) of the list
LPUSH tasks "task1"
LPUSH tasks "task2" "task3"
```

**Expected order in list:**
```
["task3", "task2", "task1"]
```

**Check the contents:**
```redis
LRANGE tasks 0 -1
```

---

## 🔵 2. Add Items with RPUSH (Right Push)

```redis
# Add items to the end (right) of the list
RPUSH events "login"
RPUSH events "click" "logout"
```

**Expected order in list:**
```
["login", "click", "logout"]
```

**Check the contents:**
```redis
LRANGE events 0 -1
```

---

## 🔍 3. Auto-Creation of Lists

If the list doesn't exist, Redis will create it automatically when you use `LPUSH` or `RPUSH`.

```redis
RPUSH fruits "apple" "banana"
```

Check:
```redis
LRANGE fruits 0 -1
```

---

## 🧪 4. Inserting Multiple Values

Both `LPUSH` and `RPUSH` accept multiple values. The order matters:

```redis
LPUSH notes "note1" "note2" "note3"
# List becomes: ["note3", "note2", "note1"]
```

---

## 📌 Summary

- `LPUSH` adds to the **start** of the list (left side).
- `RPUSH` adds to the **end** of the list (right side).
- Redis creates lists automatically.
- Use `LRANGE key 0 -1` to view the full list.
