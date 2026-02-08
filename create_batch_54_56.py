
import json

data = [
    # Page 54 - Chapter 19: Sectors of the Indian Economy (Continued)
    {
        "Chapter": "19",
        "Questions type": "Short Answer",
        "Question in English": "Write a brief note on the National Rural Employment Guarantee Act 2005.",
        "Question in Hindi": "राष्ट्रीय ग्रामीण रोजगार गारंटी अधिनियम 2005 पर संक्षिप्त टिप्पणी कीजिये-",
        "Answer in English": "The central government enacted a law implementing the Right to Work in about 625 districts of India. It is called the Mahatma Gandhi National Rural Employment Guarantee Act 2005. Under this, all those who are able to, and are in need of work in rural areas are guaranteed 100 days of employment in a year by the government. If the government fails in its duty to provide employment, it will give unemployment allowances to the people. The types of work that would in future help to increase the production from land will be given preference under the Act.",
        "Answer in Hindi": "केन्द्र सरकार द्वारा रोजगार सृजन हेतु चलाया गया एक महत्त्वपूर्ण कार्यक्रम है अन्तर्गत उन सभी लोगो, जो काम करने में सक्षम हैं और जिन्हें काम की जरूरत है को सरकार द्वारा ग्रामीण क्षेत्रों मे वर्ष में 100 दिन के रोजगार की गारंटी दी गई है। यदि सरकार रोजगार उपलब्ध कराने में असफल रहती है तो वह लोगों को बेरोजगारी भत्ता देगी। इसके अन्तर्गत उन कामों को वरीयता दी जायेगी, जिनसे भविष्य में भूमि से उत्पादन बढ़ाने में मदद मिलेगी।",
        "Marks": "3"
    },
    {
        "Chapter": "19",
        "Questions type": "Short Answer",
        "Question in English": "Clarify the difference between Public Sector and Private Sector.",
        "Question in Hindi": "सार्वजनिक क्षेत्रक एवं निजी क्षेत्रक में अन्तर स्पष्ट कीजिये।",
        "Answer in English": "In the public sector, the government owns most of the assets and provides all the services. In the private sector, ownership of assets and delivery of services is in the hands of private individuals or companies. Railways or Post Office is an example of the public sector whereas companies like Tata Iron and Steel Company Limited (TISCO) or Reliance Industries Limited (RIL) are privately owned.",
        "Answer in Hindi": "सार्वजनिक क्षेत्रक में अधिकांश परिसपत्तियों पर सरकार का स्वामित्त्व होता है और सरकार ही सभी सेवाएँ उपलब्ध कराती है। निजी क्षेत्रक में परिसंपत्तियों पर स्वामित्त्व और सेवाओं के वितरण की जिम्मेदारी एकल व्यक्ति या कम्पनी के हाथों में होता है। रेलवे तथा डाकघर सार्वजनिक क्षेत्रक के उदाहरण है तथा टिस्को एवं रिलायंस इण्डस्ट्रीज लिमिटेड जैसी कम्पनियाँ निजी स्वामित्त्व में है।",
        "Marks": "3"
    },

    # Page 55 - Chapter 20: Money and Credit
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Which of the following is a form of modern money?",
        "Question in Hindi": "निम्न में से कौनसा आधुनिक मुद्रा का रूप है?",
        "Answer in English": "(a) Paper notes",
        "Answer in Hindi": "(अ) कागज के नोट",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Who issues currency notes in India?",
        "Question in Hindi": "भारत में करेंसी नोट कौन जारी करता है?",
        "Answer in English": "(b) Reserve Bank of India",
        "Answer in Hindi": "(ब) रिजर्व बैंक ऑफ इंडिया",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Which of the following is not included in formal sources of credit?",
        "Question in Hindi": "निम्न में से साख के औपचारिक स्रोतों में शामिल नहीं है-",
        "Answer in English": "(c) Employer",
        "Answer in Hindi": "(स) नियुक्ता",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Moneylenders, traders, employees, relatives and friends etc. are included in which type of credit source?",
        "Question in Hindi": "साहूकार, व्यापारी, कर्मचारी, रिश्तेदार तथा मित्र आदि साख के किस प्रकार के स्रोत में शामिल हैं?",
        "Answer in English": "(b) Informal",
        "Answer in Hindi": "(ब) अनौपचारिक",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Most decisions regarding savings and loans in Self Help Groups are taken by-",
        "Question in Hindi": "स्वयं सहायता समूह में बचत और ऋण संबंधित अधिकतर निर्णय लिए जाते हैं-",
        "Answer in English": "(b) By Members",
        "Answer in Hindi": "(ब) सदस्यों द्वारा",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "When was the Grameen Bank of Bangladesh established?",
        "Question in Hindi": "बांग्लादेश के ग्रामीण बैंक की स्थापना कब हुई?",
        "Answer in English": "(b) 1970",
        "Answer in Hindi": "(ब) 1970",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Who monitors the functioning of formal sources of credit?",
        "Question in Hindi": "ऋण के औपचारिक स्रोतों की कार्यप्रणाली पर नजर कौन रखता है?",
        "Answer in English": "(b) Reserve Bank of India",
        "Answer in Hindi": "(ब) रिजर्व बैंक ऑफ इंडिया",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Essential in barter system is-",
        "Question in Hindi": "वस्तु विनिमय प्रणाली में आवश्यक है-",
        "Answer in English": "(a) Double coincidence of wants",
        "Answer in Hindi": "(अ) आवश्यकताओं का दुहरा संयोग",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "MCQ",
        "Question in English": "Major function of money is-",
        "Question in Hindi": "मुद्रा का प्रमुख कार्य है-",
        "Answer in English": "(d) All of the above",
        "Answer in Hindi": "(द) उपरोक्त सभी",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "What is meant by Barter System?",
        "Question in Hindi": "वस्तु विनिमय प्रणाली किसे कहते हैं?",
        "Answer in English": "A system where goods are directly exchanged without the use of money.",
        "Answer in Hindi": "वह प्रणाली जिसमें मुद्रा का उपयोग किए बिना वस्तुओं का सीधा आदान-प्रदान होता है।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "Define Money.",
        "Question in Hindi": "मुद्रा को परिभाषित कीजिए।",
        "Answer in English": "Money is anything that is generally accepted as a medium of exchange, a measure of value, and a store of value.",
        "Answer in Hindi": "मुद्रा वह है जो विनिमय के माध्यम, मूल्य के मापक और मूल्य के संचय के रूप में स्वीकार की जाती है।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "Who has accepted the Indian Rupee (currency) as a medium of exchange?",
        "Question in Hindi": "भारतीय रुपये (करेंसी) को विनिमय का माध्यम किसने स्वीकार किया है?",
        "Answer in English": "The Government of India / Reserve Bank of India.",
        "Answer in Hindi": "भारत सरकार ने / रिजर्व बैंक ऑफ इंडिया ने।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "Bank deposits are that part of money which-",
        "Question in Hindi": "बैंक निक्षेप (जमा) धन का वह हिस्सा है जिसे-",
        "Answer in English": "People deposit in banks.",
        "Answer in Hindi": "लोग बैंकों में जमा करते हैं।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "What is a Check?",
        "Question in Hindi": "चैक (Check) क्या है?",
        "Answer in English": "A paper instructing the bank to pay a specific amount from the person's account to the person in whose name the check has been issued.",
        "Answer in Hindi": "एक ऐसा कागज जो बैंक को किसी व्यक्ति के खाते से चैक पर लिखे नाम के किसी दूसरे व्यक्ति को एक खास रकम का भुगतान करने का आदेश देता है।",
        "Marks": "1"
    },

    # Page 56 - Chapter 20: Money and Credit (Continued)
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "What is meant by Credit (Loan)?",
        "Question in Hindi": "साख (ऋण) से क्या आशय है?",
        "Answer in English": "It refers to an agreement in which the lender supplies the borrower with money, goods or services in return for the promise of future payment.",
        "Answer in Hindi": "साख (ऋण) से आशय एक सहमति से है जहाँ साहूकार कर्जदार को धन, वस्तु या सेवाएँ उपलब्ध कराता है और बदले में भविष्य में कर्जदार से भुगतान का वादा लेता है।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Very Short",
        "Question in English": "What is Collateral?",
        "Question in Hindi": "समर्थक ऋणाधार क्या है?",
        "Answer in English": "It is an asset that the borrower owns (such as land, building, vehicle, livestocks, deposits with banks) and uses this as a guarantee to a lender until the loan is repaid.",
        "Answer in Hindi": "समर्थक ऋणाधार ऐसी संपत्ति है जिसका मालिक कर्जदार है (जैसे कि भूमि, इमारत, गाड़ी, पशु, बैंकों में पूँजी) और इसका इस्तेमाल वह उधारदाता को गारंटी देने के रूप में करता है जब तक कि ऋण का भुगतान नहीं हो जाता।",
        "Marks": "1"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "Mention the major functions of money.",
        "Question in Hindi": "मुद्रा के प्रमुख कार्यों का उल्लेख कीजिये।",
        "Answer in English": "1. Medium of exchange, 2. Measure of value, 3. Store of value, 4. Standard of deferred payments.",
        "Answer in Hindi": "1. विनिमय का माध्यम, 2. मूल्य का मापक, 3. मूल्य का संचय, 4. स्थगित भुगतानों का मान।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "What do you understand by 'Double Coincidence of Wants'?",
        "Question in Hindi": "'आवश्यकताओं के दोहरे संयोग' से आप क्या समझते हैं?",
        "Answer in English": "What a person desires to sell is exactly what the other wishes to buy. In a barter system where goods are directly exchanged without the use of money, double coincidence of wants is an essential feature.",
        "Answer in Hindi": "जब दोनों पक्ष एक दूसरे से चीजें खरीदने और बेचने पर सहमति रखते हैं, तो इसे आवश्यकताओं का दोहरा संयोग कहा जाता है। एक व्यक्ति जो वस्तु बेचने की इच्छा रखता है, वही वस्तु दूसरा व्यक्ति खरीदने की इच्छा रखता हो।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "State any two functions of a bank.",
        "Question in Hindi": "बैंक के कोई दो कार्य बताइये।",
        "Answer in English": "1. Accepting deposits from the public. 2. Granting loans to the public.",
        "Answer in Hindi": "1. जनता से जमा स्वीकार करना। 2. जनता को ऋण प्रदान करना।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "Write any two functions of the Reserve Bank of India.",
        "Question in Hindi": "भारतीय रिजर्व बैंक के कोई दो कार्य लिखिए।",
        "Answer in English": "1. Issues currency notes on behalf of the central government. 2. Supervises the functioning of formal sources of loans.",
        "Answer in Hindi": "1. केन्द्र सरकार की तरफ से करेंसी नोट जारी करता है। 2. यह ऋणों के औपचारिक स्रोतों की कार्यप्रणाली पर नजर रखता है।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "Clarify the difference between formal and informal sources of credit.",
        "Question in Hindi": "साख के औपचारिक एवं अनौपचारिक स्रोतों में अन्तर स्पष्ट कीजिये।",
        "Answer in English": "Formal sources include banks and cooperatives, supervised by the RBI, and have lower interest rates. Informal sources include moneylenders, traders, employers, relatives, and friends, are not supervised by any organization, and often charge higher interest rates.",
        "Answer in Hindi": "औपचारिक स्रोतों में बैंक और सहकारी समितियाँ आती हैं, इनकी कार्यप्रणाली पर आरबीआई नजर रखता है, और इनकी ब्याज दर कम होती है। अनौपचारिक स्रोतों में साहूकार, व्यापारी, मालिक, रिश्तेदार, दोस्त आदि आते हैं, इनका कोई पर्यवेक्षण नहीं होता, और ये अक्सर अधिक ब्याज वसूलते हैं।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "Write any two benefits of 'Self Help Groups' (SHG).",
        "Question in Hindi": "'स्वयं सहायता समूह' (SHG) के कोई दो लाभ लिखिए।",
        "Answer in English": "1. They help borrowers overcome the problem of lack of collateral. 2. Members can get loans for a variety of purposes at a reasonable interest rate.",
        "Answer in Hindi": "1. ये कर्जदारों को ऋणाधार की कमी की समस्या से उबरने में मदद करते हैं। 2. सदस्यों को विभिन्न उद्देश्यों के लिए उचित ब्याज दर पर ऋण मिल जाता है।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "What is the reason that banks are not ready to lend to some borrowers?",
        "Question in Hindi": "क्या कारण है कि बैंक कुछ कर्जदारों को कर्ज देने के लिए तैयार नहीं होते?",
        "Answer in English": "Banks may not lend to some borrowers due to lack of collateral, incomplete documentation, or a poor credit history.",
        "Answer in Hindi": "बैंक कुछ कर्जदारों को कर्ज देने के लिए तैयार नहीं होते क्योंकि उनके पास समर्थक ऋणाधार (गिरवी रखने के लिए संपत्ति) की कमी होती है, या उनके कागजात पूरे नहीं होते, या उनका पिछला रिकॉर्ड खराब होता है।",
        "Marks": "3"
    },
    {
        "Chapter": "20",
        "Questions type": "Short Answer",
        "Question in English": "What is written on a 10 rupee note?",
        "Question in Hindi": "10 के नोट के ऊपर क्या लिखा होता है?",
        "Answer in English": "\"I Promise to pay the bearer the sum of ten rupees\" - Governor.",
        "Answer in Hindi": "\"मैं धारक को दस रुपये अदा करने का वचन देता हूँ\" - गवर्नर।",
        "Marks": "3"
    }
]

file_path = "batch_54_56.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON data successfully written to {file_path}")
