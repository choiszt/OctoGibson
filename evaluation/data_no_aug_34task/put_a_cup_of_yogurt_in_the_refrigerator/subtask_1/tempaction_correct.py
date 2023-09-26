

def act(robot, env, camera):
    bottom_grocery_shelf = registry(env, 'bottom_cycling_groove_86')
    MoveBot(env, robot, bottom_grocery_shelf, camera)
    donothing(env)
