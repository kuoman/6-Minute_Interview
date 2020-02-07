class PhoneNumber:
    USA = 0

    CountryCodes = { "1", "20", "212", "213", "216", "218", "220", "221", "222", "223",
                     "224", "225", "226", "227", "228", "229", "230", "231", "232", "233",
                     "234", "235", "236", "237", "238", "239", "240", "241", "242", "243",
                     "244", "245", "246", "247", "248", "249", "250", "251", "252", "253",
                     "254", "255", "256", "257", "258", "260", "261", "262", "263", "264",
                     "265", "266", "267", "268", "269", "27", "290", "291", "297", "298",
                     "299", "30", "31", "32", "33", "34", "350", "351", "352", "353",
                     "354", "355", "356", "357", "358", "359", "36", "370", "371", "372",
                     "373", "374", "375", "376", "377", "378", "380", "381", "385", "386",
                     "387", "389", "39", "40", "41", "420", "421", "423", "43", "44",
                     "45", "46", "47", "48", "49", "500", "501", "502", "503", "504",
                     "505", "506", "507", "508", "509", "51", "52", "53", "5399", "54",
                     "55", "56", "57", "58", "590", "591", "592", "593", "594", "595",
                     "596", "597", "598", "599", "60", "61", "618", "62", "63", "64",
                     "65", "66", "670", "672", "673", "674", "675", "676", "677", "678",
                     "679", "680", "681", "682", "683", "684", "685", "686", "687", "688",
                     "689", "690", "691", "692", "7", "808", "81", "82", "84", "850",
                     "852", "853", "855", "856", "86", "870", "871", "872", "873", "874",
                     "878", "880", "881", "8816", "8817", "88213", "88216", "886", "90", "91",
                     "92", "93", "94", "95", "960", "961", "962", "963", "964", "965",
                     "966", "967", "968", "970", "971", "972", "973", "974", "975", "976",
                     "977", "98", "992", "993", "994", "995", "996", "998"};

    Reasons = {"Phone Number Too Long or Too Short", "US Number must be length 10", "Unknown Country Code"}

    #** The original value.
    originalValue = None

    # An index into the COUNTRY_CODES array
    countryCodeIndex = USA
    __stripped_value = None
    __invalid_reason = None

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def __init__(self, original_value):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    # *Reduce the string to just numbers * /
    def strip_phone_number(self, number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_country_code_index(self, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def validate(self, country_code_index, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    #*
    #*  International Phone number must be between 9-15 chars
    #*/
    def validate_international(self, country_code_index, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def validate_north_american(self, country_code_index, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def extract_phone_body(self, country_code_index, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_value_as_north_american(self, country_code_index, stripped_number):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_value_as_international(self, country_code_index, stripped):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def is_valid(self):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_invalid_reason(self):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def is_north_american_number(self):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_original_text(self):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    def get_stripped_number(self):
        pass

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
