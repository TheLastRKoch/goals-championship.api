from services.service_start import ServiceStart
from dotenv import load_dotenv


# Load env variables
load_dotenv()

# Service Definition
start = ServiceStart()
start.run()
