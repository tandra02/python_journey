from abc import ABC, abstractmethod


class Storage:
    @abstractmethod
    def save(self):
        pass

class LocalStorage(Storage):
	def save(self, key, value):
		print("Saved, " + key + ":" + value)


class App:
	def __init__(self, storage):
		self.storage = storage

	def start(self, key, value):
		storage.save(key, value)


if __name__ == "__main__":
	storage = LocalStorage()
	app = App(storage)
	key = input()
	value = input()
	app.start(key, value)
