import requests
# import imaplib
# import smtplib

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.header import decode_header
# from email.utils import make_msgid
from settings.configurations import DefaultConfig




class EmailClient:
	def __init__(self, config: DefaultConfig, mailbox = 'inbox') -> None:
	    self.config = config
	    self.mailbox = mailbox
	    self.api_uri = "https://api.elasticemail.com/v2"


	def build_request(self, method, url, data):
		data['apikey'] = self.config.STMP_API_KEY
		if method == 'POST':
			result = requests.post(self.api_uri + url, data = data)
		
		elif method == 'PUT':
			result = requests.put(self.api_uri + url, data = data)
		
		elif method == 'GET':
			attach = ''
			for key in data:
				attach = attach + key + '=' + data[key] + '&' 
			url = url + '?' + attach[:-1]
			result = requests.get(self.api_uri + url)	
			
		ans = result.json()
		
		if ans['success'] is False:
			return ans['error']
			
		return ans['data']


	def reply(self,  to: str, message_id: str, subject: str, message_text: str, isTransactional=True) -> None:
		data = {
			'subject': subject,
			'from': self.config.FROM_EMAIL,
			'fromName': "Support",
			'to': to,
			'bodyHtml': message_text,
			# 'bodyText': message_text,
			'isTransactional': isTransactional
		}
		
		ans = self.build_request(
			method='POST', 
			url='/email/send', 
			data=data
		)

		print("============================")
		print("Email enviado com sucesso!")
		print(ans)
		print("============================")



# class EmailClient:
#     def __init__(self, config: DefaultConfig, mailbox = 'inbox') -> None:
#         self.config = config
#         self.mailbox = mailbox

#         self.imap = imaplib.IMAP4_SSL(host=config.IMAP_SERVER)
#         self.imap.login(user=config.FROM_EMAIL, password=config.FROM_PWD)

   
#     def _create_message(self, to: str, message_id:str,  subject: str, message_text: str) -> MIMEMultipart:
#         message = MIMEMultipart()
#         message['Message-ID'] = make_msgid()
#         # message['In-Reply-To'] = message_id
#         message['References'] = message_id
#         message['From'] = self.config.FROM_EMAIL
#         message['To'] = to
#         message['Subject'] = subject

#         # html_default_ans = Answer(message_text)
#         # html = html_default_ans.botAnswer()
#         # footer = html_default_ans.footer()
#         # message.attach(MIMEText(html, 'html'))
#         # message.attach(MIMEText(footer, 'html'))      
        
#         message.attach(MIMEText(message_text, 'plain'))
#         return message


#     def reply(self, to: str, message_id: str, subject: str, message_text: str) -> None:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login(self.config.FROM_EMAIL, self.config.FROM_PWD)
    
#         message = self._create_message(
#             to=to, 
#             message_id=message_id, 
#             subject=subject, 
#             message_text=message_text
#         ).as_string()

#         server.sendmail(self.config.FROM_EMAIL, to, message)
#         server.quit()

#         print("\nEmail enviado!\n")


'''
tela de resetar senha no app (dois botões):
    1. solicitar reset de senha
        a. será enviado um hash para o email cadastrado (tempo ativo: 10 min)
            {
                'request_reset_password': bool
                'hash_reset_password'   : str
                'time_request'          : datetime 
            }
    2. já possuo o codigo de renovação
        a. o usuario copia esse hash e cola na tela de resetar senha
        b. o hash será validado pela api
            caso success: mostar a tela de redefinição de senha
            caso fail: mostrar mensagem de erro
'''

