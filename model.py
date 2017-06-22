from serializers.serializers import Serialize


class Model:
    """
    Model part of MVC
    """

    def __init__(self, serializer):
        """
        Constructor for Model class
        """
        self._serializer = Serialize(serializer)

    def return_db(self, filename):
        """
        Return database
        """
        return self._serializer.load(filename)

    def count(self, list, filename):
        """
        Calculates calories and return number of it
        """
        res = 0
        file = self._serializer.load(filename)
        for element in list:
            b = [d for d in file if d['name'] == element['name']]
            if not b:
                return element['name']
            res += int(b[0]['val']) * int(element['val'])
        return res

    def add_item(self, val, filename):
        """
        try to write new item into database
        """
        try:
            b = self._serializer.load(filename)
            if [d for d in b if d['name'] == val[0]]:
                b.remove([d for d in b if d['name'] == val[0]][0])
            b.append({'name': val[0], 'val': val[1]})
        except EOFError:
            b = [{'name': val[0], 'val': val[1]}]
        self._serializer.save(filename, b)
