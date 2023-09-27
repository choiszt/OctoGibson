def act(bot,envi,cam):
        # Register straw before moving bot to it
        straw = registry(envi,"staw-277")
        MoveBot (env, bot, straw, cam)
        donothing (env)

