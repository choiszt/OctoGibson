

def act(robot, env, camera):
    canofdogfood143 = registry(env, 'canofdogfood_103')
    MoveBot(env, robot, canofdogfood143, camera)
    liushuai = registry(env, 'choiszt103')
    donothing(env)
    MoveBot(env, robot, liushuai, camera)
