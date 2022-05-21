class User:
    def __init__(self, fname, lname, username, password, location, type):
        self.is_admin = False
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.location = location
        self.type = type

    def get_location(self):
        return self.location

    def get_user(self):
        return self.username

    def get_pass(self):
        return self.password

    def get_type(self):
    		return self.type


class Admin(User):
	def __init__(self, fname, lname, username, password, location, type):
		User.__init__(self, fname, lname, username, password, location, type)
		self.fname = fname
		self.lname = lname
		self.username = username
		self.password = password
		self.location = location
		self.type = type


class Provider(User):
    def __init__(self, fname, lname, username, password, location, type,
                 license_num, verif_code, specialties, transportation):
        User.__init__(self, fname, lname, username, password, location, type)
        self.license_num = license_num
        self.verif_code = verif_code
        self.specialties = specialties
        self.transportation = transportation
        self.available = False

    def get_license(self):
        return self.license_num

    def get_verification(self):
        return self.verif_code

    def get_specialties(self):
        return self.specialties

    def get_transportation(self):
        return self.transportation

    def get_avail(self):
        return self.available

    def set_avail(self, mode):
        self.available = mode


class Student(User):
    def __init__(self, fname, lname, username, password, location, type, school_code, disabilities, specific_need):
        User.__init__(self, fname, lname, username, password, location, type)
        self.school_code = school_code
        self.disabilities = disabilities
        self.specific_need = specific_need
        self.type = type

    def get_school(self):
        return self.school_code

    def get_disabilities(self):
        return self.disabilities

    def get_need(self):
        return self.specific_need

    def set_need(self, need):
        self.specific_need = need
