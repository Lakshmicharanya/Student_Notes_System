from database.connection import DatabaseConnection


def createTables():

    try:

        db_config = DatabaseConnection()
        cursor = db_config.cursor()

        # Users table
        users_table_query = """
        CREATE TABLE IF NOT EXISTS users(
            userid BIGINT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            hashpassword VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        # Notes table
        notes_table_query = """
        CREATE TABLE IF NOT EXISTS notes(
            notesid BIGINT AUTO_INCREMENT PRIMARY KEY,
            userid BIGINT,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY(userid) REFERENCES users(userid)
                ON DELETE CASCADE
        )
        """

        # Files table
        files_table_query = """
        CREATE TABLE IF NOT EXISTS files(
            fileid BIGINT AUTO_INCREMENT PRIMARY KEY,
            userid BIGINT,
            originalname VARCHAR(100) NOT NULL,
            storedname VARCHAR(100) NOT NULL,
            mimetype VARCHAR(255) NOT NULL,
            size INT,
            filepath VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(userid) REFERENCES users(userid)
                ON DELETE CASCADE
        )
        """

        cursor.execute(users_table_query)
        cursor.execute(notes_table_query)
        cursor.execute(files_table_query)

        db_config.commit()

        cursor.close()
        db_config.close()

        return "Tables created successfully"

    except Exception as e:

        return f"Something wrong in database/tables.py: {e}"
   