def act(robot,env,camera):
    # Subtask 3: Move the robot to the toast
    toast_150 = registry(env,"toast_150")
    MoveBot(env, robot, toast_150, camera)
    donothing(env)

