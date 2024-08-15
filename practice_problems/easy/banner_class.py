#rework so that too long of lengths or too short of lengths are accounted for

class Banner:
    def __init__(self, message, width=False):
        self.message = message
        self.length = width
        if not width:
            self.length = len(message.strip())

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {self.length * ' '} |"

    def _horizontal_rule(self):
        return f"+-{self.length * '-'}-+"

    def _message_line(self):
        return f"| {self.message.center(self.length)} |"



# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
banner2 = Banner('To boldly go where no one has gone before.', 80)
print(banner2)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
