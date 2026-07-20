# VPC Network Architecture - Project 3

## Overview

Built a production-grade VPC on AWS with:
-Public subnet for web servers (internet-accessible)
-Private subnet for databases (hidden from internet)
-Internet Gateway for public access
-NAT Gateway for secure private subnet outbound traffic
-Security groups with least-privilege access

## Components

### VPC Configuration
-Name: icp-vpc
-CIDR Block: 10.0.0.0/16
-Region: us-east-2

### Subnets
-Public: 10.0.1.0/24 (256 IPs)
-Private: 10.0.2.0/24 (256 IPs)

### Security
-Public SG allows: HTTP, HTTPS, SSH
-Private SG allows: MySQL only from public subnet
-NAT Gateway prevents unsolicited inbound traffic to private subnet

### Traffic Flow
-Public subnet → Internet Gateway → Internet (direct)
-Private subnet → NAT Gateway → Internet (secure)
-Internet → NAT Gateway ↛ Private subnet (blocked)

## Architecture Diagram

See VPC-Architecture-Diagram.txt

## Cost

Free tier eligible (1 VPC free, 1 NAT Gateway ~$32/month if used heavily)