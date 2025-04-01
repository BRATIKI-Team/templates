from pydantic_ai import Agent, RunContext
from app.core import config

class RouletteAgent:
    def __init__(self):
        self._agent = Agent(
            config.OPENAI.MODEL_NAME,
            deps_type=int,
            result_type=bool,
            system_prompt=(
                'Use the `roulette_wheel` function to see if the '
                'customer has won based on the number they provide.'
            ),
            tools=[self._roulette_wheel]
        )


    async def run(self, deps: int) -> bool:
        return await self._agent.run("Put 10$ on square 12", deps=deps)

    
    @staticmethod
    async def _roulette_wheel(ctx: RunContext[int], square: int) -> str:
        """check if the square is a winner"""
        print("check if the square is a winner", square)
        return "winner" if square == ctx.deps else "loser"


    