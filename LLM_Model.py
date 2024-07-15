from langchain.llms import Ollama
from langchain import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from pydantic import BaseModel, Field


# Initialize Ollama LLM
llm = Ollama(model="llama3")
class FishingEmail(BaseModel):
    subject: str = Field(..., description="The actual prompt subject")
    body: str = Field(None, description="The actual prompt body")
    email_from : str = Field(0.7, description="From email address")
    email_to: str = Field(100, description="To email address")

prompt1 = FishingEmail(
    subject="Invitation to Join Us at the International Tech Conference 2024",
    body="Dear $$RecipientName$$, We are pleased to extend a personal invitation to you to attend the International Tech Conference 2024, scheduled for September 13-15 at $$location$$. This event will bring together industry leaders, innovative thinkers, and technology enthusiasts from around the globe. Explore the latest in technology and gain insights from experts at the forefront of technological advancement. To confirm your attendance and for more information, please visit the registration page here: $$link$$ For any inquiries, do not hesitate to contact me directly. Warm regards, [Your Name]",
    email_from="alex.morgan@innovationcorp.com",
    email_to="partners@venturefirm.com"
)
prompt2 = FishingEmail(
    subject="Join Us at the International Tech Conference 2024 – Don’t Miss Out!",
    body="Hi $$RecipientName$$, Get ready for three exciting days of cutting-edge tech, breakthrough innovations, and inspiring sessions by world-class speakers! Join us at the International Tech Conference 2024 from September 13-15 at $$location$$. Let’s dive into the future together! Secure your spot by registering here: $$link$$ Got questions? Just hit reply – I’m here to help Cheers, [Your Name]",
    email_from="events@globalconferences.com",
    email_to="invitees@industry.com"
)
prompt3 = FishingEmail(
    subject="Attend the Premier International Tech Conference 2024",
    body="Dear $$RecipientName$$, We are delighted to invite you to attend the International Tech Conference 2024, taking place from September 13-15, 2024, at $$location$$. This premier event will feature an array of sessions focused on the impact of technology in various industries, interactive workshops, and networking opportunities with global professionals. Don’t miss out on the opportunity to enhance your professional skills and connect with leaders in the field. Please register for the conference at $$link$$. For further details or assistance, feel free to contact me. Best regards,[Your Name]",
    email_from="finance@techstartup.com",
    email_to="board@techstartup.com"
)

prompt4 = FishingEmail(
    subject="Comprehensive Monthly Financial Report for [Month-Year]",
    body="Dear $$RecipientName$$, We are pleased to provide you with the Monthly Financial Report for [Month-Year]. This report includes a detailed analysis of our financial performance, including income statements, balance sheets, and cash flow statements. You can access the complete report by clicking on the following link: [Insert Link Here] We encourage you to review the attached report and reach out if you have any questions or require further clarification on any aspect of the report. Best Regards, [Your Full Name]",
    email_from="alex.morgan@innovationcorp.com",
    email_to="partners@venturefirm.com"
)
prompt5 = FishingEmail(
    subject="[Month-Year] Financial Report Available",
    body="Hello $$RecipientName$$, The financial report for [Month-Year] is now available. We have summarized the key financial metrics and provided a full analysis in the attached document. Please review the detailed report at your convenience here: [Insert Link Here] For any inquiries or additional details, please feel free to contact me directly. Thank you, [Your Full Name]",
    email_from="events@globalconferences.com",
    email_to="invitees@industry.com"
)
prompt6 = FishingEmail(
    subject="Here's Your [Month-Year] Financial Overview!",
    body="Hi $$RecipientName$$, I hope this message finds you well! I'm excited to share our financial report for [Month-Year]. This comprehensive document captures all our financial activities and outcomes for the month. You can view and download the report using this link: [Insert Link Here] Please don't hesitate to get in touch if you have any comments or need clarification on any points in the report. Best wishes, [Your Full Name]",
    email_from="finance@techstartup.com",
    email_to="board@techstartup.com"
)
json_prompt1 = prompt1.model_dump_json()
json_prompt2 = prompt2.model_dump_json()
json_prompt3 = prompt3.model_dump_json()
json_prompt4 = prompt4.model_dump_json()
json_prompt5 = prompt5.model_dump_json()
json_prompt6 = prompt6.model_dump_json()
#print(json_prompt1)

parser = PydanticOutputParser(pydantic_object=FishingEmail)

examples = [
    {
        "question": "Write an formal email to invite for International Tech Conference 2024 at $$location$$ from September 13-15, 2024, include register link $$link$$ and provide my contact information to $$RecipientName$$",
        "answer": "{" + json_prompt1 + "}",
    },
    {
        "question": "Write an casual and friendly email to invite for International Tech Conference 2024 at $$location$$ from September 13-15, 2024, include register link $$link$$ and provide my contact information to $$RecipientName$$",
        "answer": "{" + json_prompt2 + "}",
    },
    {
        "question": "Write an Professional and Detailed email to invite for International Tech Conference 2024 at $$location$$ from September 13-15, 2024, include register link $$link$$ and provide my contact information to $$RecipientName$$",
        "answer": "{" + json_prompt3 + "}",
    },
{
        "question": "Write an Formal and Detailed Company Report email for $$month,year$$ which includes link to $$RecipientName$$",
        "answer": "{" + json_prompt4 + "}",
    },
    {
        "question": "Write an concise and direct Company Report email for $$month,year$$ which includes link to $$RecipientName$$",
        "answer": "{" + json_prompt5 + "}",
    },
    {
        "question": "Write an friendly and informative Company Report email for $$month,year$$ which includes link to $$RecipientName$$",
        "answer": "{" + json_prompt6 + "}",
    },
]


example_template = """
##User##: {question}
##AI##: {answer}
"""
example_prompt = PromptTemplate(
        input_variables=["question", "answer"], template=example_template
)

prefix = """You are an intelligent email creator. Use the following examples to produce emails.

{format_instructions}

##Examples:
"""
# and the suffix our user input and output indicator
suffix = """
##User##: {input}
##AI##: """
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input"],
    example_separator="\n\n",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

print(prompt)
print("Prompting done")
def Llama_output(input_prompt):
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(input=input_prompt)
    return response

