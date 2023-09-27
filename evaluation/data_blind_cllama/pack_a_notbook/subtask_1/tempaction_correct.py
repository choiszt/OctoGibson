

def act(robot, env, camera):
    grocery_shelf = registry(env, 'grocery_shelf_prtqlw_1')
    MoveBot(env, robot, grocery_shelf, camera)
    donothing(env)
