def act(robot,env,camera):
    # Subtask 1: Move the robot to the beet
    beet_275 = registry(env,"beet_275")
    MoveBot(env, robot, beet_275, camera)
    donothing(env)

