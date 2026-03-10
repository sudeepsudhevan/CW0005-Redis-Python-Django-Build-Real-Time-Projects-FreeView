# Fundamentals: Redis Hashes

## Redis Workbench Tutorial: Updating Hashes with `HSET`

---

## 1. How `HSET` Handles Existing Fields

**Explanation:**  
When you use `HSET` on a field that already exists in a hash, Redis will silently overwrite the existing value with the new one. There is no warning or error.

```bash
HSET user:1001 name "Alice"
HGET user:1001 name
# Output: "Alice"

HSET user:1001 name "Alicia"
HGET user:1001 name
# Output: "Alicia"
```

---

## 2. Updating a Single Field

**Explanation:**  
You can update just one field by calling `HSET` with the hash key, field, and new value.

```bash
HSET product:2001 price "19.99"
HGET product:2001 price
# Output: "19.99"

HSET product:2001 price "17.49"
HGET product:2001 price
# Output: "17.49"
```

---

## 3. Updating Multiple Fields

**Explanation:**  
You can also update multiple fields in one command by passing multiple field-value pairs.

```bash
HSET session:3001 status "active" last_seen "2025-04-30T10:00:00Z"
HGETALL session:3001
# Output:
# 1) "status"
# 2) "active"
# 3) "last_seen"
# 4) "2025-04-30T10:00:00Z"

HSET session:3001 status "inactive" last_seen "2025-04-30T12:00:00Z"
HGETALL session:3001
# Output:
# 1) "status"
# 2) "inactive"
# 3) "last_seen"
# 4) "2025-04-30T12:00:00Z"
```

---

## 4. Verifying Updates

**Explanation:**  
Use `HGET` to check a single field or `HGETALL` to inspect the entire hash.

```bash
HGET session:3001 status
# Output: "inactive"

HGETALL session:3001
# Output:
# 1) "status"
# 2) "inactive"
# 3) "last_seen"
# 4) "2025-04-30T12:00:00Z"
```

---

## 5. Avoiding Mistakes

**Explanation:**  
Watch for typos or wrong field names—Redis won’t stop you from adding unexpected fields. Also, be careful not to overwrite values unintentionally.

```bash
HSET user:1001 emaill "alice@example.com"   # Typo: "emaill"
HGETALL user:1001
# Output might include both "email" and "emaill" if the typo was new

# Best practice: Double-check field names
HGET user:1001 email
# Output: (nil) if the correct field was never set
```

Always verify with `HGETALL` to catch any accidental additions or overwrites.
