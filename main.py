from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import SessionLocal, OrderDB

app = FastAPI()

class Order(BaseModel):
    symbol: str
    side: str
    quantity: int
    price: float

class ModifyOrder(BaseModel):
    quantity: int
    price: float

@app.post("/order")
def create_order(order: Order):
    db = SessionLocal()
    new_order = OrderDB(
        symbol=order.symbol,
        side=order.side,
        quantity=order.quantity,
        price=order.price,
        status="NEW"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()

    return {
        "message": "Order created",
        "order_id": new_order.id,
        "status": "NEW"
    }

@app.put("/order/{order_id}")
def modify_order(order_id: int, update: ModifyOrder):
    db = SessionLocal()
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()

    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status != "NEW":
        db.close()
        raise HTTPException(status_code=400, detail="Only NEW orders can be modified")

    order.quantity = update.quantity
    order.price = update.price

    db.commit()
    db.close()

    return {
        "message": "Order modified successfully",
        "order_id": order_id,
        "new_quantity": update.quantity,
        "new_price": update.price
    }
@app.delete("/order/{order_id}")
def cancel_order(order_id: int):
    db = SessionLocal()
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()

    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status != "NEW":
        db.close()
        raise HTTPException(status_code=400, detail="Only NEW orders can be cancelled")

    order.status = "CANCELLED"
    db.commit()
    db.close()

    return {
        "message": "Order cancelled successfully",
        "order_id": order_id,
        "status": "CANCELLED"
    }

@app.post("/order/{order_id}/execute")
def execute_order(order_id: int):
    db = SessionLocal()
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()

    if not order:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status != "NEW":
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Only NEW orders can be executed"
        )

    order.status = "EXECUTED"
    db.commit()
    db.close()

    return {
        "message": "Order executed successfully",
        "order_id": order_id,
        "status": "EXECUTED"
    }

@app.get("/orders")
def view_orders():
    db = SessionLocal()
    orders = db.query(OrderDB).all()
    db.close()

    result = []
    for order in orders:
        result.append({
            "order_id": order.id,
            "symbol": order.symbol,
            "side": order.side,
            "quantity": order.quantity,
            "price": order.price,
            "status": order.status
        })

    return result
