def act(robot,env,camera):
    # Subtask 1: Move the bot to the peashes.
    peaches_173 = registry(env,"peachys_173")
    MoveBot(env, robot, peaches_163, camera)
    donothing(env)

