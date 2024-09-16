# F1 Race Insights Platform - Security

## Overview
Security is critical to ensuring that data and resources in the F1 Race Insights Platform are protected from unauthorized access, data breaches, and other vulnerabilities. This document outlines the security strategies used to secure the infrastructure, data, and user interactions.

## Security Measures

### 1. **IAM Roles and Policies**
- **AWS Lambda & DynamoDB Permissions**: Lambda functions are given the least privilege necessary, with IAM roles that allow read/write access only to the specific DynamoDB tables they interact with.
- **API Gateway Permissions**: API Gateway is configured to only allow access to specific Lambda functions using **IAM roles**.
- **Principle of Least Privilege**: All AWS resources are restricted to the minimum permissions required.

### 2. **API Gateway Security**
- **Rate Limiting**: API Gateway uses rate limiting to control the number of requests, preventing abuse or denial-of-service attacks.
- **Authorization**: In the future, **AWS Cognito** will be used to provide user authentication and role-based access control.
- **HTTPS**: All API Gateway endpoints are configured to only accept HTTPS traffic to ensure data is encrypted in transit.

### 3. **Data Security**
- **Encryption at Rest**: Data stored in **DynamoDB** and **S3** is encrypted at rest using AWS-managed encryption keys.
- **Encryption in Transit**: All data transferred between services (e.g., from Lambda to DynamoDB, API Gateway to Lambda) is encrypted via HTTPS.
- **S3 Bucket Policies**: Public access to S3 buckets is tightly controlled, and only the necessary static assets (like front-end files) are exposed to the public.

### 4. **Monitoring and Auditing**
- **CloudWatch Alarms**: CloudWatch is configured to trigger alarms for any unusual activity,
