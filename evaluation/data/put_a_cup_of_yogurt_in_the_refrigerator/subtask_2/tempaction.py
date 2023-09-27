def act(robot,env,camera):
    # Subtask 2: Move to the refrigerator
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    MoveBot(env, robot, fridge_xyejdx_0, camera)
    donothing(env)

