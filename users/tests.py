import email
from django.test import TestCase

# Create your tests here.
from .models import User

class UserTest(TestCase):
    def first_user_test_case(self):
        self.assertEquals(1,1)
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        User.objects.create(username='EOC', email='eoc@gmail.com', first_name ='Ethan', last_name = 'Cov')
        User.objects.create(username='MSY', email='msy@gmail.com', first_name ='Max', last_name = 'imus')

    def test_is_active_pass(self): #should pass
        user = User.objects.get(id=1)
        is_active = user.is_active
        self.assertEqual(is_active,True)
    
    def test_is_active_fail(self): #should fail
        user = User.objects.get(id=1)
        is_active = user.is_active
        self.assertEqual(is_active,False)

    def test_is_active_mod_fail(self): #should fail
        user = User.objects.get(id=1)
        is_active_old = user.is_active
        user.is_active = False
        user.save()
        updated_user = User.objects.get(id =1)
        is_active_new = updated_user.is_active
        self.assertEqual(is_active_new, is_active_old)
    
    def test_username_pass(self): #should pass
        user = User.objects.get(id=1)
        uname = user.username
        self.assertEqual(uname,'EOC')
    
    def test_username_fail(self): #should fail
        user = User.objects.get(id=1)
        uname = user.username
        self.assertEqual(uname,'eoc')   

    def test_username_mod_fail(self): #should fail
        user = User.objects.get(id=1)
        old_user_name = user.username
        user.username = 'EthanCovert'
        user.save()
        updated_user = User.objects.get(id =1)
        new_user_name = updated_user.username
        self.assertEqual(new_user_name, old_user_name)     
    
    def test_first_name_pass(self): #should pass
        user = User.objects.get(id=1)
        fname = user.first_name
        self.assertEqual(fname,'Eth')
    
    def test_first_name_fail(self): #should fail
        user = User.objects.get(id=1)
        fname = user.first_name
        self.assertEqual(fname,'covert')

    def test_first_name_mod_fail(self): #should fail
        user = User.objects.get(id=1)
        old_fname = user.first_name
        user.first_name = 'Ethan'
        user.save()
        updated_user = User.objects.get(id =1)
        new_fname = updated_user.first_name
        self.assertEqual(new_fname, old_fname)
    
    def test_last_name_pass(self): #should pass
        user = User.objects.get(id=1)
        lname = user.last_name       
        self.assertEqual(lname,'cov')
    
    def test_last_name_fail(self): #should fail
        user = User.objects.get(id=1)
        lname = user.last_name
        self.assertEqual(lname,'covert')

    def test_last_name_mod_fail(self): #should fail
        user = User.objects.get(id=1)
        old_lname = user.last_name
        user.last_name = 'Covert'
        user.save()
        updated_user = User.objects.get(id =1)
        new_lname = updated_user.last_name
        self.assertEqual(new_lname, old_lname)

    def test_email_pass(self): #should pass
        user = User.objects.get(id=1)
        email = user.email       
        self.assertEqual(email,'eoc@gmail.com')
    
    def test_email_fail(self): #should fail
        user = User.objects.get(id=1)
        email = user.email
        self.assertEqual(email,'eoc@gmail')

    def test_email_mod_fail(self): #should fail
        user = User.objects.get(id=1)
        old_email = user.email
        user.email = 'ethancovert@csus.edu'
        user.save()
        updated_user = User.objects.get(id =1)
        new_email = updated_user.email
        self.assertEqual(new_email, old_email)




'''
class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
'''