## 🚨 **Challenges Without Using AWS ECS Service Connect**

When running **microservices on ECS (Amazon Elastic Container Service)** without Service Connect, several challenges arise, especially related to **service discovery, traffic management, monitoring, and resilience.**

---

### ⚠️ **1. Service Discovery and Connectivity Challenges**
- **Manual Service Discovery:** Without Service Connect, ECS services use Elastic Load Balancers (ELB), DNS, or AWS Cloud Map for service discovery, which requires manual setup and management.
- **DNS Caching Issues:** DNS caching may cause delays in discovering updated IPs of ECS tasks, leading to failed connections.
- **Network Configuration Overhead:** Managing security groups, VPC peering, and port mappings manually can lead to configuration drift and connectivity issues.

✅ **Solution with ECS Service Connect**
- Automatic **service discovery and registration** using AWS Cloud Map.
- Built-in **dynamic service registry** that updates in real-time.
- Simplifies networking between ECS services with built-in DNS-based service discovery.

---

### ⚠️ **2. Traffic Management and Load Balancing Challenges**
- **Inconsistent Traffic Routing:** Without Service Connect, traffic routing between ECS services requires using ALBs, NLBs, or manually managing service endpoints.
- **Limited Traffic Control:** You cannot easily route traffic to different versions or subsets of a service (e.g., for blue/green or canary deployments).
- **Manual Load Balancing:** Load balancing between ECS tasks must be manually configured, which increases operational overhead.

✅ **Solution with ECS Service Connect**
- **Automatic Traffic Routing** with fine-grained control over service-to-service communication.
- **Built-in Load Balancing** across ECS tasks without needing an external load balancer.
- Supports **weighted routing** and **failover policies** between service versions.

---

### ⚠️ **3. Lack of Resilience and Failure Handling**
- **No Circuit Breaker or Rate Limiting:** Without Service Connect, handling failures requires manual implementation of retries, timeouts, and fallback mechanisms in application code.
- **Cascading Failures:** When a downstream service fails, it can cause cascading failures across upstream services.
- **Manual Error Handling:** Developers need to write custom logic to manage timeouts and connection retries.

✅ **Solution with ECS Service Connect**
- **Automatic Circuit Breaking** to block requests to unhealthy services.
- **Retry Policies and Failover** logic without modifying application code.
- **Rate Limiting** to prevent services from being overwhelmed.

---

### ⚠️ **4. Limited Observability and Monitoring**
- **Difficult to Trace Requests:** Without Service Connect, distributed tracing requires custom integration with AWS X-Ray or other monitoring tools.
- **Lack of Service-Level Metrics:** ECS services do not natively provide detailed service-to-service metrics.
- **Manual Log Aggregation:** Aggregating logs from multiple services requires setting up CloudWatch or third-party solutions.

✅ **Solution with ECS Service Connect**
- **Built-in Observability** with CloudWatch and AWS X-Ray for distributed tracing.
- Automatic **service-to-service telemetry** to measure request latency, failure rates, and throughput.
- Real-time **monitoring and alerting** on critical metrics.

---

### ⚠️ **5. Increased Operational Complexity**
- **Manual Configuration Management:** Without Service Connect, managing service communication configurations requires extensive Terraform/CloudFormation scripts.
- **Complex Security Management:** Enforcing security policies between ECS services requires fine-tuning security groups, IAM roles, and network ACLs.
- **No Native Encryption or Authentication:** Service-to-service communication security has to be managed separately.

✅ **Solution with ECS Service Connect**
- **Simplified Configuration Management** through ECS task definition and Cloud Map integration.
- **Service-Level Security Policies** with automatic traffic encryption and secure service communication.

---

### ⚠️ **6. Deployment and Scaling Complexity**
- **Manual Scaling of Service Dependencies:** Without Service Connect, scaling dependencies between ECS services requires explicit configuration.
- **Slow Rollbacks and Failovers:** Rollbacks and failovers to healthy service versions may be delayed or manual.

✅ **Solution with ECS Service Connect**
- **Auto-scaling with Traffic Control** based on load and performance.
- **Faster Rollbacks and Failovers** with automatic health checks and circuit breaker policies.

