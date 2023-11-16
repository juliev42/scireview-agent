
class SciReviewAgent:
    """
    LLM-powered research agent for researching new areas and conversing on the topic it has researched on.
    """
    def __init__(self, query, report_type, database = None, config_path=None, websocket=None):
        self.query = query
        self.report_type = report_type
        self.config = config_path
        self.database = database
        self.websocket = websocket
        self.context = []
        self.allowed_domains = ["pubmed"]

    async def run(self):
        ## initialize database
        

        ##get subqeurys 

        ##search for information

        ##scrape urls 

        ##index raw data from urls into vector db

        ##return short summary report

        pass

    async def get_new_sites(self, url_set_input):
        pass

    async def run_sub_query(self, sub_query):
        pass

    async def get_summary_report(self):
        pass
    
