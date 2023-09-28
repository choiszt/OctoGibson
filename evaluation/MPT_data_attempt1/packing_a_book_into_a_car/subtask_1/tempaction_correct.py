

def act(robot, env, camera):
    case = registry(env, 'case_188')
    MoveBot(env, 'robot', case, camera)
    donothing(env)
