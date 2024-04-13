from utils.util_prompt import UtilPrompt
from utils.util_web_request import UtilWebRequest
from os import environ as env
import json


class ServiceTodoist:

    def get_projects(self, token):
        # Define Services
        web_request = UtilWebRequest()
        service_prompt = UtilPrompt()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Check token authtentication
        if web_request.check_auth(
                headers, None, env["BASE_API_URL"]+r"/get_all?limit=1", None):
            service_prompt.message("Successfully authenticated via API Token")
        else:
            raise Exception("Something went wrong while authenticating")

        url = env["BASE_GET_PROJECTS_URL"]
        r = web_request.get(headers, None, url, None)
        return json.loads(r.text)

    def get_task(self, token, time_period):
        # Define Services
        web_request = UtilWebRequest()
        service_prompt = UtilPrompt()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Check token authtentication
        if web_request.check_auth(
                headers, None, env["BASE_API_URL"]+r"/get_all?limit=1", None):
            service_prompt.message("Successfully authenticated via API Token")
        else:
            raise Exception("Something went wrong while authenticating")

        # Obtain tasks
        limit = int(env["API_LIMIT"])
        offset = 0
        since = time_period+"T00:00:00"
        task_list = []
        while (True):
            url = env["BASE_GET_TASK_URL"].format(
                limit=limit,
                offset=offset,
                since=since
            )
            r = web_request.get(headers, None, url, None)
            body = json.loads(r.text)
            task_list += body["items"]
            offset += limit
            if len(body["items"]) == 0:
                break
        return task_list
