import os
import logging
import shutil
# Configure logging
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            logging.error("Folder not found: " + folder_path)
            return
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                extension = file.split('.')[-1].lower()

                if extension in ['jpg', 'png', 'jpeg']:
                    target_folder = "Images"
                elif extension == 'pdf':
                    target_folder = "PDFs"
                elif extension == 'txt':
                    target_folder = "TextFiles"
                else:
                    target_folder = "Others"

                target_path = os.path.join(folder_path, target_folder)

                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                    logging.info("Created folder: " + target_folder)

                shutil.move(file_path, os.path.join(target_path, file))
                logging.info(f"Moved {file} to {target_folder}")

        print("File organization completed successfully.")
        logging.info("File organization completed.")

    except Exception as e:
        print("An error occurred:", e)
        logging.error(str(e))

folder_path = input("Enter the folder path to organize: ")
organize_files(folder_path)
