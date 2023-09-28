def act(robot,env,camera):
    # Subtask 1: Move the Robot to the Carrot
    carrot = registry(env, "carrot", "151")
    MoveBot(env, robot, carrot, camera)
    donothing(env)

