from flask import Flask, render_template, request
import pickle
import os

countryCodeDict = {'Afghanistan': '002',
 'Albania': '003',
 'Algeria': '004',
 'Angola': '007',
 'Argentina': '009',
 'Armenia': '001',
 'Australia': '010',
 'Austria': '011',
 'Azerbaijan': '052',
 'Bahamas': '012',
 'Bahrain': '013',
 'Bangladesh': '016',
 'Barbados': '014',
 'Belarus': '057',
 'Belgium': '255',
 'Belize': '023',
 'Benin': '053',
 'Bhutan': '018',
 'Bolivia': '019',
 'Bosnia and Herzegovina': '080',
 'Botswana': '020',
 'Brazil': '021',
 'Brunei Darussalam': '026',
 'Bulgaria': '027',
 'Burkina Faso': '233',
 'Burundi': '029',
 'Cameroon': '032',
 'Canada': '033',
 'Central African Republic': '037',
 'Chad': '039',
 'Chile': '040',
 'China': '351',
 'Colombia': '044',
 'Congo': '046',
 'Congo, Democratic Republic of': '250',
 'Costa Rica': '048',
 'Croatia': '098',
 'Cuba': '049',
 'Czech Republic': '167',
 "CÃ\x83Â´te d'Ivoire": '107',
 'Denmark': '054',
 'Djibouti': '072',
 'Dominican Republic': '056',
 'Ecuador': '058',
 'El Salvador': '060',
 'Equatorial Guinea': '061',
 'Eritrea': '178',
 'Estonia': '063',
 'Eswatini': '209',
 'Ethiopia': '238',
 'Fiji': '066',
 'Finland': '067',
 'France': '068',
 'French Guiana': '069',
 'French Polynesia': '070',
 'Gabon': '074',
 'Gambia': '075',
 'Georgia': '073',
 'Germany': '079',
 'Ghana': '081',
 'Greece': '084',
 'Guadeloupe': '087',
 'Guatemala': '089',
 'Guinea': '090',
 'Guinea-Bissau': '175',
 'Guyana': '091',
 'Haiti': '093',
 'Hungary': '097',
 'India': '100',
 'Indonesia': '101',
 'Iran, Islamic Republic of': '102',
 'Iraq': '103',
 'Ireland': '104',
 'Israel': '105',
 'Italy': '106',
 'Jamaica': '109',
 'Japan': '110',
 'Jordan': '112',
 'Kazakhstan': '108',
 'Kenya': '114',
 "Korea, Democratic People's Republic of": '116',
 'Korea, Republic of': '117',
 'Kuwait': '118',
 'Kyrgyzstan': '113',
 "Lao People's Democratic Republic": '120',
 'Latvia': '119',
 'Lebanon': '121',
 'Lesotho': '122',
 'Liberia': '123',
 'Libyan Arab Jamahiriya': '124',
 'Lithuania': '126',
 'Luxembourg': '256',
 'Madagascar': '129',
 'Malawi': '130',
 'Malaysia': '131',
 'Mali': '133',
 'Malta': '134',
 'Mauritania': '136',
 'Mexico': '138',
 'Mongolia': '141',
 'Montenegro': '273',
 'Morocco': '143',
 'Mozambique': '144',
 'Myanmar': '028',
 'Namibia': '147',
 'Nepal': '149',
 'Netherlands': '150',
 'New Zealand': '156',
 'Nicaragua': '157',
 'Niger': '158',
 'Nigeria': '159',
 'Norway': '162',
 'Oman': '221',
 'Pakistan': '165',
 'Panama': '166',
 'Papua New Guinea': '168',
 'Paraguay': '169',
 'Peru': '170',
 'Philippines': '171',
 'Poland': '173',
 'Portugal': '174',
 'Qatar': '179',
 'Republic of Moldova': '146',
 'Republic of North Macedonia': '154',
 'Romania': '183',
 'Russian Federation': '185',
 'Rwanda': '184',
 'Saint Lucia': '189',
 'Saudi Arabia': '194',
 'Senegal': '195',
 'Serbia': '272',
 'Sierra Leone': '197',
 'Singapore': '200',
 'Slovakia': '199',
 'Slovenia': '198',
 'Solomon Islands': '025',
 'Somalia': '201',
 'South Africa': '202',
 'South Sudan': '277',
 'Spain': '203',
 'Sri Lanka': '038',
 'Sudan': '276',
 'Suriname': '207',
 'Sweden': '210',
 'Switzerland': '211',
 'Syrian Arab Republic': '212',
 'Tajikistan': '208',
 'Tanzania, United Republic of': '215',
 'Thailand': '216',
 'Timor-Leste': '176',
 'Togo': '217',
 'Trinidad and Tobago': '220',
 'Tunisia': '222',
 'Turkey': '223',
 'Turkmenistan': '213',
 'Uganda': '226',
 'Ukraine': '230',
 'United Arab Emirates': '225',
 'United Kingdom': '229',
 'United States of America': '231',
 'Uruguay': '234',
 'Uzbekistan': '235',
 'Venezuela, Bolivarian Republic of': '236',
 'Viet Nam': '237',
 'Yemen': '249',
 'Zambia': '251',
 'Zimbabwe': '181'}

