from functools import wraps


# I didn't come up with this pattern, I flagrantly stole it from:
#   https://www.pythonprogramming.in/wrap-decorators-in-python.html
# and then adopted it to work with a Class
def method_decor(loop=3, callback=None):

	def inner(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			self = args[0]  # this decorator is for a class method
			count = 0
			while True:
				print(f" > calling {func.__name__}, {count+1} of {loop}")
				try:
					return func(*args, **kwargs)
				except Exception:
					if callback is not None:
						callback(self)
					count += 1
					if count == loop:
						raise e
		return wrapper
	return inner
