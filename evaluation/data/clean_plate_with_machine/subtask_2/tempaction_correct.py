

def act(robot, env, camera):
    machine_172 = registry(env, 'machine_172')
    MoveBot(env, robot, machine_172, camera)
    donothing(env)
