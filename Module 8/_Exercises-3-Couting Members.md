# Fundamentals: Redis Sets

## Redis CLI Tutorial: Counting Members with SCARD

## Prerequisites
Make sure Redis is installed and running on your system. You can start the Redis CLI by typing:

```bash
redis-cli
```

---

## 1. Create a Set

First, let's create a set with a few members:

```bash
SADD fruits apple banana cherry
```

You should see a response indicating how many new elements were added (in this case, 3).

---

## 2. Count Members in the Set

Now, use `SCARD` to count the number of members in the `fruits` set:

```bash
SCARD fruits
```

You should see:

```
(integer) 3
```

---

## 3. Add More Members

Add more items to the set:

```bash
SADD fruits mango orange
```

Now check the count again:

```bash
SCARD fruits
```

Expected output:

```
(integer) 5
```

---

## 4. Use SCARD on a Non-Existing Key

Try using SCARD on a key that doesn’t exist:

```bash
SCARD vegetables
```

You’ll get:

```
(integer) 0
```

This means the key is either not set or is not a set type.

---

## 5. Attempt on a Non-Set Type (Optional)

Create a string key:

```bash
SET mykey "hello"
```

Now try SCARD on it:

```bash
SCARD mykey
```

You’ll get an error:

```
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```

---

## Summary

- `SCARD` gives the number of members in a set.
- Returns 0 if the key doesn’t exist.
- Errors if used on the wrong data type.

Use `SCARD` when you just need to know how many items are in a Redis set—simple and effective.

