from dataclasses import dataclass

from pyspark.sql import types as t
from schema import generate_schema


def test_string_field():
    @dataclass
    class DataSchema:
        string_field: str

    expected = t.StructType().add('string_field', t.StringType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_bool_field():
    @dataclass
    class DataSchema:
        boolean_field: bool

    expected = t.StructType().add('boolean_field', t.BooleanType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_datetime_field():
    import datetime

    @dataclass
    class DataSchema:
        timestamp_field: datetime.datetime

    expected = t.StructType().add('timestamp_field', t.TimestampType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_date_field():
    import datetime

    @dataclass
    class DataSchema:
        date_field: datetime.date

    expected = t.StructType().add('date_field', t.DateType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_decimal_field():
    import decimal

    @dataclass
    class DataSchema:
        decimal_field: decimal.Decimal

    expected = t.StructType().add('decimal_field', t.DecimalType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_float_field():
    @dataclass
    class DataSchema:
        float_field: float

    expected = t.StructType().add('float_field', t.FloatType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_integer_field():
    @dataclass
    class DataSchema:
        integer_field: int

    expected = t.StructType().add('integer_field', t.IntegerType())
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_list_of_strings_field():
    from typing import List

    @dataclass
    class DataSchema:
        list_of_strings_field: List[str]

    expected = t.StructType().add('list_of_strings_field', t.ArrayType(t.StringType()))
    actual = generate_schema(DataSchema)

    assert actual == expected


def test_list_of_integers_field():
    from typing import List

    @dataclass
    class DataSchema:
        list_of_integers_field: List[int]

    expected = t.StructType().add('list_of_integers_field', t.ArrayType(t.IntegerType()))
    actual = generate_schema(DataSchema)

    assert actual == expected
