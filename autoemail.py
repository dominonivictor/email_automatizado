import smtplib
import email.utils
import config

def enviar_email(assunto, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.ENDERECO_EMAIL, config.SENHA)
        message = 'Subject: {}\n\n{}'.format(assunto, msg)
        server.sendmail(config.ENDERECO_EMAIL, config.ENDERECO_EMAIL, message)
        server.quit()
        print("Sucesso: Email sent!")
    except:
        print('Error, something failed')
        
assunto = "Assunto teste"

msg = '''Suspendisse dui est, faucibus non ante id, elementum euismod orci. 
Ut ac ullamcorper mauris. Sed nec lectus ullamcorper, vehicula felis ut, bibendum ex. In ut tincidunt felis, 
ac volutpat nisl. Vivamus euismod, mi luctus congue porttitor, sapien ligula condimentum eros, vehicula mollis 
velit leo et sem. Sed eu dictum sem, eget euismod lorem. Quisque sit amet tempus lectus. Vivamus eleifend, 
arcu non pretium cursus, urna metus pellentesque lorem, id volutpat risus velit fringilla arcu. Donec dapibus 
lorem nisi, at fringilla dui aliquet id. Ut commodo, augue a lacinia commodo, quam erat egestas velit, et maximus 
orci nulla sit amet ante. Duis vehicula tempus purus, a tincidunt ipsum sollicitudin nec. In hac habitasse platea dictumst.
Vivamus sed lorem eu nisl consectetur euismod. Proin et faucibus mi, ut facilisis libero.

Etiam nec sem id neque egestas tempor. Duis euismod convallis dui, gravida convallis enim lacinia vitae. Vivamus quis arcu 
eget sapien eleifend rhoncus. Nullam sodales, leo sed bibendum semper, sapien purus placerat erat, id egestas velit nisi et sem. 
Pellentesque faucibus massa sit amet sagittis ullamcorper. Fusce posuere justo sit amet magna pulvinar, eget tincidunt 
elit congue. Morbi finibus mauris vel ante fermentum, nec vestibulum metus tristique. Cras egestas facilisis nisl sed cursus.
Vestibulum non ipsum sit amet sem sodales gravida nec vitae libero. Aenean sodales turpis vel neque laoreet aliquet eget 
quis urna. Phasellus in lobortis turpis, in viverra metus. 

Sed auctor commodo ante, vitae placerat libero tincidunt tincidunt.
Phasellus at lectus malesuada, egestas neque non, consequat nulla. Nulla et sapien quis arcu finibus hendrerit non eu orci. 
Aenean dignissim consequat diam, sollicitudin sollicitudin ante ultricies a. Nulla nec nunc purus. Sed consectetur libero 
at erat interdum, eget tempor dolor semper. Sed ac volutpat lectus. Class aptent taciti sociosqu ad litora torquent per 
conubia nostra, per inceptos himenaeos. Morbi bibendum erat non ante consectetur, elementum facilisis mi sodales.'''

enviar_email(assunto, msg)