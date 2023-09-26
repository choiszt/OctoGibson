

def act(robot, env, camera):
    plastic_bowl_275 = registry(env, 'plastic_bowlish_275')
    EasyGrasp(robot, plastic_bowl_275, plastic_bowl_275)
    donothing(env)
