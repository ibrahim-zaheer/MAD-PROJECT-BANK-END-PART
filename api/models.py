from django.db import models

# Create your models here.

class Notes(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50]
    class Meta:
        ordering = ['updated']


class UserProfileAfterLogin(models.Model):   
    username = models.TextField(default="Ibrahim")     
    password = models.TextField(default='1234')


class UserProfileBeforeLogin(models.Model):   
    username = models.TextField(default="Ibrahim")     
    password = models.TextField(default='1234')  
    email = models.EmailField(default='1234')  
    phoneNumber = models.TextField(default='1234') 
    role = models.TextField(default="Investor") 

class ProperProfileCreation(models.Model):
    #all this will be supplied by the previous classes
    UserId = models.IntegerField(default=100)
    username = models.TextField(default="Ibrahim")     
    password = models.TextField(default='1234')  
    email = models.EmailField(default='1234')  
    phoneNumber = models.TextField(default='1234') 
    role = models.TextField(default="Investor")
    # data now supplied by the user
    date_of_birth = models.DateField(default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default='Lahore')
    country = models.CharField(max_length=100, default='Pakistan')
    postalCode = models.IntegerField(default=54000)
    latest_job = models.CharField(max_length=1000, default='student')
    salary_Income_allowance = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    is_married = models.CharField(max_length=200,default="unmarried")
    cnic_number = models.CharField(max_length=15, default='000000000', blank=True)

    def __str__(self):
        return self.user.username





class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')


class EntrepreneurProfile(models.Model):
    UserId = models.IntegerField(default=1)
    
    # Professional Information
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Company Name')
    industry_expertise = models.CharField(max_length=100, verbose_name='Industry/Field of Expertise')
    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    
    # Entrepreneurial Background
    previous_venture = models.TextField(verbose_name='Previous Ventures/Projects (with descriptions and outcomes)')
    years_of_experience = models.PositiveIntegerField(verbose_name='Years of Experience as an Entrepreneur')
    achievements = models.TextField(verbose_name='Achievements or Recognitions')
    
    # Key Skills
    key_skills = models.CharField(max_length=255, verbose_name='Key Skills (e.g., leadership, project management, finance)')
    
    # Education
    highest_education_attained = models.CharField(max_length=100, verbose_name='Highest Level of Education Attained')
    
    # Profile Image
    profile_image = models.TextField(default='image', blank=True, null=True, verbose_name='Profile Image')
    
    # Social Media Links
    linkedin_profile = models.TextField(blank=True, null=True, verbose_name='LinkedIn Profile',default="https://twitter.com")
    twitter_profile = models.TextField(blank=True, null=True, verbose_name='Twitter Profile',default="https://twitter.com")
    # Add more social media links as needed
    
    # Bio/Introduction
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Entrepreneur Profile"



class Project(models.Model):
    UserId = models.IntegerField(default=1)
    project_id = models.AutoField(primary_key=True, verbose_name='Project ID')
    name = models.CharField(max_length=255, verbose_name='Project Name')
    field = models.CharField(max_length=100, verbose_name='Field')
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Minimum Investment (USD)')
    guaranteed_profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Guaranteed Profit (USD)')
    chance_of_risk = models.FloatField(verbose_name='Chance of Risk (%)')
    description = models.TextField(verbose_name='Project Description')
    time_scale = models.CharField(max_length=50, verbose_name='Time Scale')

    def save(self, *args, **kwargs):
        # Check if the project_id is not set (i.e., creating a new row)
        if not self.project_id:
            # Find the highest project_id in the database and increment it by 1
            latest_project = Project.objects.order_by('-project_id').first()
            self.project_id = 1 if not latest_project else latest_project.project_id + 1

        super(Project, self).save(*args, **kwargs)

class InvestorProject(models.Model):
    UserId = models.IntegerField()
    investment_id = models.AutoField(primary_key=True, verbose_name='Project ID')
    field_of_investment = models.CharField(max_length=260, verbose_name='Project Name')
    # years_of_investment = models.CharField(max_length=255, verbose_name='Field')
    # minimum_investment = models.CharField(max_length=50, verbose_name='Minimum Investment (USD)')
    # minimum_profit = models.CharField(max_length=50, verbose_name='Guaranteed Profit (USD)')
    years_of_investment = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Field')
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Minimum Investment (USD)')
    minimum_profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Guaranteed Profit (USD)')
    allowed_risk = models.FloatField(verbose_name='Chance of Risk (%)')
    description = models.TextField(verbose_name='Project Description')
    time_scale_allowed = models.CharField(max_length=50, verbose_name='Time Scale')

    def save(self, *args, **kwargs):
        # Check if the project_id is not set (i.e., creating a new row)
        if not self.investment_id:
            # Find the highest project_id in the database and increment it by 1
            latest_project = InvestorProject.objects.order_by('-investment_id').first()
            self.investment_id = 1 if not latest_project else latest_project.investment_id + 1

        super(InvestorProject, self).save(*args, **kwargs)  


    @classmethod
    def delete_all_rows(cls):
        cls.objects.all().delete()          