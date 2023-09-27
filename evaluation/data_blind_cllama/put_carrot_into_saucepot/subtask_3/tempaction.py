def act(robot,env,camera):
    # Subtask 3: Move the robot to the saucepot
    saucepot_170 = registry(env,"saucepot_170")
    MoveBot(env, robot, saucepot_170, camera)
    donothing(env)

