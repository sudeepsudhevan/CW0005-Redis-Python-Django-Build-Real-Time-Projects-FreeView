# Fundamentals: Redis Sets

## Redis Set Operations Tutorial

## 1. Creating Sets in Redis

The `SADD` command is used to create a set and add one or more members to it.

**Example:**

```bash
SADD fruits apple banana cherry
```

**Expected Output:**

```
(integer) 3
```

This adds three elements to the set `fruits`.

---

## 2. Using SUNION

The `SUNION` command returns the union of all the specified sets. It combines all unique elements from each set.

**Example:**

```bash
SADD set1 apple banana
SADD set2 banana cherry
SUNION set1 set2
```

**Expected Output:**

```
1) "apple"
2) "banana"
3) "cherry"
```

---

## 3. Using SINTER

The `SINTER` command returns only the elements that are common to all specified sets.

**Example:**

```bash
SADD set1 apple banana
SADD set2 banana cherry
SINTER set1 set2
```

**Expected Output:**

```
1) "banana"
```

---

## 4. Using SDIFF

The `SDIFF` command returns the members of the first set that are not in the other sets.

**Example:**

```bash
SADD set1 apple banana
SADD set2 banana cherry
SDIFF set1 set2
```

**Expected Output:**

```
1) "apple"
```

---

## 5. Interpreting Empty and Non-Existing Sets

If a set is empty or doesn’t exist, Redis will still process the command and return appropriate results.

**Example:**

```bash
SUNION set1 nonexist
SINTER set1 emptyset
SDIFF set1 missingkey
```

**Expected Behavior:**

- `SUNION` includes all elements from `set1`.
- `SINTER` returns an empty result if any set is empty or missing.
- `SDIFF` still shows elements in `set1` since `missingkey` has no members.

---

These commands help you work with sets efficiently in Redis and understand how data overlaps or differs across multiple sets.
