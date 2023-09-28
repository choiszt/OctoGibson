def act(robot,env,camera):
    # Subtask 1: Move the Robot to the Fruit
    fruit = registry(env, "fruit_88")
    MoveBot(env,"robot", fruit, camera)
    donothing(env)

