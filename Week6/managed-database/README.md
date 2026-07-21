# Project 4: Managed Database Deployment (RDS)

## Overview
Built an enterprise-grade RDS database with Multi-AZ automatic failover, read replicas for scaling, automated backups, and CloudWatch monitoring.

## What I Built

### Primary Database
- DB instance: icp-prod-database
- Engine: MySQL 8.0.x
- Class: db.m7g.large
- Multi-AZ: Enabled (automatic standby in different AZ)
- Storage: Auto-scaling up to 100GB

### High Availability
- Primary database in one availability zone
- Automatic standby replica in another AZ
- Automatic failover if primary fails (2-3 minutes)
- Zero data loss during failover

### Read Replica
- Instance: icp-prod-database-replica
- Purpose: Handle read-heavy workloads
- Separate copy for scaling reads
- Independent from primary failover

### Features Enabled
- Automated daily backups (7 day retention)
- Enhanced monitoring (60 second granularity)
- Performance Insights
- CloudWatch alarms for CPU/performance

## Key Learning Outcomes

### Multi-AZ Deployment
- Automatic failover without manual intervention
- Synchronous replication to standby
- Zero downtime during failures
- How Netflix, Uber, Amazon build reliability

### Read Replicas
- Horizontal scaling for reads
- Offload analytics/reporting from primary
- Read-only copy of database
- Multiple replicas possible

### Backup & Recovery
- Point-in-time restore (7 days)
- Automated daily snapshots
- Manual snapshots for long-term
- Insurance against data loss

### Monitoring
- CloudWatch metrics dashboard
- CPU, connections, storage, latency graphs
- Alarms trigger on threshold breaches
- Proactive problem detection

## Real-World Applications

Netflix uses Multi-AZ RDS because:
- Millions of concurrent users
- Database must never go down
- Automatic failover keeps service running
- Read replicas handle massive read traffic

## Cost Breakdown
- Primary DB: ~$0.30/hour (db.m7g.large)
- Standby (Multi-AZ): ~$0.30/hour
- Read Replica: ~$0.30/hour
- Storage & backups: ~$0.10/day
- **Total: ~$50-70/month for all three**

Free tier covers db.t3.micro only, so full setup requires budget.

## Screenshots
[See screenshots folder for visual proof of:
- Primary database configuration
- Multi-AZ standby setup
- Read replica creation
- Monitoring dashboard
- Backup configuration]

## Next Project
Project 5: Container Deployment (ECS) - Running applications in Docker containers at scale!