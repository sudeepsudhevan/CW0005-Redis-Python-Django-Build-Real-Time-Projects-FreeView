# Fundamentals: Redis Hashes

##  Redis Hash Reading Commands – Workbench Tutorial

## 🔹 1. Reading a Single Field with `HGET`

```redis
HSET user:1001 name "Alice" email "alice@example.com" age "28"
HGET user:1001 name
```

**Expected Output:**
```
"Alice"
```

---

## 🔹 2. Reading Multiple Fields with `HMGET`

```redis
HMGET user:1001 name email
```

**Expected Output:**
```
1) "Alice"
2) "alice@example.com"
```

---

## 🔹 3. Retrieving All Fields with `HGETALL`

```redis
HGETALL user:1001
```

**Expected Output:**
```
1) "name"
2) "Alice"
3) "email"
4) "alice@example.com"
5) "age"
6) "28"
```

> Output is a flat list: alternating field names and values.

---

## 🔹 4. Checking Field Existence with `HEXISTS`

```redis
HEXISTS user:1001 email
HEXISTS user:1001 phone
```

**Expected Output:**
```
(integer) 1   // Field "email" exists
(integer) 0   // Field "phone" does not exist
```

---

## 🔹 5. Hash Size with `HLEN`

```redis
HLEN user:1001
```

**Expected Output:**
```
(integer) 3
```

> This shows that there are 3 fields in the hash `user:1001`.
