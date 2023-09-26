def act(robot,env,camera):
    # Subtask 2: Move to the machine
    machine_172 = registry(env,"machine_172")
    MoveBot(env, robot, machine_172, camera)
    donothing(env)

