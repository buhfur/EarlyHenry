
import os
import sys
import sqlite3

class Storage:
    def __init__(self):

        self.DEFAULT_PATH = "C:\HenryFolders"




    def store_json(self, filename):
        return

    def store_video(self):
        return

    def store_picture(self):
        return

    def store_pdf(self):
        return

    def store_database(self):
        return

    def create_file(self, file_name, file_type):
        if file_type == "json":
            with open("{}.json", 'wb+').format(file_name) as json_file:
                


        return

    def create_folder(self, folder_name):



    def create_template(self):
        #different templates could be
        #flask project, visual studio project
        #java project

        return

    def create_database(self, table_name, database_name):
        #Default number of columns will be 2


    def delete_file(self, file_name):
        try:
            os.rmdir(file_name)

        except:
            return False
