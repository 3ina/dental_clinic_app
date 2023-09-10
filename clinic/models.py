from django.db import models


class Clinic(models.Model):

    name = models.CharField(max_length=255,default="")
    address = models.CharField(max_length=255,default="")
    email = models.EmailField(default="")
    number = models.CharField(max_length=255,default="")
    offer = models.CharField(max_length=255,blank=True)
    offer_desc = models.CharField(max_length=255,blank=True)
    instagram = models.CharField(max_length=255,blank=True)
    twitter = models.CharField(max_length=255,blank=True)
    facebook = models.CharField(max_length=255,blank=True)
    linkedin = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.name


class About(models.Model):
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name="about")
    maindesc = models.CharField(max_length=255,null=False,default="")
    firstdesc = models.CharField(max_length=255,null=True,blank=True)
    seconddesc = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/about')


class Testimonial(models.Model):
    clinic = models.ForeignKey(Clinic,related_name="testimonial",on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    client_image = models.ImageField(upload_to='images/clients',default='./defaultClientPic.png')
    desc = models.CharField(max_length=600)

    def __str__(self):
        return  self.client_name



class OpeningTime(models.Model):
    clinic = models.ManyToManyField(Clinic,related_name="time_opening")
    time  = models.CharField(max_length=255)


class Doctor(models.Model):
    clinic = models.ManyToManyField(Clinic)
    name = models.CharField(max_length=255,default="")
    Expertise = models.CharField(max_length=255,default="")
    image =models.ImageField(upload_to='images/doctor',blank=True)
    instagram = models.CharField(max_length=255,blank=True)
    twitter = models.CharField(max_length=255,blank=True)
    facebook = models.CharField(max_length=255,blank=True)
    linkedin = models.CharField(max_length=255,blank=True)


    def __str__(self):
       return self.name


class Service(models.Model):
    doctor = models.ManyToManyField(Doctor,related_name="services")
    name = models.CharField(max_length=255,null=False)
    price = models.PositiveSmallIntegerField(null=False,default=0)
    desc = models.CharField(max_length=400,null=False)
    image = models.ImageField(upload_to="images/services",blank=True)

    def __str__(self):
        return self.name