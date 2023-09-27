

def act(robot, env, camera):
    chocolates = registry(env, 'chocolates_177')
    MoveBot(env, robot, chocolates, camera)
    donothing(env)
