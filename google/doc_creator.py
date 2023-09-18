import google.auth
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from discord import app_commands


#This class leverages the google drive api to create google docs, slides, and sheets as well as be able to retrieve the documents created
#The API_KEY/credentials come from a google service account you can find info from google here https://developers.google.com/workspace/guides/create-credentials#service-account
#This uses the V3 version of the google drive API so if you are going to use this make sure to enable the drive api under the service account and give it all the privledges

#This is a helper class for my discord bot.
#It creates docs, slides, and sheets in a folder named after the server the file was created in.
#It also retrieves files based on the servers name, meaning files can only be retrieved from the server they were created in.
class Doc_Creator:

    def __init__(self) -> None:
        #API_Key to be able to use googles services
        API_KEY = "/home/pi/Python/A-Little-Help/google/gDrive.json"

        # Get the Scopes (permissions) to be able to create each type of document and interact with google drive
        DOCS_SCOPE = "https://www.googleapis.com/auth/documents"
        SLIDES_SCOPE = "https://www.googleapis.com/auth/presentations"
        DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"
        SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"

        #create the credentials to use the service, credentials come from the json obtained from the google follow the link above to get it
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





    # Create a new Google Drive doc inside of a folder. you need to specify the name of the folder
    # You dont need to specify the name of the document, it will get the name "default" without specifying

    #Args:
        #folder_name: The name of the folder to put the file in(in my case the name of the server)
        #doc_title: The name of the document you are trying to create
    #Returns:
        #The webViewLink of the newly created document
    async def createDoc(self, interaction, doc_title=None):
        if doc_title == None:
            doc_title = "default"


        try:
            #Gets the folder id to put the file in
            folder_id = self.getOrCreateFolder(interaction.guild)

            #Set the metadata for the file
            #mimeType is the kind of file it is
            #parents is the folder
            document_metadata = {
                'name': doc_title,
                'mimeType': 'application/vnd.google-apps.document',
                'parents': [folder_id],
            }

            #create the document
            created_document = self.drive_service.files().create(body=document_metadata, fields='id,webViewLink').execute()

            # Get the ID of the newly created document
            document_id = created_document.get('id')
            
            # Get the webViewLink
            webViewLink = created_document.get('webViewLink')

            # Update the permissions to allow anyone with the link to edit
            self.drive_service.permissions().create(
                fileId=document_id,
                body={
                    'type': 'anyone',
                    'role': 'writer',
                }
            ).execute()

            await interaction.followup.send(webViewLink)
    
        except Exception as e:
            await interaction.followup.send(f"Error creating your file: {e}")

        



    # Create a new Google Drive slide inside of a folder. you need to specify the name of the folder
    # You dont need to specify the name of the document, it will get the name "default" without specifying

    #Args:
        #folder_name: The name of the folder to put the file in(in my case the name of the server)
        #slide_title: The name of the document you are trying to create
    #Returns:
        #The webViewLink of the newly created document
    def createSlide(self, folder_name, slide_title=None):
        if slide_title == None:
            slide_title = "default"
        try:
            #Gets the folder id to put the file in
            folder_id = self.getOrCreateFolder(folder_name)

            #Set the metadata for the file
            #mimeType is the kind of file it is
            #parents is the folder
            document_metadata = {
                'name': slide_title,
                'mimeType': 'application/vnd.google-apps.presentation',
                'parents': [folder_id],
            }

            #create the document
            created_document = self.drive_service.files().create(body=document_metadata, fields='id,webViewLink').execute()

            # Get the ID of the newly created document
            document_id = created_document.get('id')
            
            # Get the webViewLink
            webViewLink = created_document.get('webViewLink')

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



    # Create a new Google Drive sheet inside of a folder. you need to specify the name of the folder
    # You dont need to specify the name of the document, it will get the name "default" without specifying

    #Args:
        #folder_name: The name of the folder to put the file in(in my case the name of the server)
        #sheet_title: The name of the document you are trying to create
    #Returns:
        #The webViewLink of the newly created document
    def createSheet(self, folder_name,  sheet_title=None):
        if sheet_title == None:
            sheet_title = "default"

        try:
            #Gets the folder id to put the file in
            folder_id = self.getOrCreateFolder(folder_name)

            #Set the metadata for the file
            #mimeType is the kind of file it is
            #parents is the folder
            document_metadata = {
                'name': sheet_title,
                'mimeType': 'application/vnd.google-apps.spreadsheet',
                'parents': [folder_id],
            }

            #Create the file
            created_document = self.drive_service.files().create(body=document_metadata, fields='id,webViewLink').execute()

            # Get the ID of the newly created document
            document_id = created_document.get('id')
            
            # Get the webViewLink
            webViewLink = created_document.get('webViewLink')

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
        



    #Retieves the webViewLink of a Google Drive file that has previously created.
    #For possible security reasons, only files created in a server can be retrieved from that server.

    #Args:
        #folder_name: The name of the folder to look for the file (in my case the name of the server)
        #doc_title: The name of the document you are trying to find
    #Returns:
        #A message if no file is found
        #A webViewLink if only one file of that name is found
        #Multiple webViewLinks if multiple files are found with that name
    def getDoc(self, folder_name, doc_title=None):
        if doc_title == None:
            return "You need to specify a document title"
        
        try:
            #Get the id of the folder to look in
            folder_id = self.getOrCreateFolder(folder_name)

            #Search for the file in the folder
            results = self.drive_service.files().list(q = f"name = '{doc_title}' and '{folder_id}' in parents").execute()
            files = results.get("files", [])
            
            #No files were found
            if not files:
                return "Could not find your file. \nFiles created in a server are only accessible in that server.\nMake sure you spelt the filename correctly and you are in the server the file was created on."
            
            #Only 1 file was found
            elif len(files) == 1:
                file = files[0]
                result = self.drive_service.files().get(fileId = file.get("id"), fields='webViewLink').execute()
                return f"Found your file! {result.get('webViewLink')}"
            
            #Multiply files were found
            else:
                allFiles = "Found multiple files:"
                for file in files:
                    result = self.drive_service.files().get(fileId = file.get("id"), fields='webViewLink').execute()
                    allFiles += f"\n\n{result.get('webViewLink')}"
                return allFiles
   
        except Exception as e:
            return f"Error finding your file: {e}"




    #Function name says it all
    #Trys to get the id of a google drive folder
    #If the folder does not exist, it creates the folder and returns that id
    def getOrCreateFolder(self, folder_name):
        #Look to see if the folder exists
        results = self.drive_service.files().list(q= f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}'").execute()
        folders = results.get('files', [])

        #Folder exists return its id
        if folders:
            return folders[0].get('id')
        
        #Folder doesnt exist create the folder and return its id
        else:
            folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
            }

            folder = self.drive_service.files().create(body=folder_metadata, fields='id').execute()
            return folder.get("id")
