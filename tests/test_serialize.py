import json
from unittest import TestCase

import yaml
from generator import generator, generate
from serializers.serializers import JsonSerialize
from serializers.serializers import PickleSerialize
from serializers.serializers import Serialize
from serializers.serializers import YamlSerialize

from serializers.serializersstreams import serializeToJsonStream
from serializers.serializersstreams import serializeToYamlStream


@generator
class TestPickleSerialize(TestCase):
    @generate(
        [[], 'test/empty']
    )
    def test_load(self, inp):
        self.assertListEqual(PickleSerialize.load(inp[1]), inp[0])

    @generate(
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load']
    )
    def test_save(self, inp):
        PickleSerialize.save(inp[1], inp[0])
        self.assertListEqual(PickleSerialize.load(inp[1]), inp[0])


@generator
class TestJsonSerialize(TestCase):
    @generate(
        [[], 'test/empty'],
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load']
    )
    def test_load(self, inp):
        self.assertListEqual(JsonSerialize.load(inp[1]), inp[0])

    @generate(
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load']
    )
    def test_save(self, inp):
        JsonSerialize.save(inp[1], inp[0])
        stream = serializeToJsonStream(inp[0])
        self.assertListEqual(json.load(stream), inp[0])


@generator
class TestYamlSerialize(TestCase):
    @generate(
        [[], 'test/empty'],
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load']
    )
    def test_load(self, inp):
        self.assertListEqual(YamlSerialize.load(inp[1]), inp[0])

    @generate(
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load']
    )
    def test_save(self, inp):
        YamlSerialize.save(inp[1], inp[0])
        stream = serializeToYamlStream(inp[0])
        self.assertListEqual(yaml.load(stream.getvalue()), inp[0])


@generator
class TestSerialize(TestCase):
    @generate(
        'unexpected-serialize-class-name'
    )
    def test__init_(self, inp):
        with self.assertRaises(KeyError):
            Serialize(inp[1])

    @generate(
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load', 'YamlSerialize']
    )
    def test_save(self, inp):
        serialize = Serialize(inp[2])
        serialize.save(inp[1], inp[0])
        self.assertListEqual(YamlSerialize.load(inp[1]), inp[0])

    @generate(
        [[{'name': 'name-1', 'val': 'val-1'}],
         'test/load', 'YamlSerialize'],
        [[], 'test/empty', 'YamlSerialize']
    )
    def test_load(self, inp):
        self.assertListEqual(Serialize(inp[2]).load(inp[1]), inp[0])
