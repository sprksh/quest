import uuid

from infrastructure import DocumentStore
from models import DocumentData


class DocumentService:
    def __init__(self):
        self.document_store = DocumentStore()

    def upload_document(self, document):
        doc_id = uuid.uuid4().hex
        self.document_store.upload(document, doc_id)
        self.save_document_data_to_db(doc_id, self.parse_document(document))
        return doc_id

    def parse_document(self, document):
        # can be made async
        # do ocr and get details
        document_data = {
            "invoice_id": 12345,
            "source": "Some Company",
            "billed_to": "Random Guy",
            "items": [
                {
                    "name": "Random Stuff 1",
                    "quantity": 3,
                    "price": 300
                },
                {
                    "name": "Random Stuff 2",
                    "quantity": 3,
                    "price": 300
                }
            ],
            "total_amount": 600,
            "payment": True
        }
        return document_data

    def save_document_data_to_db(self, doc_id, document_data):
        doc = DocumentData(doc_id, document_data=document_data, digitization_status=True)
        return doc.save()

    def get_document_data_by_id(self, doc_id):
        document_info = DocumentData.get_document_data(doc_id)
        if document_info["digitization_status"]:
            data = document_info["data"]
        else:
            data = "Not Yet Digitized"
        return data
    
    def get_digitization_status_by_id(self, doc_id):
        return DocumentData.get_document_data(doc_id)["digitization_status"]

    def set_digitization_status_by_id(self, doc_id, digitization_status):
        return DocumentData(doc_id, digitization_status=digitization_status).save()
