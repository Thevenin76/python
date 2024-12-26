courses_data = [
    ["01.12.2020", "HPC", "My Learning", "", "59973", "00:30", "Atos University", "", "English", "31.12.2020"],
    ["20.12.2001", "Digital Awareness Iberia Overall assesment", "My Learning", "", "59974", "", "00:30", "Atos University", "Spain", "Spanish", "20.12.1931"],
    ["01.12.2020", "Digital Awareness Iberia Overall assesment", "My Learning", "", "59974", "", "00:30", "Atos University", "", "English", "31.12.2020"],
    ["01.12.2020", "InformaciÃ³n adicional", "My Learning", "", "60048", "", "00:06", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "InformaciÃ³n adicional", "My Learning", "", "60048", "", "00:06", "Atos University", "Spain", "Spanish", "20.12.1930"],
    ["01.12.2020", "IntroducciÃ³n", "My Learning", "", "60049", "", "00:30", "Atos University", "", "English", "01.12.2020"],
    ["20.12.2001", "IntroducciÃ³n", "My Learning", "", "60049", "", "00:30", "Atos University", "", "English", "20.12.2001"],
    ["06.12.2021", "Atos Cybersecurity & Safety Awareness 2021", "My Learning", "", "62124", "", "0:45", "Atos University", "Spain", "English", "09.12.2021"],
    ["04.03.2021", "Atos Cybersecurity & Safety Awareness", "My Learning", "", "62124", "", "0:00", "Atos University", "", "English", "08.08.2017"],
    ["06.12.2021", "Atos Cybersecurity & Safety Awareness 2021", "My Learning", "", "62124", "", "0:00", "Atos University", "Spain", "Spanish", "08.06.2021"],
    ["26.11.2018", "New Data Protection Training (including GDPR)_ES", "My Learning", "", "A9S0017348", "", "0:00", "Atos University", "", "English", "26.11.2018"],
    ["15.01.2020", "Global B&PS items for all Directs", "My Learning", "", "B&PS_DIRECT", "", "0:00", "Atos University", "", "English", ".."],
    ["20.11.2017", "Global mandatory trainings curriculum", "My Learning", "", "INT_CERT_MAND", "", "0:00", "Atos University", "France", "English", "20.11.2017"],
    ["25.10.2021", "Global Mandatory EMS and GDPR Curriculum", "My Learning", "", "INT_CERT_MANDATORY", "", "0:00", "Atos University", "", "English", "25.10.2021"],
    ["01.04.2021", "Global Mandatory trainings curriculum 2021", "My Learning", "", "INT_CERT_MAND_2021", "", "00:00", "Atos University", "", "English", "08.06.2021"],
    ["15.02.2021", "Atos Iberia DAT Hybrid Cloud", "My Learning", "", "INT_CE_277", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["15.02.2021", "Atos Iberia DAT Codex", "My Learning", "", "INT_CE_278", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["15.02.2021", "Atos Iberia DAT Business Accelerators", "My Learning", "", "INT_CE_279", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["15.02.2021", "Atos Iberia DAT Ciberseguridad", "My Learning", "", "INT_CE_280", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["15.02.2021", "Atos Iberia DAT Digital Workplace", "My Learning", "", "INT_CE_281", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["15.02.2021", "Atos Iberia DAT Nuevos modelos gestión", "My Learning", "", "INT_CE_282", "", "00:00", "Atos University", "", "English", "15.02.2021"],
    ["20.12.2001", "Atos Iberia Digital Awareness Training", "My Learning", "", "INT_CE_283", "", "00:00", "Atos University", "Spain", "Spanish", "20.12.1931"],
    ["01.12.2020", "Atos Iberia Digital Awareness Training", "My Learning", "", "INT_CE_283", "", "00:00", "Atos University", "", "English", "31.12.2020"],
    ["20.11.2017", "Security and Safety awareness", "My Learning", "", "MIG_00028023", "", "0:49", "Atos University", "France", "English", "08.08.2017"],
    ["20.11.2017", "Atos Data protection", "My Learning", "", "MIG_00028795", "", "0:45", "Atos University", "France", "English", "19.08.2017"],
    ["20.11.2017", "Customer Experience", "My Learning", "", "MIG_00029495", "", "0:40", "Atos University", "France", "English", "20.08.2017"],
    ["22.08.2017", "Creating Value for our Clients", "My Learning", "", "MIG_00058634", "", "1:00", "Atos University", "France", "English", "22.08.2017"],
    ["02.08.2021", "Code of Ethics 2021", "My Learning", "", "MIG_00065818", "", "1:00", "Atos University", "Spain", "Spanish", "09.12.2021"],
    ["20.11.2017", "Code of Ethics", "My Learning", "", "MIG_00065818", "", "0:45", "Atos University", "France", "English", "20.08.2017"],
    ["22.08.2017", "Introduction to Atos Lean", "My Learning", "", "MIG_00068418", "", "1:00", "Atos University", "France", "English", "22.08.2017"],
    ["03.04.2018", "Beginner Git", "My Learning", "", "sd_gitf_a01_it_enus", "", "1:58", "Atos University", "France", "English", "03.04.2018"],
    ["06.06.2018", "Advanced Git", "My Learning", "", "sd_gitf_a02_it_enus", "", "2:40", "Atos University", "", "English", "06.06.2018"],
    ["23.08.2017", "Introduction to OWASP and the Top 10", "My Learning", "", "sp_owsp_a01_it_enus", "", "1:31", "Atos University", "France", "English", "23.08.2017"],
    ["20.12.2001", "DWP", "My Learning", "", "59972", "", "00:30", "Atos University", "Spain", "Spanish", "20.12.1931"],
    ["31.12.2020", "Automation Overview", "My Learning", "", "19321", "", "00:45", "Atos University", "", "English", "31.12.2020"],
    ["20.12.1931", "Automation Overview", "My Learning", "", "19321", "", "00:45", "Atos University", "", "English", "20.12.1931"],
    ["21.08.2017", "Atos Agile Awareness Level 1 Certification", "My Learning", "", "364", "", "1:00", "Atos University", "France", "English", "21.08.2017"],
    ["06.11.2018", "Oracle Cloud Road Map & Business Updates", "My Learning", "", "4469", "", "0:40", "Atos University", "", "English", "06.11.2018"],
    ["20.12.2001", "Cloud Computing", "My Learning", "", "59936", "", "00:30", "Atos University", "", "English", "20.12.2001"],
    ["02.03.2021", "Cloud Computing", "My Learning", "", "59936", "", "00:00", "Atos University", "", "English", "01.12.2020"],
    ["20.12.2001", "Nuevas Arquitecturas", "My Learning", "", "59956", "", "00:30", "Atos University", "", "English", "20.12.2001"],
    ["02.03.2021", "Nuevas Arquitecturas", "My Learning", "", "59956", "", "00:00", "Atos University", "", "English", "01.12.2020"],
    ["01.12.2020", "Big Data & Analytics", "My Learning", "", "59957", "", "00:30", "Atos University", "", "English", "01.12.2020"],
    ["01.12.2020", "IoT", "My Learning", "", "59958", "", "00:30", "Atos University", "", "English", "01.12.2020"],
    ["20.12.2001", "IoT", "My Learning", "", "59958", "", "00:30", "Atos University", "", "English", "20.12.2001"],
    ["01.12.2020", "IA", "My Learning", "", "59959", "", "00:30", "Atos University", "", "English", "29.12.2020"],
    ["01.12.2020", "Smart Assistant", "My Learning", "", "59960", "", "00:30", "Atos University", "", "English", "29.12.2020"],
    ["01.12.2020", "Automation-RPA", "My Learning", "", "59961", "", "00:30", "Atos University", "", "English", "29.12.2020"],
    ["20.12.2001", "Blockchain", "My Learning", "", "59962", "", "00:30", "Atos University", "Spain", "Spanish", "20.12.1930"],
    ["01.12.2020", "Blockchain", "My Learning", "", "59962", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["01.12.2020", "DWP", "My Learning", "", "59972", "", "00:30", "Atos University", "", "English", "31.12.2020"],
    ["20.12.2001", "Management 3.0", "My Learning", "", "59971", "", "00:30", "Atos University", "Spain", "Spanish", "20.12.1931"],
    ["01.12.2020", "Management 3.0", "My Learning", "", "59971", "", "00:30", "Atos University", "", "English", "31.12.2020"],
    ["02.03.2021", "DevOps", "My Learning", "", "59970", "", "00:00", "Atos University", "", "English", "30.12.2021"],
    ["20.12.2001", "DevOps", "My Learning", "", "59970", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "DevOps", "My Learning", "", "59970", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "Metodologías Agile", "My Learning", "", "59968", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "Metodologías Agile", "My Learning", "", "59968", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "Design Thinking & Lean Startup", "My Learning", "", "59967", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "Design Thinking & Lean Startup", "My Learning", "", "59967", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "Ciberseguridad", "My Learning", "", "59966", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "Ciberseguridad", "My Learning", "", "59966", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "SAP", "My Learning", "", "59965", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "SAP", "My Learning", "", "59965", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["20.12.2001", "Salesforce", "My Learning", "", "59963", "", "00:30", "Atos University", "", "English", "20.12.1930"],
    ["01.12.2020", "Salesforce", "My Learning", "", "59963", "", "00:30", "Atos University", "", "English", "30.12.2020"],
    ["14.09.2003", "PROGRAMACION WEB", "MPP", "", "", "400:00", "CIBERAULA", "Spain", "English", "14.04.2004"],
    ["23.08.2017", "Introduction to OWASP and the Top 10", "MPP", "", "", "1:52", "Institute OSWAP", "Spain", "English", "23.08.2017"],
    ["15.06.2005", "Forum about data protection and managment", "MPP", "", "", "2:00", "FEMETE", "Spain", "English", "15.06.2005"],
    ["01.06.2019", "Spring MVC", "MPP", "", "", "11:00", "Udemy", "Spain", "English", "30.06.2019"],
    ["01.05.2022", "Seguridad Web Informática", "MPP", "", "", "0000:00", "HackTheBox Academy", "Spain", "English", "02.06.2022"],
    ["01.05.2022", "HackThebox Starting Point", "MPP", "", "", "0000:00", "HackThebox Starting Point", "Spain", "English", "02.06.2022"],
    ["21.12.2019", "Docker Crash Course for busy DevOps a", "MPP", "", "", "0000:00", "Udemy", "Spain", "English", "29.12.2019"],
    ["14.09.2003", "WEB PROGRAMMING", "MPP", "", "", "400:00", "CIBERAULA", "Spain", "English", "14.04.2004"],
    ["08.08.2017", "Security and Safety awareness", "MPP", "", "00028023", "", "1:00", "ATOS", "Spain", "English", "08.09.2017"],
    ["19.09.2016", "Atos Data protection", "MPP", "", "00028795", "", "1:00", "ATOS", "Spain", "English", "19.09.2016"],
    ["20.08.2017", "Customer Experience", "MPP", "", "00029495", "", "1:00", "ATOS", "Spain", "English", "20.08.2017"],
    ["22.08.2017", "Creating Value for our Clientes", "MPP", "", "00058634", "", "1:00", "ATOS", "Spain", "English", "22.08.2017"],
    ["20.08.2017", "Code of Ethics", "MPP", "", "00065818", "", "1:00", "ATOS", "Spain", "English", "20.08.2017


# Función para buscar cursos
def find_courses(courses):
    course_ids = {}
    
    # Crear un diccionario para los cursos
    for course in courses:
        course_id = course[3]
        language = course[7]
        if course_id not in course_ids:
            course_ids[course_id] = set()
        course_ids[course_id].add(language)

    return course_ids

# Función para verificar cursos
def check_courses(course_ids):
    for course_id, languages in course_ids.items():
        if 'Spanish' not in languages or 'English' not in languages:
            print(f"El curso con ID {course_id} falta en el idioma(s):")
            if 'Spanish' not in languages:
                print(" - Español")
            if 'English' not in languages:
                print(" - Inglés")

            # Confirmación para agregar el curso
            confirm = input(f"¿Quieres agregar el curso con ID {course_id} en estos idiomas? (y/n): ")
            if confirm.lower() == 'y':
                print(f"Curso {course_id} agregado en los idiomas faltantes.\n")

# Ejecutar el programa
course_ids = find_courses(courses_data)
check_courses(course_ids)
