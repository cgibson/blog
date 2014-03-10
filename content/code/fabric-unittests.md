Date: 2012-10-20 10:20
Title: Running Python Unit-Tests With Fabric
Tags: fabric, unit-tests
Slug: python_unit_tests_with_fabric
Author: Chris Gibson
Summary: I've been working on a small side project to make remote administration and deployment to servers easier for myself. Fabric is a great utility for connecting to remote servers, so my code is simply an extension of that library. Unfortunately, I've found unit testing fabric a little cumbersome....
Top_Title: The Hobbit: The Desolation of Smaug
Top_Desc: Bilbo's journey to the Lonely mountains in search of a new home, a panoply of riches, and of course a monstrous dragon!

I've been working on a small side project to make remote administration and deployment to servers easier for myself. [Fabric][fabric] is a great utility for connecting to remote servers, so my code is simply an extension of that library. Unfortunately, I've found unit testing fabric a little cumbersome.

Fabric runs in two environments: in [fabfiles] via the terminal, or in python using the [fabric api][api]. The latter requires the user to pass tasks into an <code>execute()</code> function, or to run the [execute function][execute_function] of a [fabric task][task]. None of these are ideal, as we don't want to run terminal commands in our test suite, and retrieving results from <code>execute()</code> calls for test verification feels contrived and hacky.

Luckily, there's an easy fix for this. Using the [functools] python module, we can build a decorator that will specifically call execute() whenever that decorated function is called. Here is the code:

	:::python
	def execute_wrap(f):
	    @wraps(f)
	    def wrapper(*args, **kwds):
	        return execute( f, *args, **kwds )
	    return wrapper

Simply use <code>@execute_wrap</code> decorators before every function, and you'll be set!


[fabric]: http://docs.fabfile.org/
[fabfiles]: http://docs.fabfile.org/en/1.4.0/usage/fabfiles.html
[api]: http://docs.fabfile.org/en/1.4.3/usage/execution.html?highlight=fabfile
[execute_function]: http://docs.fabfile.org/en/1.4.3/api/core/tasks.html?highlight=execute#fabric.tasks.execute
[task]: http://docs.fabfile.org/en/1.4.3/api/core/tasks.html?highlight=execute#tasks
[functools]: http://docs.python.org/library/functools.html
[code]: https://gist.github.com/3925499#file_fabric_wrapper_test.py
[code_vagrant]: https://gist.github.com/3925499#file_fabric_wrapper_test_vagrant.py
