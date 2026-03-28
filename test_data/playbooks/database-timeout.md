# Runbook: Database Connection Timeouts

## Overview
This runbook provides troubleshooting steps for database connection timeout incidents.

## Symptoms
- Connection timeout errors in application logs
- Increased application latency
- Failed database transactions
- Connection pool exhaustion warnings
- Users experiencing slow or failed requests

## Common Causes
1. **Incorrect timeout configuration** - Timeout values set too low
2. **Database overload** - Database CPU/memory at capacity
3. **Network issues** - Connectivity problems between app and database
4. **Connection pool exhaustion** - Too few connections in pool
5. **Long-running queries** - Queries exceeding timeout threshold
6. **Database locks** - Transactions holding locks for extended periods

## Diagnosis Steps

### 1. Check Application Logs
```
Look for:
- Connection timeout error messages
- Timeout duration (e.g., "timeout: 30s")
- Frequency of timeouts
- Connection pool status
```

### 2. Check Database Metrics
```
Verify:
- CPU usage (should be < 80%)
- Memory usage (should be < 85%)
- Active connections count
- Slow query log
- Lock wait times
```

### 3. Check Network
```
Test:
- Ping database host
- Check network latency
- Verify firewall rules
- Check for packet loss
```

### 4. Review Recent Changes
```
Investigate:
- Recent deployments
- Configuration changes
- Database schema changes
- Timeout value modifications
```

## Resolution Steps

### Immediate Actions
1. **Check if timeout was recently reduced** - If yes, consider reverting
2. **Verify database health** - Ensure DB is not overloaded
3. **Increase connection pool size** - If pool is exhausted
4. **Rollback recent changes** - If issue started after deployment

### Short-term Fixes
1. Increase timeout values to safe levels (60s minimum for most workloads)
2. Scale up database resources if needed
3. Optimize slow queries
4. Adjust connection pool settings

### Long-term Prevention
1. **Load testing** - Test configuration changes under load before production
2. **Monitoring** - Set up alerts for connection pool exhaustion
3. **Query optimization** - Regular review of slow queries
4. **Capacity planning** - Plan for growth in database resources
5. **Configuration management** - Document safe timeout values
6. **Canary deployments** - Test config changes on subset of traffic first

## Configuration Best Practices

### Recommended Timeout Values
```
Connection timeout: 60-120 seconds (workload dependent)
Query timeout: 30-60 seconds
Connection pool:
  - Minimum connections: 10
  - Maximum connections: 100-200 (based on DB capacity)
```

### Warning Signs
- Connection pool usage > 80%
- Average query time > 5 seconds
- Database CPU > 80%
- Timeout errors > 1% of requests

## Escalation
Escalate to Database team if:
- Database metrics show resource exhaustion
- Query performance degradation
- Database locks detected
- Issue persists after configuration rollback

## Related Runbooks
- Database Performance Tuning
- Connection Pool Configuration
- Query Optimization Guide
