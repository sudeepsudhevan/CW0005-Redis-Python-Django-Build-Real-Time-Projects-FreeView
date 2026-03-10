# Fundamentals: Redis Hashes

## Redis Workbench Tutorial: Deleting Hash Fields and Keys

---

## 1. Introduction to `HDEL`

**Explanation:**  
`HDEL` is used to delete specific fields from a hash. Use it when you want to remove parts of the data but keep the hash key and other fields intact.

```bash
HSET user:1002 name "Sam" email "sam@example.com" status "active"
HGETALL user:1002
# Output:
# 1) "name"
# 2) "Sam"
# 3) "email"
# 4) "sam@example.com"
# 5) "status"
# 6) "active"
```

---

## 2. Removing Single or Multiple Fields

**Explanation:**  
You can delete one or more fields using `HDEL`. If the field doesn’t exist, Redis skips it silently.

**Example – Deleting One Field:**

```bash
HDEL user:1002 email
HGETALL user:1002
# Output will no longer include "email"
```

**Example – Deleting Multiple Fields:**

```bash
HDEL user:1002 name status
HGETALL user:1002
# Output: empty (if those were the last fields)
```

---

## 3. Verifying Field Deletion

**Explanation:**  
Use `HGET` to check a single field or `HGETALL` to view the entire hash and confirm what’s been removed.

```bash
HGET user:1002 email
# Output: (nil)

HGETALL user:1002
# Output: empty or remaining fields only
```

---

## 4. Deleting Entire Hash Keys with `DEL`

**Explanation:**  
Use `DEL` when you want to delete the entire key and all its associated fields.

```bash
HSET session:5001 token "abc123" status "valid"
DEL session:5001
HGETALL session:5001
# Output: (nil)
```

---

## 5. Differences Between `HDEL` and `DEL`

**Explanation:**  
`HDEL` targets individual fields. `DEL` removes the entire hash.

```bash
# Using HDEL
HDEL user:1002 status
# Hash key remains if other fields still exist

# Using DEL
DEL user:1002
# Entire hash key is gone
```

---

## 6. Avoiding Common Deletion Errors

**Explanation:**  
Be cautious of typos, missing fields, or confusing partial vs. full deletion.

**Example – Typo in Field:**

```bash
HDEL user:1002 statuss   # Incorrect field name
HGETALL user:1002        # "status" field still exists
```

**Example – Misunderstanding `HDEL`:**

```bash
HDEL user:1002 name
# Deletes only the 'name' field — not the whole hash
```

**Example – Check for Full Deletion:**

```bash
HGETALL user:1002
# If nothing returns, the hash might still exist as an empty structure
```

Redis won’t raise errors, so always verify your changes.
