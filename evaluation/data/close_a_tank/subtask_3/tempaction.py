def act(robot,env,camera):
    # Subtask 1: Move the robot to the tank
    tank_88 = registry(env,"tank_88")
    MoveBot(env, robot, tank_88, camera)
    donothing(env)

