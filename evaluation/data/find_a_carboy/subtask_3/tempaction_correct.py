

def act(robot, env, camera):
    reagentbottle = registry(env, 'reagentbottles_189')
    MoveBot(reagentbottle, reagentbottle, camera)
    donothing(env)
