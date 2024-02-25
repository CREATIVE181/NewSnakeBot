from aiogram.filters import Filter
from aiogram.types import Message
    


class OnlyCommand(Filter):
    _default_params = ('tex_only_cmd', 'only_cmd')

    def __init__(self, only_cmd):
        self.only_cmd = [only_cmd] if type(only_cmd) is str else only_cmd 

    async def __call__(self, message: Message):
        commands = self.only_cmd
        if message.text is None:
            return
        text_cmd = message.text.split("\n", maxsplit=1)[0].lower().strip()
        if text_cmd in commands:
            return True
        result = [
            " ".join(text_cmd.split(" ")[: len(cmd.split(" "))]) == cmd
            for cmd in commands
        ]
        return True in result