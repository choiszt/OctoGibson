def act(robot,env,camera):
    # Subtask 1: Move to the money from the checkout counter
    money_142 = registry(env,"money_142")
    MoveBot(env, robot, money_142, camera)
    donothing(env)

