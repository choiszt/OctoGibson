def act(robott,envt,camera):
     # Subtask 2: Check if The Carboy is Inside
    carboy = registry (envt,"carboy_185")
        # Check if carboy inside fridge
    if(carboy in fridge):
        return True
    return False

