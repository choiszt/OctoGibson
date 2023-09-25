

def act(robot, env, camera):
    add_operational_function = registry(env, 'add_opener_function')
    MoveBot(env, 'bot', add_operational_function, camera)
    donothing(env)
