from unittest.mock import patch

class Duck:
    def walk(self):
        return("Spectator: Look, a walking duck")

    def fly(self):
        return("Spectator: Look a flying duck")

duck1 = Duck()
duck2 = Duck()

# with patch.object(duck1, "fly") as mock:
#     mock.return_value = "Spectator: Modified, a flying pig"
#     print(duck1.walk())
#     print(duck1.fly())
#     print(duck2.walk())
#     print(duck2.fly())

# with patch.object(duck1, "fly", lambda: "Modified, lookk a flying duckling") as mock:
#     # mock.return_value = "Spectator: Modified, a flying pig"
#     print(duck1.walk())
#     print(duck1.fly())
#     print(duck2.walk())
#     print(duck2.fly())


data = {
    "key1": "value1",
    "key2": "value2",
}

print(data)
with patch.dict(data, {
    "key2": "patched_value2",
    "key3": "patched_value3"
}):
    print(data)
print(data)

