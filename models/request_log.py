from tortoise.models import Model
from tortoise import fields


class RequestLog(Model):
    id = fields.IntField(pk=True)
    operation = fields.CharField(max_length=50)
    input_data = fields.TextField()
    result = fields.IntField()
    timestamp = fields.DatetimeField(auto_now_add=True)
