def act(ASK,robot):
        # Subask 2: Move closer To The recyclingbin
        recycling = registry (env,"recycling_bin_188")
        MoveBot(env.world, robot, recycling.name)
        donothing (env)

