# F1 Race Insights Dashboard

## Project Overview

The **F1 Race Insights & Analysis Platform** is a cloud-native application that ingests, processes, and visualizes data from the Formula 1 FastF1 API. The platform enables users to explore detailed race statistics, compare driver performance, and analyze trends across different race events. 

This project leverages a serverless architecture on AWS, using services like **AWS Lambda**, **API Gateway**, **DynamoDB**, **S3**, and **CloudFront** to deliver scalable and resilient functionality. Additionally, Infrastructure as Code (IaC) is used to automate the deployment and management of resources, ensuring an agile, modern workflow.

## Key Features
- **Race Data Ingestion**: Automatically retrieve race session data (lap times, sector times, tire usage, etc.) from the FastF1 API after each race event.
- **Driver Comparison**: Compare driver performance across different races and events.
- **Historical Data Trends**: Visualize trends and insights such as lap times, tire degradation, and sector performance.
- **API-Driven Backend**: Expose race data and statistics through a RESTful API for front-end consumption.
- **Interactive Dashboard**: A web-based interface for viewing and interacting with race data.


## Future Goals
- **Predictive Analytics**: Use machine learning to predict how a driver might perform in future races based on historical data.
- **Performance Leaderboard**: rank drivers/teams on performance across the race (qualifying, overtakes, consistancy etc)

## Services and Tools used
- **AWS Lambda**: For serverless processing and data handling.
- **Amazon API Gateway**: To expose RESTful APIs for accessing race data.
- **Amazon DynamoDB**: To store and query race session data.
- **Amazon S3 & CloudFront**: For hosting and delivering the front-end web application.
- **[FastF1 API](https://docs.fastf1.dev/)**: For retrieving Formula 1 race data after each session.
- **GitHub Actions**: CI/CD pipeline for automated deployment.
- **Infrastructure as Code (IaC)**: Using AWS CloudFormation for resource management.

## Why This Project?
This project showcases the integration of real-world data with modern cloud technologies, making it an ideal demonstration of skills in serverless architecture, API development, cloud scalability, and data-driven insights. Whether you're an F1 fan or a cloud enthusiast, this platform combines exciting data with cutting-edge technology.

## Project Status
**In Progress**: Currently working on setting up core Lambda functions to ingest data from the FastF1 API and designing the initial front-end dashboard.
See my [Journey](./docs/journey.md) here

## How to Get Started
- Clone this repository.
- Set up your AWS credentials.
- Deploy the infrastructure using the provided CloudFormation templates.
- Install dependencies and run the project locally.

Check the [Architecture](./docs/architecture.md) and [Data Flow](./docs/data-flow.md) for more details on the design.

