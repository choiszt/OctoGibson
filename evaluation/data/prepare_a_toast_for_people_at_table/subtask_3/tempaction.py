def act(robot,env,camera):
    # Subtask 1: Move to front of fridge
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env.0, robot, fridge, camera)
    donothing(env)

