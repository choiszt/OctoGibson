def act(robot,env,camera):
    # Subtask 1: Move to The Straw
    straw_171 = registry(env,"staw_171")
    MoveBot(env, robot, straw_191, camera)
    donothing(env)

