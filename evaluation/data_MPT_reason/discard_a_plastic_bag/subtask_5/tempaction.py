def act(potbot, envi, cam):
    # Subtask 1: Move robot To Straw
    straw_277, straw_278 = register(envir,"straw-277",
                                    "stow-278")
    MoveBot(env, potbot, straw277, camera)
    donothing(env)

