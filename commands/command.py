class Command:
    def __init__(self, name: str, description: str, func: callable):
        self.name = name
        self.description = description
        self.func = func

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    async def run(self, **kwargs):
        await self.func(**kwargs)
