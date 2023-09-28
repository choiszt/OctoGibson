def act(robot,env,camera):
    # Subtask 1: Move the bot to the cabinets
    cabinet = registry(env, "cabnet_dszchb_0")
    MoveBot(env, robot, cabinet, camera)
    donothing(env)

