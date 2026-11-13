# Instead of calling the actual payment gateway, you create a fake object that behaves like the payment gateway.

# This is called mocking.

# Mocking is a testing technique in which we replace real dependencies with controlled simulated objects to isolate the component being tested.

from unittest.mock import Mock

payment_gateway = Mock()

payment_gateway.charge.return_value = "Payment Successful"

result = payment_gateway.charge(1000)

print(result)

