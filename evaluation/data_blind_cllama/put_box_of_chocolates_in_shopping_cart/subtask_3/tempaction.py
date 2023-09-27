def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop
    countertop = registry(env, "countertop_tpuwys_1")
    MoveBot(env, robot, countertop, camera)
    donothing(env)

