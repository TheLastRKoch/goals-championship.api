from services.service_calculate_score import ServiceCalculateScore
from services.service_formatter import ServiceFormatter
from utils.util_prompt import UtilPrompt
from services.service_filter_tasks import ServiceFilterTasks
from services.service_todoist import ServiceTodoist
import json


class ServiceStart:

    def run(self):
        keep = True
        i = 0
        while (keep):
            try:

                # Define Services
                prompt = UtilPrompt()
                service_todoist = ServiceTodoist()
                formatter = ServiceFormatter()

                prompt.welcome()
                token = prompt.ask_user_token()
                time_period = prompt.ask_time_period()

                service_todoist.check_token_auth(token)
                project_list = service_todoist.get_projects(token)
                task_list = service_todoist.get_task(token, time_period)
                payload = formatter.merge_tasks_projects(task_list, project_list)

                prompt.message(
                        "\n\nAll tasks:\n"+json.dumps(payload, indent=2))

                keep = False
            except Exception as err:
                prompt.message_wait("Error: "+str(err))
                if i < 3:
                    i += 1
                else:
                    keep = False
