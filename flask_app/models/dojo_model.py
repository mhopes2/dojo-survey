from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def save( cls, data ):
        query = "INSERT INTO dojo_survey (name, location, language, comment) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s );"
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return result

    @classmethod
    def get_survey( cls ):
        query = "SELECT * FROM dojo_survey ORDER BY dojo_survey.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return cls(results[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Must choose a location")
            is_valid = False
        if len(survey['language']) < 1:
            flash("Must choose a coding language")
            is_valid = False
        if len(survey['comment']) < 3:
            flash("Comment must be at least 3 characters")
            is_valid = False
        return is_valid