from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define rules for the chatbot
rules = [
     # Greetings
    (r'.*(ram).*', ['Jai Shree Ram']),
    (r'.*(hello|hi|hey).*', ['Hello!', 'Hi there!', 'Hey!']),

    #about mandsaur
    (r'.*(mandsaur|reach|come).*', ['''Mandsaur is a town in the Malwa region of Madhya Pradesh state in Central India.<br>
    It lies between the parallels of latitude 24.03° North , 75.08° East, and between the meridians of longitude 740 42′ 30″ East and 750 50′ 20″ East.<br>
    It is rich in its archeological and historical heritage, most famous for its unique Pashupatinath Temple, second only to the one at Kathmandu, Nepal.<br>
    Mandsaur is also one of the largest producers of opium in the world.''']),

    (r'.*(train).*', ['''Mandsaur railway station is a main railway station in Mandsaur city of Madhya Pradesh. Its code is MDS.<br> Mandsaur is an important broad gauge railway station of the Ajmer — Ratlam line. Mandsaur is well connected to Ratlam, Ujjain via Nagda and Kota & Bundi in Rajasthan via Chittorgarh. <br> 
                      The major trains passing from Mandsaur are:
    <br>Bandra Terminus – Ajmer /Udaipur Express
    <br>Indore–Udaipur City Express
    <br>Jaipur-Bhopal Express
    <br>Ajmer- Kolkata Express
    <br>Ajmer- Hyderabad Express
    <br>Ratlam-Ajmer Express
    <br>Ratlam- Chittaurgarh Express
    <br>Ratlam- Agra Fort Express
    <br>Chittaurgarh- Ratlam DMU
    <br>Nathdwara- Okha Express
    <br>Mandsaur- Meerut City Link (Dehradun) Express''']),

    (r'.*(heritage|tourist).*', ['''
    Heritage Sites worth Visiting at Mandsaur : Pashupatinath Temple , Bandi ji ka Baag , <br>
    Shree Bahi Parshwanath Digambar Jain Atishaya Kshetra , Mandsaur Fort , Shri Khade Balaji Temple , Gandhi Sagar Sanctuary
    ''']),

    # Questions about the college
    #about
    (r'.*(college|university).*', ['''Our college is known for its excellent faculty and state-of-the-art facilities.<br> 
                                    We offer a wide range of programs and opportunities for students. <br>
                                    You can find more information on our website: <a href="https://www.meu.edu.in/">https://www.meu.edu.in/ </a> ''']),

    #clubs
    (r'.*(clubs|activities).*', ['''Students clubs provide a forum for interaction among themselves and the outside world events .<br>
     Different types of clubs are available in the university related to technology , health , arts , sports and many more.<br>
     More details availabel at <a href="https://www.meu.edu.in/club-activity/"> https://www.meu.edu.in/club-activity/ </a>.
    ''']),
    (r'.*(events).*', [''' Many events are organised by the university , department and students during the whole year.
    one of the cultural event is SPANDAN , and sports event is RIVALRY.
    ''']),


    #courses
    (r'.*(course|program).*', ['We offer various undergraduate and graduate programs in fields such as Computer Science, Engineering, Business, Biology and more. <br> You can explore our programs on our website: <a href="https://www.meu.edu.in/">https://www.meu.edu.in/ </a>']),
    (r'.*(diploma).*', ['We offer various Diploma in fields such as Pharmacy, Mechanical, Electrical and Civil. <br> You can explore our Diploma course on: <a href="https://www.meu.edu.in/diploma-courses-2/"> https://www.meu.edu.in/diploma-courses-2/ </a> ']),
    (r'.*(undergraduate|bachelor).*', ['We offer various undergraduate programs in fields such as  <br> B.Tech , BCA ,BBA , B.Pharm , B.Sc. ,B.A. , B.E.d , B.P.Ed , B.Lib , B.Com. <br> You can explore these programs on: <a href="https://www.meu.edu.in/graduate-courses/">https://www.meu.edu.in/graduate-courses/ </a>']),
    (r'.*(graduate|master).*', ['Our University offers various graduate courses such as <br> MBA , MCA , M.Pharma , M.Sc. , M.Tech , M.Lib.Sc , M.A. <br> To know more please visit: <a href="https://www.meu.edu.in/post-graduate-courses/">https://www.meu.edu.in/post-graduate-courses/ </a>']),
    (r'.*(phd|ph.d).*', ['Our University also provides Ph.D . <br>To know more please visit: <a href="https://www.meu.edu.in/ph-d-entrance-exam/ ">https://www.meu.edu.in/ph-d-entrance-exam/  </a>']),

    #admission
    (r'.*(admission|apply).*', ['For admission inquiries, you can contact our admissions office or visit our website for more information about the application process and requirements visit: <a href="https://erp.meu.edu.in/anon_studentAdmissionEnquiry.htm"> https://erp.meu.edu.in/anon_studentAdmissionEnquiry.htm </a> ']),

    #scholarship
    (r'.*(scolarship).*', ['''Scholarships are offered by colleges, the government, some private organizations and individual charities.
    It is a better  to apply for multiple scholarships at the same time and increase the chances of wining one.<br> The Ministry offers National as well as External Scholarships to the needy students.
    For more details check : https://www.meu.edu.in/scholarships-aids/''']),

    # Campus facilities
    (r'.*(facilities|facility).*', ['''Our campus offers a variety of facilities including Libraries, Laboratories, Student accommodation, <br> Sports facilities, Bus transportation, Gymnasium for health and fitness, Food Courts and Banking facility. <br> Check more campus facilities at: <a href='https://www.meu.edu.in/residential-facility-2/'>https://www.meu.edu.in/residential-facility-2/ </a>''']),
    #bus
    (r'.*(bus).*', ['''We offer Bus transportation at various cities such as Neemuch , Malahrgarh , Manasa, Jaora , Suwasra , Daloda , Pipliya , Dodhar , Pipliya''']),
    

    #juno / student portl
    (r'.*(juno|portal).*', ["Here is the link to login at Universitys' student portal : <a href='https://erp.meu.edu.in/login.htm'> https://www.meu.edu.in/login.htm </a><br>"]),

    # Default response
    (r'.*(contact).*', ["""Here is the contact details
    Website : <a href='https://www.meu.edu.in/'> https://www.meu.edu.in/ </a><br>
    Mail : admissions@meu.edu.in <br>
    Admissio Cell :9424489426 <br>
    Reception:9752122999 <br>
    Address : Mandsaur University By Pass Square, Revas Devda Road, S.H.-31, Mandsaur (M.P) -458001 <br>"""]),

    # Default response
    (r'(.*)', ["""I'm sorry, I'm just a simple chatbot. For more detailed information, Here is the contact details
    Website : <a href='https://www.meu.edu.in/'> https://www.meu.edu.in/ </a><br>
    Mail : admissions@meu.edu.in <br>
    Admissio Cell :9424489426 <br>
    Reception:9752122999 <br>
    Address : Mandsaur University By Pass Square, Revas Devda Road, S.H.-31, Mandsaur (M.P) -458001 <br>"""]),
]

# Create the chatbot
college_chatbot = Chat(rules, reflections)

@app.route('/')
def index():
    # Return the content of index.html
    return open('index.html').read()

@app.route('/chat', methods=['POST'])
def chat():
    # Handle POST requests to the /chat endpoint
    user_message = request.json.get('message')
    # Process user's message and generate bot's response
    bot_response = process_user_message(user_message)
    return jsonify({'response': bot_response})

def process_user_message(user_message):
    # Your logic to process user's message and generate bot's response
    # This function should contain the logic of your chatbot
    # For example, you can use NLTK or other libraries to generate responses
    # return "Bot response to user's message: " + user_message
    #print("Hello! I'm your college chatbot. How can I assist you today? (Type 'quit' to exit)")
    # college_chatbot.converse()
    user_input = user_message
    if user_input.lower() in ['quit', 'exit']:
        return "Goodbye!"
        
    else:
        response = college_chatbot.respond(user_input)
        return response


if __name__ == '__main__':
    app.run(debug=True)
