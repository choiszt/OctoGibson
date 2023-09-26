def act(robott,env,camera):
    # Subtask 1: Register all objects
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env and camera, fridge, camera)
    donothing(env)

