import smtplib
from LLM_Model import *
import sys
def send_mail(response):

    sender_email = "test@gmail.com"
    app_password = "sbtd bygt mqsv yalf"
    receiver_email = "test@gmail.com"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    mail_content = """{"subject": "Comprehensive Annual Financial Report for [Year]","body": "Dear Director, We are pleased to provide you with our Comprehensive Annual Financial Report for [Year]. This report includes a detailed analysis of our financial performance, including income statements, balance sheets, and cash flow statements. You can access the complete report by clicking on the following link: [Insert Link Here] We encourage you to review the attached report and reach out if you have any questions or require further clarification on any aspect of the report. Best Regards, [Your Full Name]","email_from": "alex.morgan@innovationcorp.com","email_to": "director@company.com"}"""
    server.sendmail(sender_email, receiver_email, mail_content)
    server.quit()

if __name__ == "__main__":

    print("Done")