def act( robot, env, camera):
        # Subsheet:1: Grasp leafplant
        leafplant(env.0.0)
        EasyGrasp(robot, leafplant)
            donothing()

