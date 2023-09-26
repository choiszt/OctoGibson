def act(robot,env,camera):
    # Subtask 2: Move therobot to theground 
    ground = environment(env, "ground")
    MoveBot(env.env, robot, ground, camera)
    donothing(env)

