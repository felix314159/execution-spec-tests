from config import FORKS, config

frontier_gas_limit = config.get(FORKS.FRONTIER.GAS_LIMIT)
homestead_gas_limit = config.get(FORKS.HOMESTEAD.GAS_LIMIT)
inherited_value_example = config.get(FORKS.HOMESTEAD.VALUE_THAT_NEVER_CHANGED_AFTER_FRONTIER)

print(f"Frontier Gas Limit: {frontier_gas_limit}\nHomestead Gas Limit: {homestead_gas_limit}")
print(inherited_value_example)
