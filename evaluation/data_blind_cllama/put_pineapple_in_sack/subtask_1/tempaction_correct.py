

def act(robot, env, camera):
    grocery_shelf_prtqlw_2 = registry(env, 'grocery_shelf_prtqlw_2')
    MoveBot(env, robot, grocery_shelf_prtqlw_2, camera)
    donothing(env)
