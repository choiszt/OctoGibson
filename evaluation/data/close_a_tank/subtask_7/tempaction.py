def act(robot,env,camera):
    # Subtask 2: Close the tank
    tank_88 = registry(env,"tank_88")
    close(robot, tank_88)
    donothing(env)