---

## 🎯 **Key Benefits of Using ECS Service Connect**
✅ **Simplified Service Discovery and Connectivity**  
✅ **Built-in Traffic Management and Load Balancing**  
✅ **Resilient Microservices with Circuit Breakers and Rate Limiting**  
✅ **Comprehensive Observability and Monitoring**  
✅ **Reduced Operational Overhead and Configuration Complexity**  

Would you like a **hands-on guide** on enabling ECS Service Connect in your environment? 🚀

---------------------------------------------------------------------------------------



## ⚡️ **1. Challenges If We Are Not Using ECS Service Connect**

When running microservices on Amazon ECS **without Service Connect**, several challenges arise:

---

### ⚠️ **A. Service Discovery and Connectivity Issues**
- **Manual Service Discovery:** Requires configuring AWS Cloud Map, ELBs, or DNS-based routing.
- **DNS Caching Delays:** DNS caching may lead to delayed updates, causing service connectivity issues.
- **Increased Network Complexity:** Managing port mappings, security groups, and VPC peering can be error-prone.

---

### ⚠️ **B. Traffic Management and Routing Challenges**
- **Limited Traffic Control:** No built-in weighted routing or subset routing capabilities.
- **Manual Load Balancing:** Traffic is manually routed to ECS tasks, increasing operational burden.
- **Version Rollout Complexity:** Blue/green or canary deployments require additional configurations.

---

### ⚠️ **C. Lack of Resilience and Failure Management**
- **No Circuit Breakers or Retries:** Failures cascade across services without automated fallback.
- **Manual Error Handling:** Application code needs to implement retry policies and timeouts.
- **Increased Downtime Risks:** Failures in downstream services may impact upstream services.

---

### ⚠️ **D. Limited Observability and Monitoring**
- **No Native Distributed Tracing:** Tracking service-to-service requests requires custom integration.
- **Manual Log Aggregation:** Centralizing logs and metrics from multiple ECS tasks is cumbersome.
- **Inadequate Failure Insights:** Limited visibility into request failures and connection errors.

---

### ⚠️ **E. Higher Operational Complexity**
- **Manual Security Configurations:** Enforcing service-to-service security requires complex IAM, SG, and NACL setups.
- **Slow Rollbacks and Failovers:** Failover and rollback mechanisms require manual intervention.

---

---

## 🚀 **2. What We Solve by Using ECS Service Connect**

By **enabling ECS Service Connect**, the following challenges are addressed effectively:

---

### ✅ **A. Simplified Service Discovery and Connectivity**
- **Auto Service Discovery:** Automatically registers and updates service instances in Cloud Map.
- **Real-time DNS Updates:** Eliminates delays caused by DNS caching.
- **Simplified Network Management:** Automatically manages VPC networking and service communication.

---

### ✅ **B. Intelligent Traffic Management and Routing**
- **Built-in Traffic Routing:** Routes traffic dynamically to the best available service instance.
- **Weighted Traffic Splitting:** Supports gradual rollout and A/B testing with traffic control.
- **Seamless Blue/Green Deployments:** Manages traffic shifts between old and new versions effortlessly.

---

### ✅ **C. Enhanced Resilience and Failure Handling**
- **Automatic Circuit Breakers:** Prevents cascading failures by ejecting unhealthy services.
- **Retries and Failovers:** Automatically retries failed requests and fails over to healthy instances.
- **Rate Limiting:** Protects downstream services from request overload.

---

### ✅ **D. Comprehensive Observability and Monitoring**
- **Built-in Metrics and Logs:** CloudWatch collects request counts, latencies, and failures.
- **Distributed Tracing with X-Ray:** Provides deep insights into request flows and bottlenecks.
- **Automatic Log Aggregation:** Consolidates logs for easier troubleshooting.

---

### ✅ **E. Reduced Operational Complexity**
- **Automated Configuration Management:** Simplifies service communication setup.
- **Enhanced Security and Encryption:** Ensures secure service-to-service communication.
- **Faster Rollbacks and Failovers:** Automatic rollback and traffic redirection to healthy instances.

