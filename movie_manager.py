class Actor:
    def __init__(self, actor_name):
        self.name = actor_name
    
    def get_name(self):
        return self.name

# if __name__ == "__main__":
#     actor_1 = Actor("André")
#     actor_2 = Actor("Sabino")
#     print(actor_1.get_name())
#     print(actor_2.get_name())