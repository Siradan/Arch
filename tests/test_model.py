from unittest import TestCase

from generator import generator, generate

from model import Model
from serializers.serializers import JsonSerialize
from serializers.serializers import PickleSerialize
from serializers.serializers import YamlSerialize


@generator
class TestModel(TestCase):
    model = Model('JsonSerialize')

    @generate(
        'JsonSerialize', 'YamlSerialize', 'PickleSerialize'
    )
    def test_set_serializer(self, inp):
        Model(inp)

    @generate(
        [1, 'name1', '1']
    )
    def test_add_item(self, inp):
        self.assertEqual(
            inp[0],
            self.model.add_item([{'name':inp[1], 'val':inp[2]}])
        )

    @generate(
        [{'name': 'name1', 'val': 'val1'}]
    )
    def test_return_db(self, inp):
        self.assertListEqual(
            inp,
            self.model.return_db()
        )

    @generate(
        [{'name': 'name1', 'val': '1'}]
    )
    def test_load(self, inp):
        self.model.clear()
        self.model.add_item(inp)
        self.model.save('testing')
        self.model.load('testing')
        self.assertListEqual(
            inp,
            self.model.return_db())

    @generate(
        30
    )
    def test_calc(self, inp):
        self.model.clear()
        self.model.add_item([{'name': 'name1', 'val': '1'}])
        self.assertListEqual(
            inp,
            self.model.count([{'name': 'name1', 'val': '30'}]))
