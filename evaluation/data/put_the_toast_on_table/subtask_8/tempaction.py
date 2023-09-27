def act(robot,env,camera):
    # Subtask 3: Move to the toast
    toast_191 = registry(env,"toast_191")
    MoveBot(env, robot, toast_191, camera)
    donothing(env)

