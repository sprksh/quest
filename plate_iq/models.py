from extensions import db


class DocumentData:
    key = "document_data"

    def __init__(self, doc_id, document_data=None, digitization_status=False):
        self.doc_id = doc_id
        self.document_data = document_data
        self.digitization_status = digitization_status

    def save(self):
        if self.document_data:
            data = db[self.key][self.doc_id]["data"]
            data.update(self.document_data)
        if self.digitization_status is not None:
            db[self.key][self.doc_id]["digitization_status"] = self.digitization_status
        return True

    @staticmethod
    def get_document_data_object(doc_id):
        return DocumentData(doc_id, db[DocumentData.key].get(doc_id))

    @staticmethod
    def get_document_data(doc_id):
        data = db[DocumentData.key].get(doc_id)
        return data if data else None