---

## 🎯 **Summary**
✅ ECS Service Connect **automates service discovery, routing, resilience, and observability**, reducing operational complexity and improving system reliability.  
✅ Without Service Connect, organizations face **higher maintenance overhead, connectivity issues, and poor failure handling.**


------------------------------------------------------------------



## ✅ **mTLS (Mutual TLS) in ECS Service Connect**

Yes, **ECS Service Connect** supports **mTLS (Mutual TLS)** to ensure **secure and encrypted communication** between services running within an ECS cluster. mTLS enhances security by requiring **both client and server** to authenticate each other before establishing a connection.

---

## 🔐 **How mTLS Works in ECS Service Connect**
1. **Mutual Authentication:**  
   - Both the client (service initiating the request) and the server (service receiving the request) exchange TLS certificates for authentication.
   - The client verifies the server’s certificate, and the server verifies the client’s certificate.

2. **Data Encryption:**  
   - All communication between services is encrypted using TLS 1.2/1.3.
   - Prevents unauthorized access and mitigates risks of man-in-the-middle (MITM) attacks.

---

## ⚙️ **Enabling mTLS for ECS Service Connect**

### **Step 1: Configure a TLS-Enabled Namespace in AWS Cloud Map**
ECS Service Connect relies on **AWS Cloud Map** for service discovery. You need to configure a namespace with **TLS settings enabled**.

1. Open the **AWS Management Console**.
2. Go to **AWS Cloud Map**.
3. Create a namespace with **TLS encryption enabled**.
4. Add the ECS services that require mTLS.

---

### **Step 2: Define Service Connect Configuration in ECS Task Definition**
Add the **serviceConnectConfiguration** to the ECS task definition with mTLS enabled.

```json
{
  "serviceConnectConfiguration": {
    "enabled": true,
    "namespace": "my-tls-enabled-namespace",
    "services": [
      {
        "portName": "https",
        "discoveryName": "serviceA",
        "clientAliases": [{"port": 443}]
      }
    ],
    "encryptionConfiguration": {
      "certificateArn": "arn:aws:acm:region:account-id:certificate/certificate-id",
      "mode": "MUTUAL_TLS"
    }
  }
}
```
- `certificateArn`: The ARN of the certificate stored in **AWS Certificate Manager (ACM)**.
- `mode`: Set to `MUTUAL_TLS` to enforce mutual authentication.

---

### **Step 3: Configure IAM Policies for ECS Task Execution Role**
Ensure that the **ECS task execution role** has permissions to retrieve certificates from ACM.

```json
{
  "Effect": "Allow",
  "Action": [
    "acm:DescribeCertificate",
    "acm:GetCertificate",
    "secretsmanager:GetSecretValue"
  ],
  "Resource": "*"
}
```

---

### **Step 4: Deploy ECS Services with Service Connect Enabled**
Deploy your ECS services using this updated task definition. ECS Service Connect will automatically manage **mTLS communication** between services.

---

## 🎯 **Benefits of Using mTLS in ECS Service Connect**
✅ **Mutual Authentication:** Ensures both client and server identities are verified.  
✅ **Data Privacy and Encryption:** Protects data with TLS encryption.  
✅ **Secure Service-to-Service Communication:** Prevents unauthorized access and potential cyber threats.  
✅ **Compliance with Security Standards:** Meets enterprise-level compliance and security requirements.

---

## ⚡️ **Considerations When Using mTLS**
- **Certificate Management:** Ensure that certificates in ACM are rotated and managed securely.
- **Performance Impact:** TLS adds minimal latency, but it’s negligible in most microservice use cases.
- **Certificate Expiry Monitoring:** Set up AWS Certificate Manager notifications to avoid downtime due to certificate expiry.

Would you like a **Terraform or CLI example** to automate the configuration? 🚀

----------------------------------------------------------
----------------------------------------------------------

# Redis 

Deploying a **Python demo application** in **AWS ECS Fargate** with **AWS Redis Cache** involves several steps. Here’s a detailed step-by-step guide:  

