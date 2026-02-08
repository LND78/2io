import json

data = [
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Generally, on what basis can the development of a country be determined?",
        "Question_Hindi": "सामान्यता किसी देश का विकास किस आधार पर निर्धारित किया जा सकता है-",
        "Answer_English": "(d) All of the above",
        "Answer_Hindi": "(द) उपरोक्त सभी",
        "Marks": 1,
        "Options": {
             "a": "Per capita income",
             "b": "Average literacy rate",
             "c": "Health status of people",
             "d": "All of the above"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Among the following neighboring countries, which country's situation is better than India in terms of human development?",
        "Question_Hindi": "निम्नलिखित पड़ोसी देशों में से मानव विकास के लिहाज से किस देश की स्थिति भारत से बेहतर है।",
        "Answer_English": "(b) Sri Lanka",
        "Answer_Hindi": "(ब) श्रीलंका",
        "Marks": 1,
        "Options": {
             "a": "Bangladesh",
             "b": "Sri Lanka",
             "c": "Nepal",
             "d": "Pakistan"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Which of the following states has the best position in India on the basis of literacy rate?",
        "Question_Hindi": "भारत में साक्षरता दर के आधार पर सबसे अच्छी स्थिति निम्न में से किस राज्य की है।",
        "Answer_English": "(b) Kerala",
        "Answer_Hindi": "(ब) केरल",
        "Marks": 1,
        "Options": {
             "a": "Rajasthan",
             "b": "Kerala",
             "c": "Bihar",
             "d": "Punjab"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Which of the following is a non-renewable resource?",
        "Question_Hindi": "निम्न में से गैर नवीकरणीय साधन है -",
        "Answer_English": "(a) Crude oil",
        "Answer_Hindi": "(अ) कच्चा तेल",
        "Marks": 1,
        "Options": {
             "a": "Crude oil",
             "b": "Groundwater",
             "c": "Forest",
             "d": "All of the above"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Which organization releases the Human Development Report?",
        "Question_Hindi": "मानव विकास रिपोर्ट कौनसी संस्था जारी करती है-",
        "Answer_English": "(c) UNDP",
        "Answer_Hindi": "(स) यू.एन.डी.पी.",
        "Marks": 1,
        "Options": {
             "a": "World Bank",
             "b": "Asian Development Bank",
             "c": "UNDP",
             "d": "Reserve Bank of India"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Country with middle income group is-",
        "Question_Hindi": "मध्य आय वर्ग वाला देश है-",
        "Answer_English": "(b) India",
        "Answer_Hindi": "(ब) भारत",
        "Marks": 1,
        "Options": {
             "a": "USA",
             "b": "India",
             "c": "China",
             "d": "Japan"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "According to the World Bank, what criterion has been used to compare development in different countries?",
        "Question_Hindi": "विश्व बैंक के अनुसार विभिन्न देशों में विकास के आधार पर तुलना करने के लिए किस मापदण्ड का प्रयोग किया?",
        "Answer_English": "(b) Per Capita Income",
        "Answer_Hindi": "(ब) प्रतिव्यक्ति आय",
        "Marks": 1,
        "Options": {
             "a": "National Income",
             "b": "Per Capita Income",
             "c": "Gross National Product",
             "d": "Gross National Income"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Average income is called-",
        "Question_Hindi": "औसत आय को कहा जाता है-",
        "Answer_English": "(a) Per capita income",
        "Answer_Hindi": "(अ) प्रति व्यक्ति आय",
        "Marks": 1,
        "Options": {
             "a": "Per capita income",
             "b": "National income",
             "c": "Single national product",
             "d": "Gross national income"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "According to Economic Survey 2019-20, the state with highest per capita income is-",
        "Question_Hindi": "आर्थिक सर्वेक्षण 2019-20 के अनुसार सर्वाधिक प्रतिव्यक्ति आय है-",
        "Answer_English": "(b) Haryana",
        "Answer_Hindi": "(ब) हरियाणा",
        "Marks": 1,
        "Options": {
             "a": "Rajasthan",
             "b": "Haryana",
             "c": "Bihar",
             "d": "Uttar Pradesh"
        }
    },
    {
        "Chapter": 18,
        "Type": "MCQ",
        "Question_English": "Sardar Sarovar Dam is situated on which river?",
        "Question_Hindi": "सरदार सरोवर बांध किस नदी पर स्थित है?",
        "Answer_English": "(c) Narmada",
        "Answer_Hindi": "(स) नर्मदा",
        "Marks": 1,
        "Options": {
             "a": "Ganga",
             "b": "Yamuna",
             "c": "Narmada",
             "d": "Kaveri"
        }
    },
    {
        "Chapter": 18,
        "Type": "Short Answer",
        "Question_English": "Clarify why sustainability is important for development.",
        "Question_Hindi": "विकास के लिए धारणीयता (सतत पोषणीय) महत्वपूर्ण क्यों है स्पष्ट कीजिए-",
        "Answer_English": "The level of development which is achieved without burdening the future generation is called sustainable or continuous development. 1. Due to rapid economic development, natural resources are exploited excessively, due to which natural resources will be exhausted, which will endanger the development of all countries in the future. 2. Rapid industrialization causes damage to the environment and ecology, which becomes the cause of pollution and disturbs the natural balance in the future.",
        "Answer_Hindi": "विकास का वह स्तर जो भावी पीढ़ी पर बिना बोझ डाले प्राप्त किया जाता है सतत् विकास अथवा धारणीय विकास कहलाता है। \n1. तीव्र आर्थिक विकास से प्राकृतिक संसाधनों का अत्यधिक दोहन से प्राकृतिक संसाधन समाप्त हो जायेंगे जिससे भविष्य में सभी देशों का विकास खतरे में पड़ जायेगा। \n2. तीव्र औद्योगिकीकरण से पर्यावरण एवं पारिस्थितिकी को नुकसान पहुंचाता है जो प्रदूषण का कारण बनते है एवं भविष्य में प्राकृतिक संतुलन को बाधित करते है।",
        "Marks": 2
    },
    {
        "Chapter": 18,
        "Type": "Short Answer",
        "Question_English": "What sources of energy are used by the people of India? What could be its future possibilities?",
        "Question_Hindi": "भारत के लोगों द्वारा ऊर्जा के किन स्रोतों का प्रयोग किया जाता है? इसकी भविष्य में क्या संभावनाएं हो सकती है।",
        "Answer_English": "Conventional Sources: (1) Coal (2) Mineral Oil (3) Natural Gas (4) Electricity. Non-conventional Sources: (1) Wind Energy (2) Solar Energy (3) Bio Gas (4) Geothermal Energy (5) Tidal Energy. Due to the pressure of increasing population and continuous exploitation of natural resources, the demand for petroleum and related products will increase. Due to shortage of supply, the prices of these products will increase continuously, making their import expensive. Consequently, a situation of balance of payments imbalance will arise. Therefore, new energy sources will have to be discovered and dependence on non-conventional sources of energy will increase.",
        "Answer_Hindi": "परम्परागत स्रोत (1) कोयला (2) खनिज तेल (3) प्राकृतिक गैस (4) विद्युत\nगैर परम्परागत स्रोत (1) पवन ऊर्जा (2) सौर ऊर्जा (3) बायो गैस (4) भूतापीय ऊर्जा (5) ज्वारीय ऊर्जा\nबढ़ते जनसंख्या के दबाव एवं प्राकृतिक संसाधनों के निरन्तर दोहन के कारण पेट्रोलियम एवं संबद्ध उत्पादों की मांग बढ़ेगी, पूर्ति कम होने के कारण इन उत्पादों के मूल्यों में निरन्तर वृद्धि के कारण इनका आयात महंगा होगा। फलस्वरूप भुगतान असंतुलन की स्थिति पैदा होगी। अतः नये-नये ऊर्जा स्रोतों को खोजना होगा तथा ऊर्जा के गैर परम्परागत स्रोतों पर निर्भरता बढ़ेगी।",
        "Marks": 2
    },
    {
        "Chapter": 18,
        "Type": "Short Answer",
        "Question_English": "State the importance of Human Development Index.",
        "Question_Hindi": "मानव विकास सूचकांक का महत्व बताइए।",
        "Answer_English": "The importance of Human Development Index is as follows- (1) It indicates the level of development of the country. (2) Through this, information about life expectancy, literacy and real per capita income is obtained. (3) It indicates the condition and direction of human development in different countries.",
        "Answer_Hindi": "मानव विकास सूचकांक का महत्व निम्नलिखित है- (1) यह देश के विकास के स्तर का संकेत देता है। (2) इसके माध्यम से जीवन प्रत्याशा, साक्षरता एवं वास्तविक प्रति व्यक्ति आय की जानकारी मिलती है। (3) यह विभिन्न देशों में मानव विकास की दशा एवं दिशा को बतलाता है।",
        "Marks": 2
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Production of a commodity from natural resources is an activity of the ............ sector.",
        "Question_Hindi": "एक वस्तु का प्राकृतिक संसाधनों से उत्पादन .................... क्षेत्रक की गतिविधि है।",
        "Answer_English": "Primary",
        "Answer_Hindi": "प्राथमिक",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Disguised unemployment in India is found most in the ............ sector.",
        "Question_Hindi": "भारत में छिपी हुई बेरोजगारी सबसे अधिक .................... क्षेत्र में पाई जाती है।",
        "Answer_English": "Agriculture",
        "Answer_Hindi": "कृषि",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Tertiary sector is also called ............ sector.",
        "Question_Hindi": "तृतीयक क्षेत्रक को .................... भी कहा जाता है।",
        "Answer_English": "Service",
        "Answer_Hindi": "सेवा",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "At present, the maximum contribution to the national income in India is of the ............ sector.",
        "Question_Hindi": "वर्तमान में भारत की राष्ट्रीय आय में सर्वाधिक योगदान .................... का है।",
        "Answer_English": "Tertiary",
        "Answer_Hindi": "तृतीयक",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "The value of all final goods and services produced within a country in a particular year is called ............ .",
        "Question_Hindi": "किसी देश के भीतर किसी विशेष वर्ष में उत्पादित सभी वस्तुओं और सेवाओं का मूल्य ............ कहलाता है।",
        "Answer_English": "Gross Domestic Product (GDP)",
        "Answer_Hindi": "GDP (सकल घरेलू उत्पाद)",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "............ are used in the production of final goods and services.",
        "Question_Hindi": "............ अंतिम वस्तुओं और सेवाओं निर्माण में इस्तेमाल की जाती है।",
        "Answer_English": "Intermediate goods",
        "Answer_Hindi": "मध्यवर्ती वस्तुएं",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "The value of intermediate goods is already included in the value of ............ .",
        "Question_Hindi": "अंतिग वस्तुओं के मूल्य में ........ का मूल्य पहले से ही शामिल होता है।",
        "Answer_English": "Final goods",
        "Answer_Hindi": "मध्यवर्ती वस्तुए",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Full name of MNREGA is ............ .",
        "Question_Hindi": "मनरेगा का पूरा नाम ................ है।",
        "Answer_English": "Mahatma Gandhi National Rural Employment Guarantee Act",
        "Answer_Hindi": "महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार गारन्टी अधिनियम",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "The responsibility of distribution of assets and services in the ............ lies in the hands of a single person or company.",
        "Question_Hindi": "......... में परिसम्पत्तियों पर स्वामित्व और सेवाओं के वितरण की जिम्मेदारी एकल व्यक्ति या कंपनी के हाथों में होती है।",
        "Answer_English": "Private sector",
        "Answer_Hindi": "निजी क्षेत्र",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Full name of TISCO is ............ .",
        "Question_Hindi": "टिस्को का पूरा नाम ............ है।",
        "Answer_English": "Tata Iron and Steel Company Limited",
        "Answer_Hindi": "टाटा आयरन एंड स्टील कम्पनी लिमिटेड (टिस्को)",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Cotton is a ............ product and cloth is a ............ product.",
        "Question_Hindi": "कपास एक ......... उत्पाद है और कपड़ा एक ......... उत्पाद है।",
        "Answer_English": "Primary, Final",
        "Answer_Hindi": "प्राथमिक, अन्तिम",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Secondary sector is also called ............ .",
        "Question_Hindi": "द्वितीयक क्षेत्रक को ...... भी कहा जाता है।",
        "Answer_English": "Industrial sector",
        "Answer_Hindi": "औद्योगिक क्षेत्रक",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "In the public sector, the ownership of most assets is with the ............ .",
        "Question_Hindi": "सार्वजनिक क्षेत्रक में अधिकांश परिसंपत्तियों पर ...... का स्वामित्व होता है।",
        "Answer_English": "Government",
        "Answer_Hindi": "सरकार",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Fill in the Blank",
        "Question_English": "Workers of the ............ sector do not produce goods.",
        "Question_Hindi": "........ क्षेत्रक के श्रमिक वस्तुओं का उत्पादन नहीं करते है।",
        "Answer_English": "Tertiary",
        "Answer_Hindi": "तृतीयक",
        "Marks": 1
    },
    {
        "Chapter": 19,
        "Type": "Short Answer",
        "Question_English": "Differentiate between Open Unemployment and Disguised Unemployment.",
        "Question_Hindi": "खुली बेरोजगारी और प्रच्छन्न बेरोजगारी के बीच विभेद कीजिए-",
        "Answer_English": "That unemployment in which people do not have employment and sit idle is called Open Unemployment. While underemployment in which a person seems to be working but his productivity is negligible is also called Disguised Unemployment. It is mostly found in the agriculture sector of India.",
        "Answer_Hindi": "वह बेरोजगारी जिसमें लोगों के पास रोजगार नहीं है और बेकार बैठे हुए है। खुली बेरोजगारी कहलाता है। जबकि अल्प बेरोजगारी जिससे व्यक्ति काम में लगा हुआ होता है किन्तु उसकी उत्पादकता नगन्य होती है को प्रच्छन्न बेरोजगारी भी कहा जाता है। भारत के कृषि क्षेत्र में बहुधा पाई जाती है।",
        "Marks": 2
    },
    {
        "Chapter": 19,
        "Type": "Short Answer",
        "Question_English": "State any two differences between Organized and Unorganized sector.",
        "Question_Hindi": "संगठित एंव असंगठित क्षेत्रक में कोई दो अन्तर बताइए-",
        "Answer_English": "1. Unorganized sector refers to those small and scattered units which are largely outside government control. While organized sector is that place of enterprise or work where the term of employment is regular. Government rules and regulations have to be followed. 2. Terms of employment in unorganized sector are unregulated while terms of employment in organized sector are regulated.",
        "Answer_Hindi": "1. असंगठित क्षेत्र से आशय उन छोटी-मोटी एवं बिखरी इकाइयों से है जो अधिकांशतः राजकीय नियंत्रण से बाहर होती है। जबकि संगठित क्षेत्रक उस उधम या कार्य के स्थान से है, वहाँ रोजगार की अवधि नियमित होती है। सरकारी नियमों व विनियमों का पालन करना होता है। \n2. असंगठित क्षेत्रक में रोजगार की शर्तें अनियंत्रित होती है जबकि संगठित क्षेत्रक में रोजगार की शर्तें नियंत्रित होती है।",
        "Marks": 2
    },
    {
        "Chapter": 19,
        "Type": "Short Answer",
        "Question_English": "What do you understand by Tertiary sector?",
        "Question_Hindi": "तृतीयक क्षेत्रक से आपका क्या अभिप्राय है?",
        "Answer_English": "Apart from primary and secondary sectors, all other activities are included in the tertiary sector. Those activities come under this which help in the development of primary and secondary sectors. Such as transport, communication, banking etc.",
        "Answer_Hindi": "प्राथमिक एवं द्वितीयक क्षेत्रक के अतिरिक्त अन्य समस्त गतिविधियों को तृतीयक क्षेत्रक में सम्मिलित किया जाता है। इसके अन्तर्गत वे क्रियाएं आती है जो प्राथमिक और द्वितीयक क्षेत्रक के विकास में सहायता करती है।",
        "Marks": 2
    }
]

with open("batch_51_53.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
