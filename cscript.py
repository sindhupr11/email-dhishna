import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os 
def send_email(sender_email, sender_password, receiver_email, subject, message):
    message_obj = MIMEMultipart()
    message_obj['From'] = sender_email
    message_obj['To'] = receiver_email
    message_obj['Subject'] = subject
    attachment_path = "../email-gdsc/pdfs/cs-brochure-23.PDF"  # Replace with the actual path to your attachment file

    message_obj.attach(MIMEText(message, 'plain'))
    # Open the file in binary mode
    with open(attachment_path, "rb") as attachment:
        # The application type is pdf
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header 
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(attachment_path)}",
    )

    # Add attachment to your message and convert it to string
    message_obj.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message_obj)
            print(f"Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print(f"Failed to authenticate with the SMTP server. Check your username/password.")
    except smtplib.SMTPConnectError:
        print(f"Failed to connect to the SMTP server. Check your network connection.")
    except smtplib.SMTPServerDisconnected:
        print(f"The SMTP server unexpectedly disconnected. Try again later.")
    except smtplib.SMTPRecipientsRefused:
        print(f"The recipient's email address was refused: {receiver_email}. Check the email address.")
    except smtplib.SMTPSenderRefused:
        print(f"The sender's email address was refused: {sender_email}. Check the email address.")
    except smtplib.SMTPDataError:
        print(f"The SMTP server refused to accept the message data.")
    except smtplib.SMTPException as e:
        print(f"An error occurred. Error: {str(e)}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {str(e)}")
        print(f"SMTP Server Response: {e.smtp_error.decode()}")
        import traceback
        traceback.print_exc()

sender_email = 'acescusat1@gmail.com'
sender_password = 'pswrd'  # Using application-specific password
subject = 'Invitation to Dhishna - Tech Fest 2023'


participants = {

    'sindhupr2003@gmail.com', 'antonprince95@gmail.com'
}

message = f'''
Respected Sir/Ma'am,

I trust this message finds you well. On behalf of the Computer Science Department at Cochin University of Science and Technology (CUSAT), I am honored to extend an invitation to you for our annual technical extravaganza, Dhishna, scheduled to take place from November 24th to 26th.

Event Highlights:

1. GenAI magic:
   Witness the magic of generative artificial intelligence, where innovation meets the limitless possibilities of AI.

2. Typing Contest:
   Showcase your speed and accuracy in our Typing Contest, a challenge for those with nimble fingers and a flair for precision.

3. Cusat Esport:
   Unleash your competitive spirit in Cusat Esport, where gaming enthusiasts come together for thrilling competitions and camaraderie.

4. Outdoor Sketching:
   Unleash your creativity with outdoor sketching sessions, providing a refreshing break from the digital world.

5. Web3:
   Explore the evolution of the internet with a focus on Web3, understanding its transformative potential and implications.

6. Beneath the Clock:
   Embark on a mysterious journey with "Beneath the Clock," an event that promises puzzles, challenges, and an unforgettable experience.

Dhishna is more than just a tech fest; it is a celebration of innovation, collaboration, and the spirit of technology. Our event draws participants from across the country, showcasing the diversity and talent that CUSAT is renowned for.

We would be honored to have representatives from your esteemed organization join us for this grand event. Your participation will not only enhance the success of Dhishna but also offer students unique opportunities for networking and skill development, fostering connections with some of the brightest minds in technology.

For additional details, please refer to the attached brochure. 

Dhishna official site link: https://www.dhishna.org

Thank you for your time and consideration. We eagerly anticipate the pleasure of hosting you at Dhishna 2023.

Best regards,
 Computer Science Department 
 Cochin University of Science and Technology (CUSAT)
'''

for email in participants:
    send_email(sender_email, sender_password, email, subject, message)