---

## **Step 1: Setup AWS Environment**
### **1.1 Install AWS CLI and Docker**
Ensure you have AWS CLI and Docker installed on your local machine.  
- Install AWS CLI: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)  
- Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)  
- Install AWS CDK (optional for Infrastructure as Code):  
  ```sh
  npm install -g aws-cdk
  ```

### **1.2 Configure AWS CLI**
Authenticate with AWS:  
```sh
aws configure
```
Enter the **AWS Access Key**, **Secret Key**, **Region**, and **Output Format**.

---

## **Step 2: Create a Python Demo Application**
### **2.1 Create a New Python Project**
```sh
mkdir python-ecs-demo
cd python-ecs-demo
python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```
### **2.2 Install Dependencies**
```sh
pip install flask redis
```

### **2.3 Create `app.py`**
This application will connect to AWS Redis Cache (Elasticache) and store/retrieve data.
```python
from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    return "Welcome to Python ECS Fargate Demo with Redis!"

@app.route("/set-cache", methods=["POST"])
def set_cache():
    data = request.get_json()
    key = data.get("key")
    value = data.get("value")
    if key and value:
        redis_client.set(key, value)
        return jsonify({"message": f"Cached key: {key} with value: {value}"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route("/get-cache/<key>", methods=["GET"])
def get_cache(key):
    value = redis_client.get(key)
    if value:
        return jsonify({key: value}), 200
    return jsonify({"error": "Key not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## **Step 3: Create a Docker Image**
### **3.1 Create `Dockerfile`**
```dockerfile
# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install flask redis

# Expose port
EXPOSE 5000

