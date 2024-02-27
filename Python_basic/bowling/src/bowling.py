class Bowling:
    def __init__(self, init_inf: str):
        self.data = list(init_inf.replace("-", "0"))
        self.data_upd = list(init_inf.replace("-", "0"))
        self.total = 0

    def run(self):
        self.play()
        return self.total

    def play(self):
        for numb, item in enumerate(self.data):
            if item == "X":
                self.total += 20
                self.data_upd.remove(item)
            elif item == "/" and numb > 0:
                self.total += 15
                self.data_upd.remove(self.data[numb - 1])
                self.data_upd.remove(item)
        for item in self.data_upd:
            try:
                self.total += int(item)
            except Exception as error:
                raise ValueError(f"Unpredictable symbol check string")


def get_score(game_result: str) -> int:
    bowling = Bowling(game_result)
    bowling.run()
    return bowling.total
