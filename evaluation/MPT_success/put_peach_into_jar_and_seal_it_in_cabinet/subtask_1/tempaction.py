def act(robot,env,camera):
    # Subtask 1: Move the Robot to the Peaches
    peaches_173 = registry(env,"peaching_peash_173")
    MoveBot(env, robot, peach_173, camera)
    donothing(env)

