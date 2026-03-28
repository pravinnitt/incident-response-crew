# Runbook: NullPointerException Resolution

## Overview
This runbook provides guidance for diagnosing and resolving NullPointerException (NPE) incidents.

## Symptoms
- NullPointerException in application logs
- Failed requests with 500 Internal Server Error
- Transactions stuck in incomplete state
- Specific feature/workflow broken
- Stack trace pointing to specific code line

## Common Causes
1. **Missing null checks** - Accessing properties on null objects
2. **Optional fields** - Not handling optional/nullable fields
3. **Database nulls** - NULL values from database not handled
4. **API responses** - Missing fields in external API responses
5. **Configuration issues** - Missing configuration values
6. **Race conditions** - Object not initialized when accessed

## Diagnosis Steps

### 1. Analyze Stack Trace
```
Identify:
- Exact line of code throwing NPE
- Method and class involved
- Which variable is null
- Call chain leading to NPE
```

### 2. Check Application Logs
```
Look for:
- Frequency of NPE (one-off vs. recurring)
- Pattern in affected requests
- Common characteristics (user type, data, workflow)
- Time when NPE started occurring
```

### 3. Review Recent Changes
```
Investigate:
- Code changes to affected method/class
- Database schema changes
- API contract changes
- New features using affected code path
```

### 4. Reproduce Locally
```
Try to reproduce with:
- Sample data that triggered NPE
- Same request parameters
- Edge cases (empty, null, missing fields)
```

## Resolution Steps

### Immediate Actions
1. **Identify affected workflow** - Determine scope of impact
2. **Check if workaround exists** - Can users avoid the issue?
3. **Rollback if recent deployment** - If caused by recent code change
4. **Add temporary null check** - Quick fix while proper solution developed

### Root Cause Fix

#### Add Proper Null Handling
```java
❌ Bad:
public void processOrder(Order order) {
    String address = order.getShippingAddress().trim();
    // NPE if shippingAddress is null
}

✅ Good:
public void processOrder(Order order) {
    String address = order.getShippingAddress();
    if (address != null) {
        address = address.trim();
    }
    // Or use Optional
    String trimmed = Optional.ofNullable(order.getShippingAddress())
        .map(String::trim)
        .orElse("");
}
```

#### Use Java Optional
```java
❌ Bad:
public User getUser(String id) {
    User user = database.findUser(id);
    return user.getName(); // NPE if user not found
}

✅ Good:
public Optional<User> getUser(String id) {
    return Optional.ofNullable(database.findUser(id));
}

// Usage:
getUser(id)
    .map(User::getName)
    .orElse("Unknown");
```

#### Validate Input
```java
✅ Add validation:
public void processOrder(Order order) {
    Objects.requireNonNull(order, "Order cannot be null");
    // Validate optional fields
    if (order.isPickupDelivery()) {
        // Shipping address not required
    } else {
        Objects.requireNonNull(order.getShippingAddress(),
            "Shipping address required for delivery orders");
    }
}
```

### Long-term Prevention
1. **Code review checklist** - Check for null handling
2. **Static analysis** - Use tools like SpotBugs, NullAway
3. **Null-safety annotations** - @NonNull, @Nullable
4. **Use Optional** - For methods that may return null
5. **Fail fast** - Validate inputs early
6. **Unit tests** - Test with null/missing values

## Code Review Checklist

### Check for Null Safety
- [ ] All method parameters validated
- [ ] Optional fields handled properly
- [ ] Database NULL values handled
- [ ] External API responses validated
- [ ] Configuration values have defaults
- [ ] Collections checked before access (isEmpty)

### Testing Requirements
- [ ] Unit test with null inputs
- [ ] Test with missing optional fields
- [ ] Test edge cases
- [ ] Integration tests with real data

## Common NPE Patterns

### Database Results
```java
// Check if result exists
User user = query.getSingleResult();
if (user != null) {
    // Process user
}
```

### Optional Fields
```java
// Handle optional fields
if (order.getShippingAddress() != null) {
    processShipping(order.getShippingAddress());
} else if (order.isPickupDelivery()) {
    processPickup();
}
```

### API Responses
```java
// Validate external API response
ApiResponse response = callExternalApi();
if (response != null && response.getData() != null) {
    process(response.getData());
}
```

## Prevention Best Practices

### Use Modern Java Features
```java
// Java 8+ Optional
Optional<String> address = Optional.ofNullable(user.getAddress());
address.ifPresent(this::processAddress);

// Java 14+ Switch expressions with null check
String result = switch (Optional.ofNullable(status)) {
    case Optional.of("ACTIVE") -> "Active user";
    case Optional.of("INACTIVE") -> "Inactive user";
    default -> "Unknown status";
};
```

### Annotation-based Null Safety
```java
import javax.annotation.Nonnull;
import javax.annotation.Nullable;

public void processUser(@Nonnull User user, @Nullable String notes) {
    // IDE and tools can warn if null passed for user
}
```

## Escalation
Escalate to development team lead if:
- NPE cause not identified within 1 hour
- Affects critical business workflow
- No obvious fix available
- Requires architectural changes

## Related Runbooks
- Exception Handling Best Practices
- Input Validation Guide
- Code Review Standards
- Java Best Practices
