def act(robot,env,camera):
    # Subtask 1: Move therobot to thecabinent
    cab_1 = registry(env.2)
    MoveBot(env, robot, cab_1, camera)
                       
    donothing(env)
                      

