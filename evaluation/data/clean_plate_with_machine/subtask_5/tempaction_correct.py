

def act(robot, env, camera):
    plate_170 = registry(env, 'plate_170')
    unfold(robot, plate_170)
    donothing(env)
