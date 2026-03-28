# Runbook: Memory Leak Detection and Resolution

## Overview
This runbook covers identification and resolution of memory leak incidents in Java applications.

## Symptoms
- Continuously increasing memory usage over time
- Frequent garbage collection (GC) cycles
- OutOfMemoryError exceptions
- Application becomes unresponsive
- High CPU usage due to excessive GC
- Application restarts don't resolve the issue long-term

## Common Causes
1. **Unbounded caches** - Caches without eviction policies
2. **Static collections** - Static lists/maps that grow indefinitely
3. **Event listeners** - Not properly deregistered
4. **ThreadLocal misuse** - Not cleaned up properly
5. **Database connection leaks** - Connections not closed
6. **Large object retention** - Objects held in memory unnecessarily

## Diagnosis Steps

### 1. Monitor Memory Trends
```
Check:
- Heap memory usage over time (should stabilize after GC)
- GC frequency and duration
- Old generation memory (should not continuously grow)
- Number of loaded classes
```

### 2. Analyze Heap Dump
```
Trigger heap dump:
- jmap -dump:live,format=b,file=heap.bin <pid>

Analyze with tools:
- Eclipse MAT (Memory Analyzer Tool)
- VisualVM
- JProfiler
```

### 3. Check Application Logs
```
Look for:
- OutOfMemoryError messages
- Excessive GC log entries
- Warnings about resource exhaustion
- Cache size metrics
```

### 4. Review Recent Code Changes
```
Investigate:
- New caching implementations
- Collection usage patterns
- Resource management code
- Static variable additions
```

## Resolution Steps

### Immediate Actions
1. **Restart application** - Provides temporary relief
2. **Increase heap size** - Buys time for investigation (not a fix)
3. **Enable heap dump on OOM** - For post-mortem analysis
   ```
   -XX:+HeapDumpOnOutOfMemoryError
   -XX:HeapDumpPath=/var/logs/heapdump.hprof
   ```

### Short-term Fixes
1. **Clear problematic cache** - If cache is identified as culprit
2. **Restart on schedule** - Until permanent fix is deployed
3. **Reduce cache TTL** - Temporary mitigation

### Root Cause Fix
1. **Add cache eviction policy**
   ```java
   Cache with TTL and max size:
   - Time-to-live: 1-4 hours
   - Max entries: Based on expected load
   - LRU eviction when full
   ```

2. **Fix resource leaks**
   ```java
   try (Connection conn = getConnection()) {
       // Use connection
   } // Auto-closed
   ```

3. **Remove static collection growth**
   ```java
   Use bounded collections:
   - ConcurrentLinkedQueue with size checks
   - Guava Cache with eviction
   - Caffeine cache
   ```

### Long-term Prevention
1. **Code review checklist** - Review cache implementations
2. **Memory profiling** - Regular profiling in test environments
3. **Monitoring alerts** - Alert on memory trends
4. **Load testing** - Test memory behavior under sustained load
5. **Cache guidelines** - Document caching best practices
6. **Resource management patterns** - Use try-with-resources

## Cache Configuration Best Practices

### Recommended Settings
```
Maximum entries: 10K-1M (based on data size)
TTL: 1-4 hours (based on data freshness requirements)
Eviction policy: LRU (Least Recently Used)
Memory limit: 10-20% of heap max

Example with Caffeine:
Cache<Key, Value> cache = Caffeine.newBuilder()
    .maximumSize(500_000)
    .expireAfterWrite(3, TimeUnit.HOURS)
    .build();
```

### Warning Signs
- Heap usage grows continuously without plateau
- GC time > 10% of CPU time
- Old generation > 85% after full GC
- Heap usage doesn't drop after GC

## Investigation Tools

### JVM Flags for Diagnosis
```
-XX:+PrintGCDetails
-XX:+PrintGCDateStamps
-Xloggc:/var/logs/gc.log
-XX:+HeapDumpOnOutOfMemoryError
```

### Heap Dump Analysis
```
Key metrics to check:
- Objects by retained size
- Duplicate strings
- Collection sizes
- Objects grouped by class
```

## Escalation
Escalate to Platform team if:
- Memory leak source not identified within 2 hours
- Leak spans multiple services
- JVM tuning required
- Infrastructure-level memory issues suspected

## Related Runbooks
- JVM Performance Tuning
- Garbage Collection Optimization
- Cache Configuration Guide
- Resource Management Best Practices
