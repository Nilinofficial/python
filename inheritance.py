class member:
    @staticmethod
    def read():
        print("Read Access")


class developer(member):
    def write(self):
        print("Write Access")


dev = developer()

dev.read()
dev.write()