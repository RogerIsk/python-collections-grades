# Task - Access nested keys
# Accessing a value in a nested dictionary can lead to difficult to read syntax like: `data['really']['deeply']['nested']['value']`.
# Implement a method `get` that takes a dictionary and a nested key name with levels seperated by `.` 
# (`really.deeply.nested.value` in the example) and returns the value if it exists and `None` if it doesn't.

data = {
  'students': [
    {
      'name': 'Josephine',
      'subjects': [
        {
          'name': 'English',
          'teacher': 'Mr. Hoover'
        }
      ]
    },
    {
      'name': 'Luke',
      'subjects': [
        {
          'name': 'History',
          'teacher': 'Mrs. Peters'
        }
      ]
    },
    {
      'name': 'Julia',
      'subjects': [
        {
          'name': 'Chemistry',
          'teacher': 'Mrs. Fauci'
        }
      ]
    }
  ]
}

# found this in the internet, it works, but I don't understand it completely
def get(dictionary, key):
    keys = key.split('.')
    value = dictionary
    for k in keys:
        if isinstance(value, list):
            try:
                k = int(k)
            except ValueError:
                return None
        try:
            value = value[k]
        except (KeyError, IndexError):
            return None
    return value

print(get(data, 'students.1.subjects.0.name'))
print(get(data, 'students.0.subjects.0.teacher'))