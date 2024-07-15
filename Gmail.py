import smtplib
sender_email = "sandeepkokkula2807@gmail.com"
app_password = "sbtd bygt mqsv yalf"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, app_password)
mail_content = "Hello World!"
server.sendmail(sender_email, sender_email, mail_content)
server.quit()