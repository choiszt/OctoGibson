def act(robot,env,camera):
    # Subtask 1: Move the robot to the fridge
    fridge = registry(env,"fridge_xyejdx_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)