def bioFootprintCalc(land_type):
    if land_type == "builtup":
        return 2.51
    elif land_type == "carbon":
         return 1.26
    elif land_type == "cropland":
         return 2.51
    elif land_type == "fishingground":
         return 0.37
    elif land_type == "forestland":
         return 1.26
    else:
         return 0.46

def switch(landType):
    if landType == "builtup":
        v10, v6, v7, v8, v9 = 0, 0, 0, 0, 0
        v5 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)
    elif landType == "carbon":
        v5, v10, v7, v8, v9 = 0, 0, 0, 0, 0
        v6 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)
    elif landType == "cropland":
        v5, v6, v10, v8, v9 = 0, 0, 0, 0, 0
        v7 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)
    elif landType == "fishingground":
        v5, v6, v7, v10, v9 = 0, 0, 0, 0, 0
        v8 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)
    elif landType == "forestland":
        v5, v6, v7, v8, v10 = 0, 0, 0, 0, 0
        v9 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)
    elif landType == "grazingland":
        v5, v6, v7, v8, v9 = 0, 0, 0, 0, 0
        v10 = 1
        return int(v5), int(v6), int(v7), int(v8), int(v9), int(v10)


server = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
cf_port = os.getenv("PORT")

#---------------- Home ----------------#
@server.route("/")
def home():
	return render_template('index.html')

#---------------- Prediction Form ----------------#
@server.route("/predictionForm")
def predictionForm():
	print("HEY")
	return render_template('predict.html')

#---------- ML Model endpoint ----------#
@server.route("/predictEcoFootprintML", methods =["GET", "POST"])
def getPrediction():
    country_name = float(request.form["country"])
    land_type = request.form["radio"]
    bio_total = float(request.form["bioTot"])
    eco_cons = float(request.form["ecoCons"])
    eco_prod = float(request.form["ecoProd"])
    eco_exp = float(request.form["ecoExports"])
    eco_imp = float(request.form["ecoImports"])

    print("RADIO", land_type)
    builtup, carbon, crop, fish, forest, graze = switch(land_type)
	
    eco_total = eco_prod + eco_cons + eco_exp + eco_imp
    bio_footprint = bio_total * bioFootprintCalc(land_type)

    filename = "random_forest.pickle"
    loaded_model = pickle.load(open(filename, "rb"))

    # T = [[-0.111125, -0.977002, 211, -0.903476, 0, 0, 0, 0, 0, 1]]
    input_values  = [[bio_total, eco_total, country_name, bio_footprint, builtup, carbon, crop, fish, forest, graze]]
    y_pred = loaded_model.predict(input_values)
    data=[
    {
        'value': y_pred[0]
    }]
    return render_template('results.html', data = data)


if __name__ == '__main__':
    # app.run()
	if cf_port is None:
		server.run(host='0.0.0.0', port=5000, debug=True)
	else:
		server.run(host='0.0.0.0', port=int(cf_port), debug=True)
    
