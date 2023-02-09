from dataclasses import fields
from datetime import date, datetime
from decimal import Decimal
from typing import List

from pyspark.sql import types as t


def generate_schema(obj) -> t.StructType:
    schema = t.StructType()
    for field in fields(obj):
        schema.add(field.name, convert_type(field.type))
    return schema


def convert_type(typeclass) -> t.DataType:
    if typeclass is bool:
        return t.BooleanType()
    if typeclass is datetime:
        return t.TimestampType()
    if typeclass is date:
        return t.DateType()
    if typeclass is Decimal:
        return t.DecimalType()
    if typeclass is float:
        return t.FloatType()
    if typeclass is int:
        return t.IntegerType()
    if typeclass is List[str]:
        return t.ArrayType(t.StringType())
    if typeclass is List[int]:
        return t.ArrayType(t.IntegerType())
    if typeclass is str:
        return t.StringType()
