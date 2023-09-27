

def act(robot, env, camera):
    pizzabox_85 = registry(env, 'pizza-bbox-85')
    EasyGrasp(robot, pizzabox_85)
    donothing(env)
