## Tools

This folder contains a variety of tools that can be used to better grade a student. 

#### Useful Tools:

1. <b>Timeout decorator</b> <i> limited to use on MacOS exclusively </i>

	- Decorate any of the test functions with it to enforce a timeout

Example without arguments: 

	@timeout()
    def test_greet(self):
        self.assertEqual(greet("Saad"), "Hello, Saad!", "Testing Greet")
	

Example with arguments:
	
	@timeout(seconds=10, error_message=os.strerror(errno.ETIME))
    def test_greet(self):
        self.assertEqual(greet("Saad"), "Hello, Saad!", "Testing Greet")
