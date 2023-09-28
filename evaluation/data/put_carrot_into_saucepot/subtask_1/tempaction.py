def act(robot,env,camera):
    # Subtask 1: Move tothe refrigerator
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(environment, robot, fridge, camera)
    donothing(env)

