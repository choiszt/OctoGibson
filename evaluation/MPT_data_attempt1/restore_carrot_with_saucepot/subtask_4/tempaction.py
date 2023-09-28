def act(robot, env, camera):
        # Subtopask 1: Register and Move the Robot to the Carrot in the Fridge
        carrot = registry (env, 'carrot')
        MoveBot ( env, robot, carrot, camera)
        donothing (env)

