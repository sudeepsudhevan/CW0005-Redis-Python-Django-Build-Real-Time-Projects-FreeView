# Fundamentals: Redis Lists

## Redis Workbench Tutorial: Redis Lists

---

## 🔹 Tutorial 1: Create a new list called "fruits" by pushing items to the left

```redis
# Create a new list called "fruits" by pushing items to the left
LPUSH fruits "apple" "banana" "cherry"

# Check the contents of the list
LRANGE fruits 0 -1
```
