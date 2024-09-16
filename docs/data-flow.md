# F1 Race Insights Platform - Data Flow

## Overview
The data flow within the F1 Race Insights Platform follows a logical path from ingestion of race data to user interaction via the front-end. This document outlines how data moves through the system, starting from the FastF1 API, processing through AWS Lambda, and finally being served via the front-end dashboard.

## Data Flow Steps

### 1. **Data Ingestion**
- **EventBridge** triggers an AWS Lambda function after each race session. The Lambda function retrieves race data (e.g., lap times, sector times, tire data) via the **FastF1 API**.
  
### 2. **Data Processing**
- The Lambda function processes the incoming JSON data, formats it, and enriches it (e.g., calculating averages, fastest lap).
- Processed data is stored in **Amazon DynamoDB** under relevant tables (e.g., `Drivers`, `Races`, `Laps`).

### 3. **Data Storage**
- **DynamoDB** stores race session data in a NoSQL structure that allows for fast querying based on race or driver IDs.
- **Amazon S3** stores any static data related to the race (e.g., driver images, race track maps) that might be used on the front-end.

### 4. **API Access**
- **API Gateway** exposes RESTful APIs to allow the front-end to query the stored race data. API requests trigger specific Lambda functions that retrieve data from DynamoDB and return the results to the user.

### 5. **Frontend Display**
- The front-end, hosted on **S3** and delivered via **CloudFront**, makes API calls to display race data. Users can interact with driver comparisons, visualize trends, and analyze lap times through charts and graphs.

## Data Flow Diagram
[Include a diagram here]

## Future Data Flow Enhancements
- Implementing a more sophisticated data processing pipeline for calculating advanced driver metrics.
- Integrating a real-time streaming component for live race data (future scope as FastF1 does not provide real-time data yet).
