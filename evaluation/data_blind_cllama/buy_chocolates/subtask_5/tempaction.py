def act(robot,env,camera):
    # Subtask 4: Move to the chocolates
    chocolates = registry(env,"chocolates_177")
    MoveBot(env, robot, chocolates, camera)
    donothing(env)

