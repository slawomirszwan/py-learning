sample_dict = {'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
sample_dict['first_name']

# x = sample_dict['alibaba']
# KeyError: 'alibaba'

x = sample_dict.get('alibaba', 'default')

print(x,sample_dict)