# Start application
CMD ["python", "app.py"]
```

### **3.2 Build and Test Locally**
```sh
docker build -t python-ecs-demo .
docker run -p 5000:5000 --env REDIS_HOST=localhost python-ecs-demo
```
Test the API with:
```sh
curl -X POST "http://localhost:5000/set-cache" -H "Content-Type: application/json" -d '{"key": "message", "value": "Hello from ECS!"}'
curl -X GET "http://localhost:5000/get-cache/message"
```

---

## **Step 4: Push Docker Image to AWS ECR**
### **4.1 Create an AWS ECR Repository**
```sh
aws ecr create-repository --repository-name python-ecs-demo
```
Get the repository URL:
```sh
aws ecr describe-repositories --repository-names python-ecs-demo
```

### **4.2 Authenticate and Push Image**
```sh
aws ecr get-login-password | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com
docker tag python-ecs-demo <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/python-ecs-demo
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/python-ecs-demo
```

---

## **Step 5: Deploy AWS ElastiCache Redis**
### **5.1 Create an ElastiCache Redis Cluster**
```sh
aws elasticache create-cache-cluster --cache-cluster-id my-redis --engine redis --cache-node-type cache.t3.micro --num-cache-nodes 1 --security-group-ids <SECURITY_GROUP_ID> --subnet-group-name <SUBNET_GROUP_NAME>
```
Get the Redis endpoint:
```sh
aws elasticache describe-cache-clusters --cache-cluster-id my-redis --show-cache-node-info
```
Use **Primary Endpoint** as `REDIS_HOST`.

---

## **Step 6: Deploy Application to AWS ECS Fargate**
### **6.1 Create ECS Cluster**
```sh
aws ecs create-cluster --cluster-name python-ecs-cluster
```

### **6.2 Create a Task Definition**
Create `task-def.json`:
```json
{
  "family": "python-ecs-task",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "python-container",
      "image": "<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/python-ecs-demo",
      "memory": 512,
      "cpu": 256,
      "essential": true,
      "portMappings": [
        {
          "containerPort": 5000,
          "hostPort": 5000
        }
      ],
      "environment": [
        {
          "name": "REDIS_HOST",
          "value": "<REDIS_ENDPOINT>"
        },
        {
          "name": "REDIS_PORT",
          "value": "6379"
        }
      ]
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512"
}
```
Register the task definition:
```sh
aws ecs register-task-definition --cli-input-json file://task-def.json
```

### **6.3 Run the Task on Fargate**
```sh
aws ecs run-task --cluster python-ecs-cluster --launch-type FARGATE --task-definition python-ecs-task --network-configuration "awsvpcConfiguration={subnets=[<SUBNET_ID>],securityGroups=[<SECURITY_GROUP_ID>],assignPublicIp=\"ENABLED\"}"
```

---

## **Step 7: Test the Application**
Get the **public IP** of the running ECS task:
```sh
aws ecs describe-tasks --cluster python-ecs-cluster --tasks <TASK_ID>
```
Test API with:
```sh
curl -X POST "http://<ECS_PUBLIC_IP>:5000/set-cache" -H "Content-Type: application/json" -d '{"key": "greeting", "value": "Hello from Fargate!"}'
curl -X GET "http://<ECS_PUBLIC_IP>:5000/get-cache/greeting"
```

---

## **Step 8: Cleanup Resources**
To delete resources:
```sh
aws ecs delete-cluster --cluster python-ecs-cluster
aws elasticache delete-cache-cluster --cache-cluster-id my-redis
aws ecr delete-repository --repository-name python-ecs-demo --force
```

---

### **Conclusion**
This guide walked through:
✅ Creating a **Flask API**  
✅ Using **AWS ElastiCache Redis**  
✅ **Dockerizing** and **Pushing to ECR**  
✅ Deploying to **ECS Fargate**  

Would you like help automating this with **Terraform or AWS CDK**? 🚀



To **view and manage data** stored in **AWS ElastiCache Redis** via your Python demo application, follow these steps:

---

## ✅ **Step 1: Connect to AWS Redis Cache from Local Machine**
You can interact with Redis Cache directly using a Redis CLI.

### **1.1 Install Redis CLI (if not installed)**
- For Linux:
```bash
sudo apt update && sudo apt install redis-tools
```
- For Mac:
```bash
brew install redis
```
- For Windows:
Download from [Redis GitHub](https://github.com/microsoftarchive/redis/releases).

---

### **1.2 Get Redis Endpoint**
Run this command to get the Redis endpoint:
```bash
aws elasticache describe-cache-clusters --cache-cluster-id my-redis --show-cache-node-info
```
Look for the `Endpoint.Address` and `Port` fields:
```
"Endpoint": {
    "Address": "my-redis.xyz.cache.amazonaws.com",
    "Port": 6379
}
```
Take note of the `Address` and `Port`.

---

### **1.3 Connect to Redis Using CLI**
```bash
redis-cli -h my-redis.xyz.cache.amazonaws.com -p 6379
```
✅ **To verify connection:**
```bash
ping
```
You should get:
```
PONG
```

---

## ✅ **Step 2: View Data in Redis Using CLI**
### **2.1 List All Keys**
```bash
keys *
```
Example output:
```
1) "greeting"
2) "message"
```

### **2.2 Retrieve Value of a Key**
```bash
get greeting
```
Example output:
```
"Hello from Fargate!"
```

### **2.3 Check Key Expiry (TTL)**
```bash
ttl greeting
```
If the key does not have an expiry, it returns `-1`.

---

## ✅ **Step 3: Viewing Cache from Python Application**
You can also retrieve and view cache data through the Flask API endpoints.

### **3.1 Get Cached Data via API**
Use the `GET /get-cache/<key>` endpoint:
```bash
curl -X GET "http://<ECS_PUBLIC_IP>:5000/get-cache/greeting"
```
Example response:
```json
{
  "greeting": "Hello from Fargate!"
}
```

### **3.2 List All Keys Using Python Script**
If you want to list all keys via Python, modify `app.py` by adding this route:
```python
@app.route("/list-keys", methods=["GET"])
def list_keys():
    keys = redis_client.keys('*')
    return jsonify({"keys": keys}), 200
