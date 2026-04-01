# import irsim

# env = irsim.make('ir-sim/usage/17gui_world/gui.yaml') # initialize the environment with the configuration file

# for i in range(300): # run the simulation for 300 steps

#     env.step()  # update the environment
#     env.render() # render the environment

#     if env.done(): break # check if the simulation is done

# env.end() # close the environment


def add_two_numbers(a, b):
    return a + b


var_a = 5
var_b = 10

result = add_two_numbers(var_a, var_b)
print(f"The result of adding {var_a} and {var_b} is: {result}")
