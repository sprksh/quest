from infrastructure import DocumentStore


class NestedDict(dict):

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    def setup(self):
        # can be used to create pre defined keys for each table and then freeze it for
        # addition of new tables
        return self


# singleton objects
db = NestedDict().setup()
document_store = DocumentStore()
