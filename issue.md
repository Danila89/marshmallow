### [version 2.20.0] TypeError: 'NoneType' object is not subscriptable
After update from version 2.19.5 to 2.20.0 I got error for code like:

```python
from marshmallow import Schema, fields, validates


class Bar(Schema):
    value = fields.String()

    @validates('value')  # <- issue here
    def validate_value(self, value):
        pass


class Foo(Schema):
    bar = fields.Nested(Bar)


sch = Foo()

sch.validate({
    'bar': 'invalid',
})
```

```
Traceback (most recent call last):
  File "/_/bug_mschema.py", line 19, in <module>
    'bar': 'invalid',
  File "/_/env/lib/python3.7/site-packages/marshmallow/schema.py", line 628, in validate
    _, errors = self._do_load(data, many, partial=partial, postprocess=False)
  File "/_/env/lib/python3.7/site-packages/marshmallow/schema.py", line 670, in _do_load
    index_errors=self.opts.index_errors,
  File "/_/env/lib/python3.7/site-packages/marshmallow/marshalling.py", line 292, in deserialize
    index=(index if index_errors else None)
  File "/_/env/lib/python3.7/site-packages/marshmallow/marshalling.py", line 65, in call_and_store
    value = getter_func(data)
  File "/_/env/lib/python3.7/site-packages/marshmallow/marshalling.py", line 285, in <lambda>
    data
  File "/_/env/lib/python3.7/site-packages/marshmallow/fields.py", line 265, in deserialize
    output = self._deserialize(value, attr, data)
  File "/_/env/lib/python3.7/site-packages/marshmallow/fields.py", line 465, in _deserialize
    data, errors = self.schema.load(value)
  File "/_/env/lib/python3.7/site-packages/marshmallow/schema.py", line 588, in load
    result, errors = self._do_load(data, many, partial=partial, postprocess=True)
  File "/_/env/lib/python3.7/site-packages/marshmallow/schema.py", line 674, in _do_load
    self._invoke_field_validators(unmarshal, data=result, many=many)
  File "/_/env/lib/python3.7/site-packages/marshmallow/schema.py", line 894, in _invoke_field_validators
    value = data[field_obj.attribute or field_name]
TypeError: 'NoneType' object is not subscriptable
```