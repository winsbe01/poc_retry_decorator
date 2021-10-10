## Proof of Concept -- Retry Decorators

This is an example of a decorator that will retry a method a definable number 
of times if an exception is raised. Additionally, it takes in a `callback` 
parameter, which is a method that gets called in the case of an exception, 
before retrying the original method.

Things to note:
 - This is written specifically to work on class methods, as it's assuming a 
   first argument of `self`. It could trivially be rewritten to work for plain 
   functions, though I haven't tried getting it to work for both.
 - As written, the `callback` *cannot* take any defined parameters (besides `self`).
   The best we could do in this scenario would be to pass in all the arguments 
   that were passed to the original method. This may be less of an issue with 
   methods, as the callback method would at least have a reference to whatever 
   state `self` has.
 - Since the decorator itself takes in parameters, it must be followed by parens 
   (when called), even if it's no changing any of the defaults. I haven't yet 
   figured out how to stop this, as a decorator without parameters *should* just 
   be the decorator word, no parens. Most decorators work like this -- I'll 
   have to investigate.
