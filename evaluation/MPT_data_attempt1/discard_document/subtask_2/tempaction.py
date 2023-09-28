def act(task,robot):
        # SubTask 2: Move the Robot To the Cutting Recyclage bin
        cutting_recycling_bin = registry (env, 'cutting_repcycling-bin_188')
        MoveBot(env.env, robot, cutting_recycle_bin, camera)
        donothing (env)

