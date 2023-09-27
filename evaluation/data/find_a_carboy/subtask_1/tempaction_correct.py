

def act(robot, env, camera):
    reagent = registry(env, 'reagent-bottles_189')
    MoveBot(env, robot, reagent, camera)
