BASE_FRAME_TYPE = ["┌", "─", "┐", "│", "", "│", "├", "─", "┤", "└", "─", "┘"]


class Frame:
    def __init__(self, length: int, height: int, insert: list = [], frame: list = BASE_FRAME_TYPE):
        self.length = length
        self.height = height
        self.__frame = frame
        self.insert = insert
        self.out = []

    def create(self):
        self.out = []

        for line in range(self.height + 2):
            out = ""

            if line == 0:
                out += f"{self.__frame[0]}{self.__frame[1] * (self.length - 2)}{self.__frame[2]}"

            elif line == self.height + 1:
                out += f"{self.__frame[9]}{self.__frame[10] * (self.length - 2)}{self.__frame[11]}"

            else:
                if len(self.insert) >= line:
                    if self.insert[line - 1] == "&empty&":
                        out += f"{self.__frame[3]}{' ' * (self.length - 2)}{self.__frame[5]}"

                    elif self.insert[line - 1] == "&line&":
                        out += f"{self.__frame[6]}{self.__frame[7] * (self.length - 2)}{self.__frame[8]}"

                    else:
                        out += f"{self.__frame[3]}{self.insert[line - 1].ljust(self.length - 2)}{self.__frame[5]}"

                else:
                    out += f"{self.__frame[3]}{''.ljust(self.length - 2)}{self.__frame[5]}"

            self.out.append(out)

    def get(self):
        return self.out

    def get_line(self, line):
        return list(self.out[line])


if __name__ == "__main__":
    frame = Frame(30, 10, ["1", "2", "3"])
    frame.create()
    for element in frame.get():
        print(element)
