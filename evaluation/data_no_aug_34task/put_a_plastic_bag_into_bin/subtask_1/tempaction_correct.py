

def act(robot, env, camera):
    plastic_baskets_277 = registry(env, 'plastic_basket_277')
    MoveBot(env, robot, plastic_baskets_277, camera)
    donothing(env)
