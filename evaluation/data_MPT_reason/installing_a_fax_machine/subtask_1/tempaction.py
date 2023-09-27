def act(robot,env,camera):
    # Subtask 1: Move the Robot to the Floor where the Fax Engine is Located
    floor = registry(env, "floor")
    MoveBot(environment, robot, floor, camera)
    donothing(env)