```
Access it by calling:
```bash
curl -X GET "http://<ECS_PUBLIC_IP>:5000/list-keys"
```
Response:
```json
{
  "keys": ["greeting", "message"]
}
```

---

## ✅ **Step 4: Clear or Delete Keys in Redis**
### **4.1 Delete a Specific Key**
```bash
del greeting
```
Response:
```
(integer) 1
```

### **4.2 Flush All Keys (Use with Caution)**
```bash
flushall
```
Response:
```
OK
```

---

## ✅ **Step 5: Monitor Redis Cache Metrics**
To view Redis performance and usage:
1. Open **AWS Management Console**.
2. Go to **ElastiCache > Redis Clusters > my-redis**.
3. Click **Monitoring** to view metrics such as:
   - CPU Utilization
   - Memory Usage
   - Number of Connections
   - Cache Hits/Misses

---

## 🚀 **Bonus: Automate Data Retrieval with a Python Script**
If you need to manage or automate cache data retrieval, create a script:
```python
import redis

redis_host = "my-redis.xyz.cache.amazonaws.com"
redis_port = 6379

# Connect to Redis
client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# List all keys
keys = client.keys('*')
print("Keys in Redis:", keys)

# Get all key-value pairs
for key in keys:
    value = client.get(key)
    print(f"{key}: {value}")
