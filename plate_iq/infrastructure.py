

class DocumentStore:
    def __init__(self):
        self.connection = "s3_connection"

    def upload(self, document, doc_id):
        # location = self.connection.upload(document)
        return True

    def get_document_by_uuid(self, doc_id):
        # document = self.connection.get(doc_id)
        document = ""
        return document

