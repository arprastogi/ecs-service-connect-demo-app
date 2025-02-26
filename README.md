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
