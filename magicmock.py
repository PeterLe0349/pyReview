from unittest.mock import Mock, MagicMock

# m = MagicMock()

# m+1
# print(m+1)

m = Mock()
m(1)
m(2,3)
m(2,3,4)

m.assert_called_with(2,3,  4)
m.assert_any_call(1)
print(m.call_args_list)