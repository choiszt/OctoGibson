def act(robot,env,camera):
    # Subtask 1: Move the Robot towards the Tank
    tank_88 = registry(env,"tank-88")
    MoveBot(env, robot, tank_88, camera)
    donothing(env)

