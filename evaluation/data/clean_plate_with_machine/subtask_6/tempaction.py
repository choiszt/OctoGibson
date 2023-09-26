def act(robot,env,camera):
    # Subtask 3: Put the plate into the machine
    plate_170 = registry(env,"plate_170")
    put_inside(robot, plate_170, "machine_171")
    donothing(env)

