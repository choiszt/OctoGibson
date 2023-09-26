def act(robot,env,camera):
    # Subtask 3: Put the plate into the machine
    plate_170 = registry(env,"plate_170")
    machine_172 = registry(env,"machine_172")
    unfold(robot, plate_170, machine_172)
    donothing(env)

