from flask import Flask
import graphene
import os
from graphene import ObjectType, String, Schema, Boolean, List
from flask_graphql import GraphQLView
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
CORS(app)


class Maize(ObjectType):
    hash = String()
    written_to_db = Boolean()
    points = List(int)


class Solution(ObjectType):
    question = String()
    questionID = String()




class Query(ObjectType):

    get_question = graphene.Field(Question)

    get_category_question = graphene.Field(Categorize)

    set_category_question = String(sender=String(),
                                   questionID=String(),
                                   category=String(),
                                   timestamp=String(),
                                   categorized=graphene.Boolean(String)
                                   )

    get_reply = graphene.Field(Reply,
                               question=String(),
                               sender=String(),
                               timestamp=String(),
                               context=String()
                               )

    answer_question = String(sender=String(),
                             questionID=String(),
                             timestamp=String(),
                             answer=String()
                             )

    train = String(
        key = String()
    )

    add_answer_csv = String(
        category=String(),
        answer=String(),
        key = String()
    )

    add_question_csv = String(
        category=String(),
        question=String(),
        key = String()
    )

    test = String(
    )

    def resolve_test(root, info):
        return "Test Sucessful"

    def resolve_get_question(root, info):
        retreived_question = DataHandler.get_question()
        question = retreived_question["question"]
        questionID = retreived_question["questionID"]
        return {"question": question, "questionID": questionID}

    def resolve_get_category_question(root, info):
        retreived_question = DataHandler.get_question()
        question = retreived_question["question"]
        questionID = retreived_question["questionID"]
        try:
            predicted_category = inferer.classify_intent(question)
        except Exception as e:
            logger.log_traceback(e)
            # here there might be errors from infer of datahandler
            logger.log("Classify intent Error Logged", repr(e))
            predicted_category: [
                "**not_available**", "Error occuered at graphsql_server.py line 100", "while classifing check current inferer"]
        data = {"predicted_category": predicted_category,
                "question": question,
                "questionID": questionID}
        return data

    def resolve_set_category_question(root, info, questionID, category, sender, timestamp, categorized):
        written_to_database = False
        data_dictionary = {'questionID': questionID,
                           'sender': sender,
                           'timestamp': int(timestamp),
                           'category': category,
                           'categorized': True
                           }
        written_to_database = DataHandler.save_user_data(data_dictionary)
        if written_to_database:
            return "Category saved to database"
        return "There was an error saving to the Database"

    def resolve_get_reply(root, info, question, sender, timestamp, context):
        written_to_database = False
        try:
            reply = inferer.craft_reply(question, previous_context=context)
        except Exception as e:
            logger.log_traceback(e)
            logger.log("Craft Reply Error Logged!", repr(e))
            reply = "My brain isn't working right now. I have to think", ''
        hash_question = hashlib.md5(question.encode('utf-8')).hexdigest()
        data_dictionary = {'questionID': hash_question,
                           'question': question,
                           'sender': sender,
                           'timestamp': int(timestamp)
                           }
        written_to_database = DataHandler.save_user_data(data_dictionary)
        data = {
            "reply": reply[0], "written_to_db": written_to_database, "context": reply[1]}
        return data

    def resolve_answer_question(root, info, questionID, sender, timestamp, answer):
        written_to_database = False
        data_dictionary = {'questionID': questionID,
                           'sender': sender,
                           'timestamp': int(timestamp),
                           'answer': answer
                           }
        written_to_database = DataHandler.save_user_data(data_dictionary)
        if written_to_database:
            return "Answer saved to database"
        return "There was an error saving to the Database"

    def resolve_add_answer_csv(root, info, answer, category, key):
        if (key == config.GQL_AUTH):
            file_name = config.r_answers_data
            message = DataHandler.write_to_csv(file_name, category, answer)
            return message
        else:
            return "Authentication Failed"

    def resolve_add_question_csv(root, info, question, category, key):
        if (key == config.GQL_AUTH):
            file_name = config.r_training_data
            message = DataHandler.write_to_csv(file_name, category, question)
            return message
        else:
            return "Authentication Failed"

    def resolve_train(root, info, key):
        if (key == config.GQL_AUTH):
            try:
                inferer.train()
                return "Training Successful"
            except Exception as e:
                logger.log_traceback(e)
                logger.log("Training Error Logged", repr(e))
                return "Training Unsuccessful"+repr(e)
        else:
            return "Authentication Failed"


schema = Schema(query=Query)


@app.route("/")
def index():
    return "API endpoints available on: /api"


app.add_url_rule(
    "/api", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
