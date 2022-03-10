class Gold:
    def melt(self):
        print("Gold will melt easily")
class Diamond(Gold):
    def melt(self):
        super().melt()
        print("Diamond will not melt")
things = Diamond()
things.melt()