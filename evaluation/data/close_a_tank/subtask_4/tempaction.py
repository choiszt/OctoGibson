def act(rotbot, env, camera):
  # Subask 2: Grasp THE Fuel Tan
  fuel_taker_188 = registry (env,"fuel_tan_188")
  EasyGrasp (robot,"fuel-taker-188") 
  donothing(env)


