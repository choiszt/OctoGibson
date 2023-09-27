def act(robot,env,camera):
    # Subtask 1: Move the robot to the modem
    modem_279 = registry(env,"modem_279")
    MoveBot(env, robot, modem_279, camera)
    donothing(env)

