import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("mainpage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/projects.py", label="Projects", icon="💻")
    bar4.page_link("pages/contacts.py", label="Contacts", icon="🌏")
    st.write("")

def footer():
    st.markdown("""
    <style>
        .footer {
            position: relative;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }
    </style>
    <div class="footer">
       Designed & inspired by <a href="https://github.com/Rsirp0c/portfolio" target="_blank">Haoran Cheng</a>. <br>
        Customized & rebuilt by me.
    </div>
""", unsafe_allow_html=True)


#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Hi, my name’s Tuan, aka Meotism. I’m a Software Developer with 3+ years of experience building scalable backend web apps using Python, Go and C#. \
                    My passion lies in developing applications for a large user base and enhancing the user experience to ensure easy access and smooth usage. \
                        I was evaluated by everyone around me as a responsible person and persistently completed the assigned tasks. I’m always eager to learn new technologies and languages and can quickly adapt to them. \
                            Besides, I have written blogs at [Dev Community](https://dev.to/meotism)
              """,
        "title":"Software Developer",
        'fullname':'Tran Ngoc Tuan', 
        'study':'Ho Chi Minh City University of Science',
        'location':'HCMC, VietNam',
        'interest':'Reading news, books, and IT blogs along with cooking and playing sports such as badminton, football, ping pong, etc',
        'skills':['Python','Go','C#','Docker Compose','bash','Figma',
                  'Microservices','Monolithic','Console','uWSGI','nginx','MongoDB',
                  'PostgreSQL','MySQL','mqtt','Crontab','Git','SSO','flask','Unix',
                  'Webhook', 'Sentry','Redis','Swagger','RESTfulAPI'],
        }
# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [[":green[Metadoc] | Healthcare Platform", "Software Engineer",  "FPT Software",
              "March 2023 – Ferbuary 2025", "HCMC, VN",  
              """  
              - :grey[**Description:**] The project has a duty to bring healthcare to every home including urban and remote areas and that is a Family Doctor Program  
              - :grey[**Responsibilities:**] I was responsible for handling some services such as: live chat service, telehealth service, third-party service, chatbot service, newsfeed service, notification service, internal request service,...Moreover, I used JavaScript to support Frontend configuration and run push notification, process the task of recording the appointment. Specifically, I mention technical tasks, such as coding, debugging, designing architecture, optimizing performance, writing technical documents, researching new technology, etc. I collaborate with the team to describe any collaborative aspects such as agile methodologies, sprint planning or cross-functional team coordination and clarify the required use cases
              - :grey[**Technologies:**] Python, Flask, mqtt, Redis, nginx, consult, uWSGI, NodeJS, MongoDB, Webhook, SSO, PostgreSQL, Gitlab, Firebase, Docker, Docker Compose, S3, Crontab
              """,  
            "https://metadoc.vn/",
            "https://apps.apple.com/vn/app/metadoc/id6446609399",
            "https://play.google.com/store/apps/details?id=com.fpt.metadoc"],
            [":orange[Medipathy] | Healthcare Management", "Backend Developer", "Executionlab.asia",
              "June 2022 – March 2023", "HCMC, VN", 
              """
              - :grey[**Description:**] The project Assistance in assignment management and employee work, widely notified and easy communication, optimize the management process of clinics and hospitals more effectively
              - :grey[**Responsibilities:**] Collaborate with teammates and communicate with clients to clarify business use case, develop the frameworks and modules of the system. Prepare documents and technical guide for new developers joining the team
              - :grey[**Technologies:**] Go, Sentry, Firebase, Redis, SMTP, Swagger, MySQL, Github, Docker, Docker Compose, bash, S3, Crontab
              """,
             "https://medipathy.doctorsfile.jp/",
            "https://apps.apple.com/vn/app/metadoc/id6446609399",
            "https://play.google.com/store/apps/details?id=jp.doctorsfile.medipathy"],
              [":blue[Paynetvn] | E-wallet Startup", "Database Administrator Intern", "Paynetvn",
              "May 2023 – Sep 2023", "Hangzhou, China", 
              """
              - :grey[**Description:**] The project is a startup that provides a secure and convenient way to pay for goods and services online
              - :grey[**Responsibilities:**] Migrated data application from MSSQL to Oracle database and wrote procedures and triggers following requirements workflow. Wrote scripts and generated test data using Mockaroo and tested by Postman
              - :grey[**Technologies:**] Oracle, Mockaroo, Postman, MSSQL
              """,
             "https://business.paynetvn.com/",
            "http://paynetvn.com/",
            "http://paynetvn.com/"]
              ]      

# Projects --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Projects = { 1:[":blue[Phi's] | Chatbot Assistant Website",
              """
             :grey[**Technologies:**] Python, Streamlit, Hugging Face, SpeechRecognition, TOML
              """],
              2:[":orange[Review University] | Website rating of universities in Vietnam",
                """
                :grey[**Technologies:**] Python, flask, Machine Learning, beautiful soup, Project Jupiter
                """],
              3:[':green[Swiftlet’s Nest Anh Xuan] | Advertising website',
            """
            :grey[**Technologies:**] wordpress, cpanel, DNS, LAMP server, design UI/content
            """],
              4:[":red[Jisti's] | Video Conference meeting",
            """
            :grey[**Technologies:**] Jitsi open source, EC2, certbot, crontab, bash, duckdns, https
            """],
              5:[':blue[Meotism] | My portfolio',  
            """
            :grey[**Technologies:**] Python, Streamlit, html, css
            """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "935724391"
email = "tranngoctuan391@gmail.com"
linkedin_link = "www.linkedin.com/in/meotism"
github_link = "https://github.com/meotism"

