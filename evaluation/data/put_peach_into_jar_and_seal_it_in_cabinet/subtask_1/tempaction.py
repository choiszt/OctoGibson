def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop where the peach is located.
    countertop_tpuwys_1 = registry(env,"countertop_tpuwys_1")
    MoveBot(env, robot, countertop_tpuwys_1, camera)
    donothing(env)

