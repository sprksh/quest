from flask import Flask
from flask import request

from services import DocumentService

app = Flask(__name__)


"""
API endpoints for the end customer
    - To allow a customer to provide a PDF document (invoice) to process
    - To allow a customer to track a document’s digitization status
    - To allow a customer to retrieve the structured invoice information for a specified
      document, if the document status is digitized (simply return mock data in this case)

API endpoints for internal users / other microservices
    - To allow a staff member (or another microservice) to manually add digitized / parsed
      (structured) information for a specific document
    - For example, if a staff member views the document and wishes to record in the
      Structured data tables that the Invoice Number is INV1234, they should be able
      to do so
    - It should be possible to add/update more than one field at a time, if the caller
      chooses to do so
    - It should not be mandatory to update all fields/information in the same call; it
      should be possible to independently and partially add/update each piece of
      information
    - To allow marking a document as “digitized”
"""


@app.route('/')
def ping():
    return {"message": 'Pong!'}


@app.route('/documents/', methods=["GET", "POST"])
def document_upload():
    if request.method == "POST":
        # file = request.file
        file = "document"
        document_id = DocumentService().upload_document(file)
        return {"message": "Success", "document_id": document_id}


@app.route('/documents/<string:doc_id>/status', methods=["GET", "POST"])
def document_digitization_status(doc_id):
    if request.method == "GET":
        status = DocumentService().get_digitization_status_by_id(doc_id)
        return {"status": status}
    if request.method == "POST":
        digitization_status = request.json["digitization_status"]
        updated = DocumentService().set_digitization_status_by_id(doc_id, digitization_status)
        return {"message": "Success" if updated else "Failed"}


@app.route('/documents/<string:doc_id>/data', methods=["GET", "POST"])
def document_data(doc_id):
    if request.method == "GET":
        doc_data = DocumentService().get_document_data_by_id(doc_id)
        return {"data": doc_data}
    if request.method == "POST":
        data = request.json
        updated = DocumentService().save_document_data_to_db(doc_id, data)
        return {"message": "Success" if updated else "Failed"}
