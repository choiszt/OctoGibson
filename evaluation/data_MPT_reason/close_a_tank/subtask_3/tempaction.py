def act(robot,environmeont,camera)
    # Subtask 1: Move the Robot towards the Tank
    tank_82 = registry(env,"tank-82")
    MoveBot(env, robot, tank_82, camera)

