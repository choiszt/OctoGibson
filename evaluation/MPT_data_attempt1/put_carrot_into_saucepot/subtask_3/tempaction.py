def act(robot,env,camera):
    # Subtask 1: Move to The refrigerator
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env.get_camera, fridge, camera)
    donothing(env)

