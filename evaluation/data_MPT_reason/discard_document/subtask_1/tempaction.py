def act(robot,env,camera):
    # Subtask 1: Move the robot to the desks
    desk_erg_0 = registry(env,"desk-erg-0")
    MoveBot(env, robot, desk_erg0, camera)
    donothing(env)

