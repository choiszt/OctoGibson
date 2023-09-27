

def act(robot, env, camera):
    (stove_188, staw191) = registry(env, 'stow_188')
    EasyGrasp(camera, robot)
    donothing()
