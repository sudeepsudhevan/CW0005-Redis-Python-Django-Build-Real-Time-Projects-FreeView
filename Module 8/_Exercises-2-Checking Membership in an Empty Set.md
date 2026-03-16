# Fundamentals: Redis Sets

## Redis CLI Examples: SISMEMBER

This file demonstrates how to use the `SISMEMBER` command in the Redis CLI to check if a value exists in a set.

---

## Example 1: Basic Membership Check

```bash
# Add values to the set
redis-cli SADD colors "red" "blue" "green"

# Check if "red" is in the set
redis-cli SISMEMBER colors "red"
# Expected output: (integer) 1

# Check if "yellow" is in the set
redis-cli SISMEMBER colors "yellow"
# Expected output: (integer) 0
```

---

## Example 2: Checking Membership in an Empty Set

```bash
# Create a new empty set (nothing added yet)
redis-cli DEL emptyset

# Check membership
redis-cli SISMEMBER emptyset "value"
# Expected output: (integer) 0
```

---

## Example 3: Working with Numeric Values

```bash
# Add numbers as strings to the set
redis-cli SADD numbers "1" "2" "3"

# Check for a number that exists
redis-cli SISMEMBER numbers "2"
# Expected output: (integer) 1

# Check for a number that does not exist
redis-cli SISMEMBER numbers "5"
# Expected output: (integer) 0
```

---

## Example 4: Case Sensitivity

```bash
# Add a lowercase value
redis-cli SADD names "alice"

# Check with different case
redis-cli SISMEMBER names "Alice"
# Expected output: (integer) 0
```

Remember, Redis sets are case-sensitive and store string values as-is.
