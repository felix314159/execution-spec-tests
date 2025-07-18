from pydantic import BaseModel


class FrontierConfig(BaseModel):
    gas_limit: int = 100
    value_that_never_changed_after_frontier: int = 2
