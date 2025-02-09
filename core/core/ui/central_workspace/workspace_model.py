
class WorkspaceModel:
    def __init__(self, data_info={}, credentials={}):
        self.data_info = data_info
        self.credentials = credentials

    def get_data_info(self):
        return self.data_info
    
    def get_credentials(self):
        return self.credentials