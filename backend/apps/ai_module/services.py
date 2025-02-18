from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import pipeline

class ProjectAIService:
    def __init__(self):
        self.risk_analyzer = pipeline(
            "text-classification", 
            model="ml_models/risk_prediction/"
        )
        
    def generate_project_plan(self, inputs):
        template = """Generate PMI-compliant project plan for:
        Project Type: {project_type}
        Complexity Level: {complexity}
        Team Size: {team_size}
        Output Format: JSON"""
        
        prompt = PromptTemplate.from_template(template)
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(inputs)
    
    def analyze_risks(self, project_data):
        return self.risk_analyzer(project_data.description)