from config_eest import FORKS, config_eest
from config_eest.example_constants.hello import some_dict, some_int, some_list, some_truth

# ------------- fork example ------------------
frontier_gas_limit = config_eest.get(FORKS.FRONTIER.GAS_LIMIT)
homestead_gas_limit = config_eest.get(FORKS.HOMESTEAD.GAS_LIMIT)
inherited_value_example = config_eest.get(FORKS.HOMESTEAD.VALUE_THAT_NEVER_CHANGED_AFTER_FRONTIER)

print(f"Frontier Gas Limit: {frontier_gas_limit}\nHomestead Gas Limit: {homestead_gas_limit}")
print(inherited_value_example)

# ----------- retrieving constants example -------------
print(some_int, some_truth, some_list, some_dict)
