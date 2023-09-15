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
    def createDoc(self, folder_name, doc_title=None):
        try:
            folder_id = self.getOrCreateFolder(folder_name)

            document_metadata = {
                'name': doc_title,
                'mimeType': 'application/vnd.google-apps.document',
                'parents': [folder_id],
            }

            created_document = self.drive_service.files().create(body=document_metadata).execute()

            # Get the ID of the newly created document
            document_id = created_document['id']
            
            # Get the webViewLink
            webViewLink = created_document['webViewLink']

            # Update the permissions to allow anyone with the link to edit
            self.drive_service.permissions().create(
                fileId=document_id,
                body={
                    'type': 'anyone',
                    'role': 'writer',
                }
            ).execute()

            return webViewLink
    
        except Exception as e:
            return f"Error creating your file: {e}"




        # if doc_title == None:
        #     doc_title = "A Little Help"
        # try:
        #     doc = self.docs_service.documents().create(body={"title": doc_title}).execute()
        #     if doc:
        #         doc_id = doc["documentId"]
        #         permission = {"type": "anyone", "role": "writer", "withLink": True}
        #         self.drive_service.permissions().create(fileId=doc_id, body=permission).execute()
        #         file_url = f"Document URL: https://docs.google.com/document/d/{doc_id}"
        #         return file_url
        #     else:
        #         raise HttpError
        # except Exception:
        #     return "Error: File Creation Unsuccesful, Try Again"

        




    def createSlide(self, folder_name, slide_title=None):
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


    def createSheet(self, folder_name,  sheet_title=None):
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
        






    def getDoc(self, folder_name, doc_title=None):
        try:
            if doc_title == None:
                return "You need to specify a document title"
            
        
            folder_id = self.getOrCreateFolder(folder_name)
            results = self.drive_service.files().list(q = f"name = '{doc_title}' and {folder_id} in parents").execute()
            files = results.get("files", [])
            

            if not files:
                return "Could not find your file. For security purposes files created in a server are only accessible in that server.\n Make sure you spelt the filename correctly and you are in the server the file was created on."
            elif len(files) == 1:
                file = files[0]
                result = self.drive_service.files().get(fileId = file.get("id"), fields='webViewLink').execute()
                return f"Found your file! {result}"
            else:
                allFiles = "Found multiple files:\n"
                for file in files:
                    result = self.drive_service.files().get(fileId = file.get("id"), fields='webViewLink').execute()
                    allFiles += f"\n\n\n{result.get('webViewLink')}"
                return allFiles
   
        except Exception as e:
            return f"Error finding your file: {e}"





    def getOrCreateFolder(self, folder_name):
        results = self.drive_service.files().list(q= f"mimeType='application/vnd.google-apps.folder' and name={folder_name}").execute()
        folders = results.get('files', [])

        if folders:
            return folders[0]['id']
        else:
            folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
            }

            folder = self.drive_service.files().create(body=folder_metadata, fields='id').execute()
            return folder['id']
