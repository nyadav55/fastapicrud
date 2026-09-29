from fastapi import FastAPI
from pydantic import BaseModel # Predefine basemodel help in validation auto generated
from typing import List 

app = FastAPI()

class Car(BaseModel):
    id : int
    name : str
    model : str
cars: List[Car] = []


@app.get("/") #decoraters
def hello():
    return {"message": "Welcome Car Bazar"}

@app.get("/cars")
def get_cardata():
    return cars

@app.post("/cars")
def add_cardata(car : Car):
    cars.append(car) 
    return car

@app.put("/cars/{car_id}")
def update_cardata(car_id  : int, updated_car: Car):
    for index, car in enumerate(cars): # enumerate  check each row carid and fetch 
        if car.id == car_id:
            cars[index] = updated_car
            return updated_car
    return {"error": "Car not found!"}    

@app.delete("/cars/{car_id}")     
def delete_car(car_id: int):
    for index, car in enumerate(cars):
        if car.id == car_id:
            delete = cars.pop(index)
            return delete
    return {"error": "Car not found !"}        
      
