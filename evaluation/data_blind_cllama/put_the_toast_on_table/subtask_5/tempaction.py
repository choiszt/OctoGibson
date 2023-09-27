def act(robot,env,camera):
    # Subtask 4: Grasp the toast from the bottom cabinet
    toast_150 = registry(env,"toast_150")
    MoveBot(env, robot, toast_150, camera)
    donothing(env)

