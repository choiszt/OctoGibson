def act(robot,env,camera):
    # Subtask 1: Move therobotto thebowl
    bowl_194 = registry(env,"bowl-194")
    MoveBot(env, robot, bowl_194, camera)