```
Run the script:
```bash
python cache_viewer.py
```

---

## 🎉 **Summary**
✅ List and retrieve cache keys via Redis CLI  
✅ Retrieve cache data using Flask API endpoints  
✅ Monitor Redis Cache usage in AWS Console  
✅ Delete or flush cache keys when needed  

Let me know if you’d like to automate Redis cache management or add logging for cache hits and misses! 🚀


-----------------------------------------------------------------
# ecs-service-connect-demo-app
ecs-service-connect-demo-app


How to Test the Setup
Step 1: Store Data in Each Service
🔹 Store Data in Caller Service
bash
Copy
Edit
curl -X POST "http://<CALLER_SERVICE_PUBLIC_IP>:5000/data" \
     -H "Content-Type: application/json" \
     -d '{"user": "Alice", "message": "Hello from Caller Service!"}'
✅ Expected Response

json
Copy
Edit
{
  "message": "Data stored successfully in Service A",
  "stored_data": {
    "user": "Alice",
    "message": "Hello from Caller Service!"
  }
}
🔹 Store Data in Responder Service
bash
Copy
Edit
curl -X POST "http://<RESPONDER_SERVICE_PUBLIC_IP>:5000/data" \
     -H "Content-Type: application/json" \
     -d '{"user": "Bob", "message": "Hello from Responder Service!"}'
✅ Expected Response

json
Copy
Edit
{
  "message": "Data stored successfully in Service B",
  "stored_data": {
    "user": "Bob",
    "message": "Hello from Responder Service!"
  }
}
Step 2: Fetch Combined Data from Caller Service
bash
Copy
Edit
curl http://<CALLER_SERVICE_PUBLIC_IP>:5000/
✅ Expected Response

json
Copy
Edit
{
  "caller_service_data": [
    {
      "user": "Alice",
      "message": "Hello from Caller Service!"
    }
  ],
  "responder_service_data": [
    {
      "user": "Bob",
      "message": "Hello from Responder Service!"
    }
  ]
}
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------


# 🛡️ ECS Service Connect with TLS/mTLS Chaos Engineering and Log Forwarding

This repository demonstrates how to secure ECS Service Connect with TLS/mTLS, configure ECS tasks for secure communications, and integrate AWS Fault Injection Simulator (FIS) for chaos testing scenarios. It also includes steps to forward ECS Service Connect logs to a Logstash HTTP endpoint on port `5049`.

---

## 📚 Table of Contents
- [Overview](#overview)
- [Chaos Engineering Test Cases](#chaos-engineering-test-cases)
- [Enabling ECS Service Connect Logs to Logstash](#enabling-ecs-service-connect-logs-to-logstash)
- [Configuring AWS Fault Injection Simulator (FIS)](#configuring-aws-fault-injection-simulator-fis)
- [Monitoring and Observability](#monitoring-and-observability)
- [Next Steps](#next-steps)

---

## 🎯 Overview
This project covers the following objectives:

✅ Enable TLS/mTLS communication between ECS services using Service Connect.  
✅ Implement Chaos Engineering with AWS FIS to test TLS/mTLS resilience.  
✅ Forward ECS Service Connect logs to a Logstash HTTP endpoint using Fluent Bit.  

---

## 🔥 Chaos Engineering Test Cases

### 📊 Detailed Chaos Test Scenarios

| ⚡️ Experiment                    | 📝 Hypothesis                                                                 | 🎯 Target                | ⏱️ Duration | 🔍 Test Steps                                                                                   | ⚡️ Expected Outcome                                 |
|-----------------------------------|------------------------------------------------------------------------------|-------------------------|------------|------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 🔥 **Certificate Expiry Test**     | Expired certs should prevent TLS/mTLS connection.                            | ECS Task/Service        | 5 mins     | 1. Modify cert to expire.<br>2. Restart ECS task.<br>3. Attempt connection via Service Connect. | ❌ Connection denied with cert error.               |
| 🔥 **Invalid Client Certificate**  | Connection should be denied with invalid client certificate.                 | ECS Task                | 5 mins     | 1. Replace client cert with invalid cert.<br>2. Restart task.<br>3. Test mTLS call.             | ❌ Connection rejected due to invalid cert.         |
| 🔥 **Revoked Certificate Test**    | Revoked certificates should trigger TLS handshake failure.                   | ECS Task                | 5 mins     | 1. Revoke client cert.<br>2. Use Certificate Revocation List (CRL).<br>3. Attempt connection.   | ❌ Connection fails with cert revocation error.     |
| 🔥 **Certificate Rotation Test**   | Service should automatically pick up new certs.                              | ECS Service             | 5 mins     | 1. Rotate cert in ACM/Secrets Manager.<br>2. Restart ECS service.<br>3. Test secure connection. | ✅ Connection succeeds with new certs.              |
| 🔥 **DNS Spoofing/MITM Test**       | ECS Service Connect should reject spoofed DNS responses.                     | Route 53 Resolver       | 5 mins     | 1. Alter DNS records to simulate MITM.<br>2. Attempt connection.<br>3. Check logs.              | ❌ DNS spoofed requests rejected.                   |
| 🔥 **TLS Downgrade Attack Test**   | Downgraded HTTP connection should be rejected.                               | ECS Task/Service        | 5 mins     | 1. Attempt to communicate over HTTP.<br>2. Observe connection behavior.                        | ❌ HTTP request rejected.                           |
| 🔥 **Backend Service Unavailability** | Failover or retries should occur when backend becomes unavailable.            | ECS Service             | 10 mins    | 1. Stop backend tasks.<br>2. Observe ECS Service Connect retries or failover.                   | ✅ Requests routed to healthy targets.              |
| 🔥 **Simulate High TLS Load**      | TLS connections should not degrade under high traffic.                       | ECS Cluster             | 15 mins    | 1. Simulate high concurrent requests.<br>2. Observe latency and connection stability.           | ✅ No degradation in performance.                   |
| 🔥 **Task Certificate Hot Reload** | ECS tasks should reload new certificates without downtime.                   | ECS Task                | 5 mins     | 1. Update certs.<br>2. Restart ECS tasks.<br>3. Verify mTLS connection.                        | ✅ Zero downtime certificate reload.                |
| 🔥 **Backend Service Certificate Mismatch** | Cert mismatch should trigger connection failure.                       | ECS Service             | 5 mins     | 1. Use mismatched cert on backend.<br>2. Test connection from frontend.                        | ❌ Connection denied due to mismatch.               |
| 🔥 **ECS Cluster Failure Test**    | ECS Service Connect should recover automatically after cluster failure.      | ECS Cluster             | 10 mins    | 1. Simulate ECS cluster failure.<br>2. Restart tasks.<br>3. Observe Service Connect recovery.   | ✅ Service Connect reconnects post-recovery.        |

---

## 📡 Enabling ECS Service Connect Logs to Logstash

### 🛠️ Step 1: Enable ECS Service Connect Logs in Task Definition

```json
"firelensConfiguration": {
  "type": "fluentbit",
  "options": {
    "enable-ecs-log-metadata": "true"
  }
}
