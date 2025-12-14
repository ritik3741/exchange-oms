# Exchange Order Management System (OMS)

## Overview
This project is a **simulated exchange-style Order Management System (OMS)** built using Python and REST APIs.  
It demonstrates how real trading systems handle the **complete order lifecycle** along with **testing and certification-style validations**.

The system is designed for learning and interview demonstration purposes.

---

## Features
- Create New Orders
- Modify existing orders (only if order is NEW)
- Cancel orders (only if order is NEW)
- Execute orders (final state)
- View all orders stored in database
- Enforced exchange-style order state rules
- Database-backed persistence
- Manual testing and certification documentation

---

## Order Lifecycle
NEW → MODIFIED → EXECUTED
NEW → CANCELLED

---


Once an order is **EXECUTED**, it cannot be modified or cancelled.

---

## Technology Stack
- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **API Style:** REST
- **Version Control:** Git & GitHub
- **Environment:** Linux / Windows
- **Testing:** Manual testing & certification-style validation

---

## API Endpoints

### Create New Order
`POST /order`

### Modify Order
`PUT /order/{order_id}`  
(Allowed only for NEW orders)

### Cancel Order
`DELETE /order/{order_id}`  
(Allowed only for NEW orders)

### Execute Order
`POST /order/{order_id}/execute`  
(Final state)

### View All Orders
`GET /orders`

---

## Testing & Certification
The system was tested using:
- Functional testing
- End-to-end order lifecycle validation
- Negative testing (invalid state transitions)
- Backend data verification
- Certification-style checklist similar to broker/exchange systems

Test documents included:
- Test Plan
- Test Cases
- Certification Checklist

---

## How to Run the Project

### 1. Install dependencies
pip install fastapi uvicorn sqlalchemy


### 2. Start the server
uvicorn main:app --reload


### 3. Open API documentation
Open browser and go to:
http://127.0.0.1:8000/docs


---

## Learning Outcome
This project helped in understanding:
- Exchange order workflows
- OMS lifecycle management
- REST API design
- Database persistence
- Certification and conformance testing
- Real-world trading system logic

---

## Author
**Ritik Kumar**
