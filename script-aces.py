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

    'sindhupr2003@gmail.com', 'antonprince95@gmail.com',
    'principal.cptc@gmail.com', 'gwptc@yahoo.co.in', 'gptcnta@gmail.com', 'gptcnedumangad@gmail.com', 'gptcatl@gmail.com', 'gptcplr@gmail.com', 'snpolytechnic@yahoo.co.in', 'gptcezhukone@gmail.com', 'gptcvnklm@yahoo.com', 'gptcadr@gmail.com', 'nsspolytechnic@yahoo.com', 'gptcvchr@gmail.com', 'gptcctl@gmail.com', 'carmelpolytechniccollege@gmail.com', 'wptckylm@gmail.com', 'kottayampolyemail@yahoo.com', 'gptcpala@yahoo.com', 'gpckdy@yahoo.com', 'gptcmuttom@yahoo.co.in', 'gptckumily@rediffmail.com', 'gptcnedumkandam@yahoo.co.in', 'gptcpurappuzha@rediffmail.com', 'gptckalamassery@dataone.in', 'sjwptc@gmail.com', 'polytechnickothamangalam@gmail.com', 'gptcpbvr@gmail.com', 'mtitsr@rediffmail.com', 'srpolyoffice@gmail.com', 'mail@thiagarajarpolytechnic.org', 'prlgptckty@gmail.com', 'polykkm@yahoo.co.in', 'wpttcr@rediffmail.com', 'gptcchelakkara@yahoo.com', 'gptcpalakkad@gmail.com', 'polyshoranur@dataone.in', 'polypmna@gmail.com', 'gptctgdi@gmail.com', 'ssmpoly@sify.com', 'gwptckottakkal@gmail.com', 'info@mahdinonline.com', 'kgptc@yahoo.com', 'wptccalicut@asianetindia.com', 'awhptc@gmail.com', 'poly@kmct.edu.in', 'jdtpoly@gmail.com', 'cnn_gptknr@bsnl.com', 'gptcmattanur@gmail.com', 'rwpcpnr@yahoo.co.in', 'gptc24wayanad@gmail.com', 'gptcmepadi@rediffmail.com', 'principalksgd@gmail.com', 'principalksgd@yahoo.in', 'snpolytechnic@yahoo.co.in', 'gptctkr@gmail.com', 'mptpainavu@ihrd.ac.in', 'mptkarunagappally@ihrd.ac.in', 'eknmmptkallyassery@ihrd.ac.in', 'mptmala@ihrd.ac.in', 'mptmattakkara@ihrd.ac.in', 'mptvadakara@ihrd.ac.in',
    'principal@acetvm.com', 'ceattingal@ihrd.ac.in', 'principal@cemuttathara.ac.in', 'principal@cet.ac.in', 'principal@gecbh.ac.in', 'principal@hcet.in', 'principal@jcmcsiit.ac.in', 'principal@lbsitw.ac.in', 'lourdesmathaoffice@gmail.com', 'mgcet2011@gmail.com', 'principal@mbcet.ac.in', 'mail@marian.ac.in', 'chairman@mcetonline.com', 'principal@musaliarcollegeckl.com', 'macevprincipal@gmail.com', 'paacet2003@gmail.com', 'principal@riet.edu.in', 'principal@sist.in', 'principal@sctce.ac.in', 'info@thetrinitycollege.in', 'principal@stisttvm.edu.in', 'vksbkt2008@gmail.com', 'principal@vidyatcklmr.ac.in', 'padmasuresh77@gmail.com', 'bishopjeromegi@yahoo.com', 'cekottarakkara.ihrd@gmail.com', 'principal@ceknpy.ac.in', 'principal@perumonec.ac.in', 'principal.pathanapuram@gmail.com', 'principal@mesitam.ac.in', 'shmenggcollege@gmail.com', 'principal@tkmce.ac.in', 'principal@tkmit.ac.in', 'tecprincipalcet@gmail.com', 'ukfindia@gmail.com', 'principalyounuscollegekollam@gmail.com', 'principal@cek.ac.in', 'principal@cea.ac.in', 'principal@cearanmula.ac.in', 'mzcengg@mail.com', 'principal@musaliarcollege.com', 'sbcewae@gmail.com', 'principal@snit.edu.in', 'ccetalappuzha@gmail.com', 'principal.cemp@gmail.com', 'principal@ceconline.edu', 'principal@cectl.ac.in', 'kvmceit@gmail.com', 'office@mahagurutech.ac.in', 'mountzionist@gmail.com', 'principal@providence.edu.in', 'principal@sbce.ac.in', 'info@stcet.net', 'office@amaljyothi.ac.in', 'cekcape@gmail.com', 'cepoonjar.ihrd@gmail.com', 'gisatonline@gmail.com', 'kitscollegeprincipal2015@gmail.com', 'principal@mangalam.in', 'principalktu@rit.ac.in', 'mail@saintgits.org', 'principal@sjcetpalai.ac.in', 'tomtjoseph45@gmail.com', 'principalaacet@gmail.com', 'mail@cemunnar.ac.in', 'gecidukki@ktu.edu.in', 'mbc@mbcpeermade.com', 'principal@ucet.ac.in', 'principal@adishankara.ac.in', 'manager@aisat.ac.in', 'city@christknowledgecity.com', 'mail@fisat.ac.in', 'ilahia@icet.ac.in', 'principal@iipe.in', 'jaibharathengg@gmail.com', 'principal@kmeacollege.ac.in', 'principal@mace.ac.in', 'mbits@ktu.edu.in', 'cochinist@ktu.edu.in', 'mescet.kunnukara@gmail.com', 'mail@mgmcet.ac.in', 'principal@mec.ac.in', 'principal@mgits.ac.in', 'office@rajagiritech.edu.in', 'anithagpillai@scmsgroup.org', 'sngist@sngist.org', 'info@snmimt.edu.in', 'info@sngce.ac.in', 'mail@tistcochin.edu.in', 'office@visat.ac.in', 'contact@cce.edu.in', 'principal@gectcr.ac.in', 'bennyjohn100@gmail.com', 'ernakulathappantrust@gmail.com', 'mail@iesce.info', 'principal@jecc.ac.in', 'gkftvm@gmail.com', 'mets@metsengg.ac.in', 'office@ncerc.ac.in', 'nicechalakudy@gmail.com', 'royal@ktu.edu.in', 'exedirector@sahrdaya.ac.in', 'info@thejusengg.ac.in', 'info@uec.ac.in', 'principal@vidyaacademy.ac.in', 'principal.aset@ahalia.edu.in', 'principal@alameencollege.com', 'principal@gecskp.ac.in', 'jcetncerc@gmail.com', 'principal@nssce.ac.in', 'principal@rist.edu.in', 'principal@simat.ac.in', 'office@ekc.edu.in', 'info@meaec.edu.in', 'principal@mesce.ac.in', 'principal@mgmcet.in', 'vvit@vedavyasa.org', 'principal@awhengg.org', 'citvcape@gmail.com', 'principal@geckkd.ac.in', 'sabiqclt@gmail.com', 'kmctcew@gmail.com', 'ceet@kmct.org', 'office@mdit.ac.in', 'gecwoffice@gmail.com', 'cetpayyanur@gmail.com', 'principal@cethalassery.ac.in', 'principal@gcek.ac.in', 'mit@anjarakandy.in', 'principal@sngcet.org', 'stthomaskannur@ktu.edu.in', 'office@vjec.ac.in', 'principal@cetkr.ac.in', 'principal@lbscek.ac.in'

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



