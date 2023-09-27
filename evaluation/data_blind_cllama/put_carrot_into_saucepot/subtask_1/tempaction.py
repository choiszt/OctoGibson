def act(robot,env,camera):
    # Subtask 1: Move the robot to the carrot
    carrot_178 = registry(env,"carrot_178")
    MoveBot(env, robot, carrot_178, camera)
    donothing(env)

