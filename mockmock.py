from unittest.mock import Mock

# sample_mock = Mock(a=1, b=2)

# sample_mock = Mock(side_effect=range(3))

# sample_mock = Mock(side_effect=ValueError)

# sample_mock = Mock(side_effect=[1,3,'almost there', ValueError])

# same_mock = Mock(side_effect=print)

# print(sample_mock())
# print(sample_mock())
# print(sample_mock())
# print(sample_mock())

# same_mock(1)

# efffect with function
def the_fake_function(a):
    return a*5

sample_mock = Mock(side_effect=the_fake_function)
print(sample_mock(3))