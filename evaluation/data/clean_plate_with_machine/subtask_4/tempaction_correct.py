

def act(robot, env, camera):
    plate_170 = registry(env, 'plate_170')
    machine_172 = registry(env, 'machine_172')
    unfold(robot, plate_170, machine_172)
    donothing(env)
