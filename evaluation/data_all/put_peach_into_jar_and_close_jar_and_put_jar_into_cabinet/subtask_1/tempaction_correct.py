

def act(robot, env, camera):
    peaches_173 = registry(env, 'peachys_173')
    MoveBot(env, robot, peaches_173, camera)
    donothing(env)
