import smtplib
from email.mime.text import MIMEText

def send_mail_test(customer, rating, feedback):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'e3a5118e97b1e5'
    password ='f1775a51b8a149'
    message = f'<h3>New Review Submitted!</h3><p>{customer} has a given us a rating of: {rating} with feedback stating: {feedback}</p>'
    sender_email = 'manilaeateryfeedback@gmail.com'
    receiver_email = 'manilaeatery45@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Manila Eatery: New Review'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    
# def send_mail(customer, rating, feedback):
#     message = f'<h3>New Review Submitted!</h3><p>{customer} has a given us a rating of: {rating} with feedback stating: {feedback}</p>'
#     sender_email = 'manilaeateryfeedback@gmail.com'
#     sender_password = ''
#     receiver_email = 'manilaeatery45@gmail.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Manila Eatery: New Review'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
#     session.starttls() #enable security
#     session.login(sender_email, sender_password) #login with mail_id and password
#     text = msg.as_string()
#     session.sendmail(sender_email, receiver_email, text)
#     session.quit()