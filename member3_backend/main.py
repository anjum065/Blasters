from fastapi import FastAPI

app = FastAPI(
    title="Subscription Management System",
    description="Member 3 Backend",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }

@app.get("/test")
def test():
    return {
        "status": "Working",
        "member": 3,
        "modules": ["Invoices", "Payments", "Discounts"]
    }