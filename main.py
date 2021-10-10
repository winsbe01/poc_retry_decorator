import random
from decorators import method_decor


class ExampleClass:

	def __init__(self):
		self.state = "initialized"

	def this_is_a_callback(self):
		self.state = "calling-back"

	@method_decor()
	def random_exception(self):
		print(f"in random_exception: {self.state}")
		denom = random.randint(0,1)
		1 / denom

	@method_decor(callback=this_is_a_callback)
	def always_exception(self):
		print(f"in always_exception: {self.state}")
		raise Exception


def main():
	obj = ExampleClass()

	try:
		obj.random_exception()
		print("random exception succeeded!")
	except Exception:
		print("randomly excepted too many times")

	try:
		obj.always_exception()
		print("we should never reach this")
	except Exception:
		print("we should have retried the number of times defined in the callback")


if __name__ == "__main__":
	main()
