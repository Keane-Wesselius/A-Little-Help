import google.auth
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Doc_Creator:

    def __init__(self) -> None:
        #API_Key to be able to use googles services
        API_KEY = "/home/pi/Python/A-Little-Help/google/gDrive.json"

        # Get the Scopes (permissions) to be able to create each type of document and interact with google drive
        DOCS_SCOPE = "https://www.googleapis.com/auth/documents"
        SLIDES_SCOPE = "https://www.googleapis.com/auth/presentations"
        DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"
        SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"

        #create the credentials to use the service
        creds = Credentials.from_service_account_file(
            API_KEY,
            scopes=[DOCS_SCOPE, SLIDES_SCOPE, DRIVE_SCOPE, SHEETS_SCOPE]
        )

        #Sets the version of the api service we are using and gets the actual services so we can use them
        try:
            self.drive_service = build("drive", "v3", credentials=creds)
            self.docs_service = build("docs", "v1", credentials=creds)
            self.slides_service = build("slides", "v1", credentials=creds)
            self.sheets_service = build("sheets", "v4", credentials=creds)
        except Exception as e:
            print(e)



    # Create a new Google Docs document
    def createDoc(self, doc_title=None):
        if doc_title == None:
            doc_title = "A Little Help"
        try:
            doc = self.docs_service.documents().create(body={"title": doc_title}).execute()
            if doc:
                doc_id = doc["documentId"]
                permission = {"type": "anyone", "role": "writer", "withLink": True}
                self.drive_service.permissions().create(fileId=doc_id, body=permission).execute()
                file_url = f"Document URL: https://docs.google.com/document/d/{doc_id}"
                return file_url
            else:
                raise HttpError
        except Exception:
            return "Error: File Creation Unsuccesful, Try Again"

        

    def createSlide(self, slide_title=None):
        if slide_title == None:
            slide_title = "A Little Help"
        try:
            slide = self.slides_service.presentations().create(body={"title": slide_title}).execute()
            if slide:
                slide_id = slide["presentationId"]
                permission = {"type": "anyone", "role": "writer", "withLink": True}
                self.drive_service.permissions().create(fileId=slide_id, body=permission).execute()
                file_url = f"Presentation URL: https://docs.google.com/presentation/d/{slide_id}"
                return file_url
            else:
                raise HttpError
        except Exception:
            return "Error: File Creation Unsuccesful, Try Again"


    def createSheet(self, sheet_title=None):
        if sheet_title == None:
            sheet_title = "A Little Help"
        try:
            sheet = self.sheets_service.spreadsheets().create(body={"properties": {"title": sheet_title}}).execute()
            if sheet:
                sheet_id = sheet["spreadsheetId"]
                permission = {"type": "anyone", "role": "writer", "withLink": True}
                self.drive_service.permissions().create(fileId=sheet_id, body=permission).execute()
                file_url = f"Spreadsheet URL: https://docs.google.com/spreadsheets/d/{sheet_id}"
                return file_url
            else:
                raise HttpError
        except Exception:
            return "Error: File Creation Unsuccesful, Try Again"
        

    def getDoc(self, doc_title=None):
        if doc_title == None:
            return "You need to specify a document title"
        try:
            results = self.drive_service.files().list(q = f"name = '{doc_title}'", fields='webViewLink').execute()
            files = results.get("files", [])
        except Exception as e:
            return f"Error finding your file: {e}"
        
        if not files:
            return "File does not exist"
        else:
            for file in files:
                return f"Found your file! {file.get('name')}\n {file}"
    
