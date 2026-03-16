# Fundamentals: Redis Sets

## Redis CLI Commands: Adding and Removing Set Members

This guide demonstrates how to use `SADD` and `SREM` commands with the Redis CLI to add and remove members from a set.

## Adding Members with `SADD`

To add one or more members to a set:

```bash
redis-cli SADD myset "member1"
redis-cli SADD myset "member2" "member3"
```

- `myset` is the name of the Redis set.
- `"member1"`, `"member2"`, etc. are the elements you want to add.

### Example:

```bash
redis-cli SADD fruits "apple" "banana" "cherry"
```

## Removing Members with `SREM`

To remove one or more members from a set:

```bash
redis-cli SREM myset "member1"
redis-cli SREM myset "member2" "member3"
```

### Example:

```bash
redis-cli SREM fruits "banana"
```

This will remove `"banana"` from the `fruits` set if it exists.

## Verifying the Set Contents

To check the contents of the set:

```bash
redis-cli SMEMBERS myset
```

### Example:

```bash
redis-cli SMEMBERS fruits
```

This will list all remaining members in the `fruits` set.

